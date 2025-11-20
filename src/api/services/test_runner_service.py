"""
Service for running Hardhat tests on generated contracts.
"""
import subprocess
import json
import re
import os
import sys
from pathlib import Path
from typing import Tuple, List, Optional

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from ..models.job import TestResult
from src.cli.hardhat_test_runner import HardhatTestRunner, HardhatConfig, HardhatTestResult
from src.pipeline.pipeline_item import PIData


class TestRunnerService:
    """Service for executing Hardhat tests."""

    def __init__(self, hardhat_project_dir: Path, timeout: int = 300):
        """
        Initialize test runner service.

        Args:
            hardhat_project_dir: Path to Hardhat project directory
            timeout: Timeout in seconds for test execution
        """
        self.hardhat_project_dir = hardhat_project_dir
        self.timeout = timeout
        self._hardhat_runner = None

    def _get_runner(self, config: HardhatConfig) -> HardhatTestRunner:
        """Get or create HardhatTestRunner instance."""
        pi_data = PIData(key="HardhatTestRunner")
        return HardhatTestRunner(
            pipeline_item_data=pi_data,
            input_key_hardhat_config="hardhat_config",
            auto_install_deps=True
        )

    def run_full_test_pipeline(
        self,
        contracts_dir: Path,
        tests_dir: Path,
        network: str = "hardhat"
    ) -> Tuple[bool, TestResult, dict]:
        """
        Run the full test pipeline using HardhatTestRunner.

        Args:
            contracts_dir: Path to generated contracts
            tests_dir: Path to generated tests
            network: Network to run tests on

        Returns:
            Tuple of (success, test_result, artifacts)
        """
        config = HardhatConfig(
            project_dir=str(self.hardhat_project_dir),
            contracts_source_dir=str(contracts_dir),
            tests_source_dir=str(tests_dir),
            network=network,
            timeout_seconds=self.timeout
        )

        runner = self._get_runner(config)
        result = runner.run({"hardhat_config": config})

        # Convert HardhatTestResult to TestResult
        test_result_dict = result.get('test_result', {})
        test_result = TestResult(
            passed=test_result_dict.get('success', False),
            total_tests=test_result_dict.get('total_tests', 0),
            passed_tests=test_result_dict.get('passed_tests', 0),
            failed_tests=test_result_dict.get('failed_tests', 0),
            duration_ms=test_result_dict.get('duration_ms', 0),
            gas_used=test_result_dict.get('gas_used'),
            output=test_result_dict.get('output', ''),
            errors=test_result_dict.get('errors', [])
        )

        success = (
            result.get('setup_success', False) and
            result.get('install_success', False) and
            result.get('compile_success', False) and
            test_result.passed
        )

        return success, test_result, result.get('artifacts', {})

    def setup_hardhat_project(self, contracts_dir: Path, tests_dir: Path) -> Tuple[bool, List[str]]:
        """
        Set up Hardhat project structure for testing.

        Args:
            contracts_dir: Path to generated contracts
            tests_dir: Path to generated tests

        Returns:
            Tuple of (success, errors)
        """
        errors = []
        try:
            # Create project directory
            self.hardhat_project_dir.mkdir(parents=True, exist_ok=True)

            # Create hardhat.config.js if not exists
            config_path = self.hardhat_project_dir / 'hardhat.config.js'
            if not config_path.exists():
                config_content = '''require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: {
    version: "0.8.20",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
  networks: {
    hardhat: {
      chainId: 31337
    },
    localhost: {
      url: "http://127.0.0.1:8545",
      chainId: 31337
    }
  },
  paths: {
    sources: "./contracts",
    tests: "./test",
    cache: "./cache",
    artifacts: "./artifacts"
  }
};
'''
                with open(config_path, 'w') as f:
                    f.write(config_content)

            # Create package.json if not exists
            package_path = self.hardhat_project_dir / 'package.json'
            if not package_path.exists():
                package_content = {
                    "name": "dao-deployment-tests",
                    "version": "1.0.0",
                    "devDependencies": {
                        "@nomicfoundation/hardhat-toolbox": "^4.0.0",
                        "hardhat": "^2.19.0"
                    }
                }
                with open(package_path, 'w') as f:
                    json.dump(package_content, f, indent=2)

            # Create symlinks or copy contracts and tests
            project_contracts = self.hardhat_project_dir / 'contracts'
            project_tests = self.hardhat_project_dir / 'test'

            # Remove old symlinks/directories
            if project_contracts.is_symlink():
                project_contracts.unlink()
            elif project_contracts.exists():
                import shutil
                shutil.rmtree(project_contracts)

            if project_tests.is_symlink():
                project_tests.unlink()
            elif project_tests.exists():
                import shutil
                shutil.rmtree(project_tests)

            # Create symlinks
            project_contracts.symlink_to(contracts_dir.resolve())
            project_tests.symlink_to(tests_dir.resolve())

            return True, errors

        except Exception as e:
            errors.append(f"Hardhat setup error: {str(e)}")
            return False, errors

    def install_dependencies(self) -> Tuple[bool, List[str], str]:
        """
        Install Hardhat dependencies.

        Returns:
            Tuple of (success, errors, output)
        """
        try:
            result = subprocess.run(
                ['npm', 'install'],
                cwd=str(self.hardhat_project_dir),
                capture_output=True,
                text=True,
                timeout=120
            )

            if result.returncode != 0:
                return False, [result.stderr], result.stdout

            return True, [], result.stdout

        except subprocess.TimeoutExpired:
            return False, ["npm install timed out"], ""
        except Exception as e:
            return False, [str(e)], ""

    def compile_contracts(self) -> Tuple[bool, List[str], str]:
        """
        Compile Solidity contracts using Hardhat.

        Returns:
            Tuple of (success, errors, output)
        """
        try:
            result = subprocess.run(
                ['npx', 'hardhat', 'compile'],
                cwd=str(self.hardhat_project_dir),
                capture_output=True,
                text=True,
                timeout=self.timeout
            )

            if result.returncode != 0:
                return False, [result.stderr], result.stdout

            return True, [], result.stdout

        except subprocess.TimeoutExpired:
            return False, ["Compilation timed out"], ""
        except Exception as e:
            return False, [str(e)], ""

    def run_tests(self) -> TestResult:
        """
        Execute Hardhat tests.

        Returns:
            TestResult with execution details
        """
        try:
            result = subprocess.run(
                ['npx', 'hardhat', 'test', '--network', 'hardhat'],
                cwd=str(self.hardhat_project_dir),
                capture_output=True,
                text=True,
                timeout=self.timeout
            )

            output = result.stdout + result.stderr

            # Parse test results from output
            passed, total, failed = self._parse_test_output(output)

            # Extract gas usage if available
            gas_used = self._extract_gas_usage(output)

            # Calculate duration (rough estimate from output)
            duration_ms = self._extract_duration(output)

            errors = []
            if result.returncode != 0:
                errors.append(result.stderr if result.stderr else "Tests failed")

            return TestResult(
                passed=result.returncode == 0 and failed == 0,
                total_tests=total,
                passed_tests=passed,
                failed_tests=failed,
                duration_ms=duration_ms,
                gas_used=gas_used,
                output=output,
                errors=errors
            )

        except subprocess.TimeoutExpired:
            return TestResult(
                passed=False,
                total_tests=0,
                passed_tests=0,
                failed_tests=0,
                duration_ms=self.timeout * 1000,
                output="",
                errors=["Test execution timed out"]
            )
        except Exception as e:
            return TestResult(
                passed=False,
                total_tests=0,
                passed_tests=0,
                failed_tests=0,
                duration_ms=0,
                output="",
                errors=[str(e)]
            )

    def _parse_test_output(self, output: str) -> Tuple[int, int, int]:
        """Parse test counts from Hardhat output."""
        # Look for pattern like "X passing" and "Y failing"
        passing_match = re.search(r'(\d+)\s+passing', output)
        failing_match = re.search(r'(\d+)\s+failing', output)

        passed = int(passing_match.group(1)) if passing_match else 0
        failed = int(failing_match.group(1)) if failing_match else 0
        total = passed + failed

        return passed, total, failed

    def _extract_gas_usage(self, output: str) -> Optional[int]:
        """Extract gas usage from output if available."""
        # Look for gas report patterns
        gas_match = re.search(r'gas[:\s]+(\d+)', output, re.IGNORECASE)
        if gas_match:
            return int(gas_match.group(1))
        return None

    def _extract_duration(self, output: str) -> int:
        """Extract test duration from output."""
        # Look for duration pattern like "(123ms)" or "123 ms"
        duration_match = re.search(r'\((\d+)ms\)', output)
        if duration_match:
            return int(duration_match.group(1))

        # Alternative pattern
        duration_match = re.search(r'(\d+)\s*ms', output)
        if duration_match:
            return int(duration_match.group(1))

        return 0

    def get_artifacts(self) -> dict:
        """
        Get compiled contract artifacts.

        Returns:
            Dictionary of contract name -> artifact data
        """
        artifacts = {}
        artifacts_dir = self.hardhat_project_dir / 'artifacts' / 'contracts'

        if not artifacts_dir.exists():
            return artifacts

        for sol_dir in artifacts_dir.iterdir():
            if sol_dir.is_dir():
                for artifact_file in sol_dir.glob('*.json'):
                    # Skip debug files
                    if '.dbg.' in artifact_file.name:
                        continue

                    with open(artifact_file, 'r') as f:
                        artifact_data = json.load(f)

                    contract_name = artifact_file.stem
                    artifacts[contract_name] = {
                        'abi': artifact_data.get('abi', []),
                        'bytecode': artifact_data.get('bytecode', ''),
                        'deployedBytecode': artifact_data.get('deployedBytecode', ''),
                    }

        return artifacts
