"""
Service for deploying contracts to blockchain networks.
"""
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from ..models.job import DeploymentResult


class DeploymentService:
    """Service for deploying Solidity contracts to blockchain."""

    def __init__(self, hardhat_project_dir: Path, networks: Dict):
        """
        Initialize deployment service.

        Args:
            hardhat_project_dir: Path to Hardhat project
            networks: Network configuration dictionary
        """
        self.hardhat_project_dir = hardhat_project_dir
        self.networks = networks

    def deploy(
        self,
        network: str,
        contract_names: List[str],
        deployer_private_key: Optional[str] = None
    ) -> DeploymentResult:
        """
        Deploy contracts to specified network.

        Args:
            network: Network name (localhost, sepolia, etc.)
            contract_names: List of contract names to deploy
            deployer_private_key: Private key for deployment

        Returns:
            DeploymentResult with addresses and transaction info
        """
        if network not in self.networks:
            return DeploymentResult(
                success=False,
                network=network,
                errors=[f"Unknown network: {network}"]
            )

        try:
            # Create deployment script
            script_path = self._create_deployment_script(contract_names)

            # Set up environment
            env = dict()
            if deployer_private_key:
                env['DEPLOYER_PRIVATE_KEY'] = deployer_private_key

            # Update hardhat config with network settings
            self._update_hardhat_config(network, deployer_private_key)

            # Run deployment
            result = subprocess.run(
                ['npx', 'hardhat', 'run', str(script_path), '--network', network],
                cwd=str(self.hardhat_project_dir),
                capture_output=True,
                text=True,
                timeout=300,
                env={**dict(__import__('os').environ), **env}
            )

            if result.returncode != 0:
                return DeploymentResult(
                    success=False,
                    network=network,
                    errors=[result.stderr if result.stderr else "Deployment failed"],
                )

            # Parse deployment output
            contracts, tx_hash, block_number, gas_used = self._parse_deployment_output(
                result.stdout
            )

            return DeploymentResult(
                success=True,
                network=network,
                transaction_hash=tx_hash,
                block_number=block_number,
                gas_used=gas_used,
                contracts=contracts,
            )

        except subprocess.TimeoutExpired:
            return DeploymentResult(
                success=False,
                network=network,
                errors=["Deployment timed out"]
            )
        except Exception as e:
            return DeploymentResult(
                success=False,
                network=network,
                errors=[str(e)]
            )

    def _create_deployment_script(self, contract_names: List[str]) -> Path:
        """Create Hardhat deployment script."""
        scripts_dir = self.hardhat_project_dir / 'scripts'
        scripts_dir.mkdir(exist_ok=True)

        script_path = scripts_dir / 'deploy.js'

        # Generate deployment script
        deployments = []
        for name in contract_names:
            deployments.append(f'''
    // Deploy {name}
    const {name}Factory = await ethers.getContractFactory("{name}");
    const {name.lower()} = await {name}Factory.deploy();
    await {name.lower()}.waitForDeployment();
    const {name.lower()}Address = await {name.lower()}.getAddress();
    console.log("DEPLOYED:{name}:" + {name.lower()}Address);
    deployed["{name}"] = {name.lower()}Address;
''')

        script_content = f'''const {{ ethers }} = require("hardhat");

async function main() {{
    const [deployer] = await ethers.getSigners();
    console.log("Deploying contracts with account:", deployer.address);

    const balance = await ethers.provider.getBalance(deployer.address);
    console.log("Account balance:", ethers.formatEther(balance));

    const deployed = {{}};

    {"".join(deployments)}

    console.log("DEPLOYMENT_COMPLETE");
    console.log("DEPLOYED_CONTRACTS:" + JSON.stringify(deployed));
}}

main()
    .then(() => process.exit(0))
    .catch((error) => {{
        console.error(error);
        process.exit(1);
    }});
'''

        with open(script_path, 'w') as f:
            f.write(script_content)

        return script_path

    def _update_hardhat_config(self, network: str, private_key: Optional[str]):
        """Update Hardhat config with network and key settings."""
        config_path = self.hardhat_project_dir / 'hardhat.config.js'

        network_config = self.networks.get(network, {})
        url = network_config.get('url', 'http://127.0.0.1:8545')
        chain_id = network_config.get('chain_id', 31337)

        accounts_config = ""
        if private_key and network != 'localhost' and network != 'hardhat':
            accounts_config = f'accounts: [process.env.DEPLOYER_PRIVATE_KEY || "{private_key}"],'

        config_content = f'''require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {{
  solidity: {{
    version: "0.8.20",
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
    }},
    {network}: {{
      url: "{url}",
      chainId: {chain_id},
      {accounts_config}
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

    def _parse_deployment_output(
        self,
        output: str
    ) -> Tuple[Dict[str, str], Optional[str], Optional[int], Optional[int]]:
        """Parse deployment script output."""
        contracts = {}
        tx_hash = None
        block_number = None
        gas_used = None

        import re

        # Parse deployed contracts
        for match in re.finditer(r'DEPLOYED:(\w+):(\w+)', output):
            contract_name = match.group(1)
            address = match.group(2)
            contracts[contract_name] = address

        # Try to parse JSON output
        json_match = re.search(r'DEPLOYED_CONTRACTS:(.+)', output)
        if json_match:
            try:
                contracts = json.loads(json_match.group(1))
            except json.JSONDecodeError:
                pass

        # Parse transaction hash if available
        tx_match = re.search(r'transaction[:\s]+(\w+)', output, re.IGNORECASE)
        if tx_match:
            tx_hash = tx_match.group(1)

        return contracts, tx_hash, block_number, gas_used

    def generate_frontend_manifest(
        self,
        deployment_result: DeploymentResult,
        artifacts: Dict
    ) -> Dict:
        """
        Generate frontend integration manifest.

        Args:
            deployment_result: Deployment result with addresses
            artifacts: Contract artifacts with ABIs

        Returns:
            Frontend manifest dictionary
        """
        manifest = {
            'network': deployment_result.network,
            'chainId': self.networks.get(deployment_result.network, {}).get('chain_id'),
            'deployedAt': None,  # Could add timestamp
            'contracts': {}
        }

        for contract_name, address in deployment_result.contracts.items():
            artifact = artifacts.get(contract_name, {})
            manifest['contracts'][contract_name] = {
                'address': address,
                'abi': artifact.get('abi', []),
            }

        return manifest

    def save_deployment_artifacts(
        self,
        output_dir: Path,
        deployment_result: DeploymentResult,
        artifacts: Dict
    ):
        """
        Save deployment artifacts to output directory.

        Args:
            output_dir: Output directory path
            deployment_result: Deployment result
            artifacts: Contract artifacts
        """
        deployments_dir = output_dir / 'deployments' / deployment_result.network
        deployments_dir.mkdir(parents=True, exist_ok=True)

        # Save each contract's deployment info
        for contract_name, address in deployment_result.contracts.items():
            artifact = artifacts.get(contract_name, {})
            deployment_info = {
                'address': address,
                'abi': artifact.get('abi', []),
                'bytecode': artifact.get('bytecode', ''),
                'network': deployment_result.network,
                'transactionHash': deployment_result.transaction_hash,
                'blockNumber': deployment_result.block_number,
            }

            deployment_file = deployments_dir / f'{contract_name}.json'
            with open(deployment_file, 'w') as f:
                json.dump(deployment_info, f, indent=2)

        # Save manifest
        manifest = self.generate_frontend_manifest(deployment_result, artifacts)
        manifest_file = output_dir / 'deployment-manifest.json'
        with open(manifest_file, 'w') as f:
            json.dump(manifest, f, indent=2)
