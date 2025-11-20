"""
Hardhat test runner pipeline item for executing Solidity tests.
"""
import os
import subprocess
import json
import re
import shutil
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field

import src.cli.cli_executor as cli_module
import src.pipeline.pipeline_item as pi
import src.files.file_utils as file_utils
import src.utilities.utils as u


@dataclass
class HardhatTestResult:
    """Result of Hardhat test execution."""
    success: bool
    passed_tests: int = 0
    failed_tests: int = 0
    total_tests: int = 0
    duration_ms: int = 0
    gas_used: Optional[int] = None
    output: str = ""
    errors: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            'success': self.success,
            'passed_tests': self.passed_tests,
            'failed_tests': self.failed_tests,
            'total_tests': self.total_tests,
            'duration_ms': self.duration_ms,
            'gas_used': self.gas_used,
            'output': self.output,
            'errors': self.errors
        }


class HardhatConfig:
    """Configuration for Hardhat project setup and test execution."""

    def __init__(self,
                 project_dir: str,
                 contracts_source_dir: str = None,
                 tests_source_dir: str = None,
                 network: str = "hardhat",
                 solidity_version: str = "0.8.20",
                 timeout_seconds: int = 300):
        """
        Initialize Hardhat configuration.

        Args:
            project_dir: Directory for the Hardhat project
            contracts_source_dir: Source directory containing generated contracts
            tests_source_dir: Source directory containing generated tests
            network: Network to run tests on (hardhat, localhost)
            solidity_version: Solidity compiler version
            timeout_seconds: Timeout for test execution
        """
        self.project_dir = project_dir
        self.contracts_source_dir = contracts_source_dir
        self.tests_source_dir = tests_source_dir
        self.network = network
        self.solidity_version = solidity_version
        self.timeout_seconds = timeout_seconds

    def get_contracts_dir(self) -> str:
        return file_utils.concat_folder_filename(self.project_dir, "contracts")

    def get_tests_dir(self) -> str:
        return file_utils.concat_folder_filename(self.project_dir, "test")

    def get_artifacts_dir(self) -> str:
        return file_utils.concat_folder_filename(self.project_dir, "artifacts")

    def __repr__(self):
        return f"""HardhatConfig(
            project_dir={self.project_dir},
            contracts_source_dir={self.contracts_source_dir},
            tests_source_dir={self.tests_source_dir},
            network={self.network}
        )"""

    def to_json(self):
        return {
            'project_dir': self.project_dir,
            'contracts_source_dir': self.contracts_source_dir,
            'tests_source_dir': self.tests_source_dir,
            'network': self.network,
            'solidity_version': self.solidity_version,
            'timeout_seconds': self.timeout_seconds
        }


class HardhatTestRunner(cli_module.CLIExecutor):
    """Pipeline item for running Hardhat tests on generated Solidity contracts."""

    def __init__(self,
                 pipeline_item_data: pi.PIData,
                 input_key_hardhat_config: str,
                 auto_install_deps: bool = True,
                 printer_debug: u.PrinterDebug = None):
        """
        Initialize Hardhat test runner.

        Args:
            pipeline_item_data: Pipeline item data
            input_key_hardhat_config: Key to retrieve HardhatConfig from inputs
            auto_install_deps: Whether to auto-install npm dependencies if missing
            printer_debug: Debug printer
        """
        super().__init__(pipeline_item_data, inputs_as_separated_commands=False)
        if input_key_hardhat_config is None:
            raise Exception("HardhatTestRunner needs a non-None 'input_key_hardhat_config'")
        self.input_key_hardhat_config = input_key_hardhat_config
        self.auto_install_deps = auto_install_deps
        self.printer_debug = printer_debug

    def _debug(self, message: str):
        if self.printer_debug:
            self.printer_debug.print_debug(message)
        else:
            print(message)

    def get_config_from_inputs(self, inputs: dict) -> HardhatConfig:
        """Extract HardhatConfig from pipeline inputs."""
        config = inputs.get(self.input_key_hardhat_config)
        if config is None or not isinstance(config, HardhatConfig):
            raise Exception(f"Expected HardhatConfig, got: {type(config)}")
        return config

    def setup_hardhat_project(self, config: HardhatConfig) -> Tuple[bool, List[str]]:
        """
        Set up Hardhat project structure.

        Creates project directory, config files, and links contracts/tests.
        """
        errors = []
        try:
            # Create project directory
            os.makedirs(config.project_dir, exist_ok=True)

            # Create hardhat.config.js
            config_path = file_utils.concat_folder_filename(config.project_dir, "hardhat.config.js")
            config_content = f'''require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {{
  solidity: {{
    version: "{config.solidity_version}",
    settings: {{
      optimizer: {{
        enabled: true,
        runs: 200
      }}
    }}
  }},
  networks: {{
    hardhat: {{
      chainId: 31337
    }},
    localhost: {{
      url: "http://127.0.0.1:8545",
      chainId: 31337
    }}
  }},
  paths: {{
    sources: "./contracts",
    tests: "./test",
    cache: "./cache",
    artifacts: "./artifacts"
  }}
}};
'''
            with open(config_path, 'w') as f:
                f.write(config_content)

            # Create package.json if not exists
            package_path = file_utils.concat_folder_filename(config.project_dir, "package.json")
            if not os.path.exists(package_path):
                package_content = {
                    "name": "dao-hardhat-tests",
                    "version": "1.0.0",
                    "devDependencies": {
                        "@nomicfoundation/hardhat-toolbox": "^4.0.0",
                        "hardhat": "^2.19.0"
                    }
                }
                with open(package_path, 'w') as f:
                    json.dump(package_content, f, indent=2)

            # Link or copy contracts
            project_contracts = config.get_contracts_dir()
            if config.contracts_source_dir:
                self._link_directory(config.contracts_source_dir, project_contracts)

            # Link or copy tests
            project_tests = config.get_tests_dir()
            if config.tests_source_dir:
                self._link_directory(config.tests_source_dir, project_tests)

            return True, errors

        except Exception as e:
            errors.append(f"Setup error: {str(e)}")
            return False, errors

    def _link_directory(self, source: str, target: str):
        """Create symlink or copy directory."""
        # Remove existing
        if os.path.islink(target):
            os.unlink(target)
        elif os.path.exists(target):
            shutil.rmtree(target)

        # Create symlink
        source_abs = os.path.abspath(source)
        if os.path.exists(source_abs):
            os.symlink(source_abs, target)
        else:
            os.makedirs(target, exist_ok=True)

    def install_dependencies(self, config: HardhatConfig) -> Tuple[bool, str]:
        """Install npm dependencies if needed."""
        node_modules = file_utils.concat_folder_filename(config.project_dir, "node_modules")

        if os.path.exists(node_modules):
            return True, "Dependencies already installed"

        try:
            result = subprocess.run(
                ['npm', 'install'],
                cwd=config.project_dir,
                capture_output=True,
                text=True,
                timeout=120
            )

            if result.returncode != 0:
                return False, result.stderr

            return True, result.stdout

        except subprocess.TimeoutExpired:
            return False, "npm install timed out"
        except Exception as e:
            return False, str(e)

    def compile_contracts(self, config: HardhatConfig) -> Tuple[bool, str]:
        """Compile Solidity contracts using Hardhat."""
        try:
            result = subprocess.run(
                ['npx', 'hardhat', 'compile'],
                cwd=config.project_dir,
                capture_output=True,
                text=True,
                timeout=config.timeout_seconds
            )

            output = result.stdout + result.stderr

            if result.returncode != 0:
                return False, output

            return True, output

        except subprocess.TimeoutExpired:
            return False, "Compilation timed out"
        except Exception as e:
            return False, str(e)

    def run_tests(self, config: HardhatConfig) -> HardhatTestResult:
        """Execute Hardhat tests and return structured results."""
        try:
            result = subprocess.run(
                ['npx', 'hardhat', 'test', '--network', config.network],
                cwd=config.project_dir,
                capture_output=True,
                text=True,
                timeout=config.timeout_seconds
            )

            output = result.stdout + result.stderr

            # Parse test results
            passed, total, failed = self._parse_test_output(output)
            duration_ms = self._extract_duration(output)
            gas_used = self._extract_gas_usage(output)

            errors = []
            if result.returncode != 0:
                errors.append(result.stderr if result.stderr else "Tests failed")

            return HardhatTestResult(
                success=result.returncode == 0 and failed == 0,
                passed_tests=passed,
                failed_tests=failed,
                total_tests=total,
                duration_ms=duration_ms,
                gas_used=gas_used,
                output=output,
                errors=errors
            )

        except subprocess.TimeoutExpired:
            return HardhatTestResult(
                success=False,
                output="",
                errors=["Test execution timed out"]
            )
        except Exception as e:
            return HardhatTestResult(
                success=False,
                output="",
                errors=[str(e)]
            )

    def _parse_test_output(self, output: str) -> Tuple[int, int, int]:
        """Parse test counts from Hardhat output."""
        passing_match = re.search(r'(\d+)\s+passing', output)
        failing_match = re.search(r'(\d+)\s+failing', output)

        passed = int(passing_match.group(1)) if passing_match else 0
        failed = int(failing_match.group(1)) if failing_match else 0
        total = passed + failed

        return passed, total, failed

    def _extract_duration(self, output: str) -> int:
        """Extract test duration from output."""
        duration_match = re.search(r'\((\d+)ms\)', output)
        if duration_match:
            return int(duration_match.group(1))

        duration_match = re.search(r'(\d+)\s*ms', output)
        if duration_match:
            return int(duration_match.group(1))

        return 0

    def _extract_gas_usage(self, output: str) -> Optional[int]:
        """Extract gas usage from output if available."""
        gas_match = re.search(r'gas[:\s]+(\d+)', output, re.IGNORECASE)
        if gas_match:
            return int(gas_match.group(1))
        return None

    def get_artifacts(self, config: HardhatConfig) -> Dict:
        """Get compiled contract artifacts."""
        artifacts = {}
        artifacts_dir = file_utils.concat_folder_filename(
            config.get_artifacts_dir(), "contracts"
        )

        if not os.path.exists(artifacts_dir):
            return artifacts

        for root, dirs, files in os.walk(artifacts_dir):
            for file in files:
                if file.endswith('.json') and '.dbg.' not in file:
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r') as f:
                        artifact_data = json.load(f)

                    contract_name = file[:-5]  # Remove .json
                    artifacts[contract_name] = {
                        'abi': artifact_data.get('abi', []),
                        'bytecode': artifact_data.get('bytecode', ''),
                    }

        return artifacts

    def commands_froms_inputs(self, inputs):
        """Not used directly - we override run() instead."""
        return ""

    def run(self, inputs: dict) -> Dict:
        """
        Execute the full Hardhat test pipeline.

        Returns:
            Dictionary with test results and artifacts
        """
        config = self.get_config_from_inputs(inputs)

        result = {
            'setup_success': False,
            'install_success': False,
            'compile_success': False,
            'test_result': None,
            'artifacts': {},
            'errors': []
        }

        # Step 1: Setup project
        self._debug(f"Setting up Hardhat project at {config.project_dir}")
        success, errors = self.setup_hardhat_project(config)
        result['setup_success'] = success
        if not success:
            result['errors'].extend(errors)
            return result

        # Step 2: Install dependencies
        if self.auto_install_deps:
            self._debug("Installing dependencies...")
            success, output = self.install_dependencies(config)
            result['install_success'] = success
            if not success:
                result['errors'].append(f"Install failed: {output}")
                return result
        else:
            result['install_success'] = True

        # Step 3: Compile contracts
        self._debug("Compiling contracts...")
        success, output = self.compile_contracts(config)
        result['compile_success'] = success
        if not success:
            result['errors'].append(f"Compilation failed: {output}")
            return result

        # Step 4: Run tests
        self._debug("Running tests...")
        test_result = self.run_tests(config)
        result['test_result'] = test_result.to_dict()

        # Step 5: Get artifacts
        result['artifacts'] = self.get_artifacts(config)

        return result

    def repr_inner(self):
        return f"""
            {super().repr_inner()}
            "input_key_hardhat_config": {self.input_key_hardhat_config},
            "auto_install_deps": {self.auto_install_deps}
        """
