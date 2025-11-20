"""
Service for managing deployment jobs.
"""
import threading
from pathlib import Path
from typing import Dict, List, Optional
from concurrent.futures import ThreadPoolExecutor

from ..models.job import Job, JobStatus, JobPhase
from .translator_service import TranslatorService
from .test_runner_service import TestRunnerService
from .deployment_service import DeploymentService


class JobService:
    """Service for managing and executing deployment jobs."""

    def __init__(
        self,
        jobs_dir: Path,
        output_dir: Path,
        templates_dir: Path,
        hardhat_project_dir: Path,
        networks: Dict,
        max_workers: int = 5
    ):
        """
        Initialize job service.

        Args:
            jobs_dir: Directory for job storage
            output_dir: Base output directory
            templates_dir: Templates directory
            hardhat_project_dir: Hardhat project directory
            networks: Network configurations
            max_workers: Maximum concurrent jobs
        """
        self.jobs_dir = jobs_dir
        self.output_dir = output_dir
        self.templates_dir = templates_dir
        self.hardhat_project_dir = hardhat_project_dir
        self.networks = networks

        self.jobs_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Services
        self.translator_service = TranslatorService(templates_dir, output_dir)
        self.test_runner_service = TestRunnerService(hardhat_project_dir)
        self.deployment_service = DeploymentService(hardhat_project_dir, networks)

        # Job execution
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self._jobs_cache: Dict[str, Job] = {}
        self._lock = threading.Lock()

    def create_job(self, xml_content: str, config: Optional[Dict] = None) -> Job:
        """
        Create a new deployment job.

        Args:
            xml_content: DAO-ML XML content
            config: Job configuration

        Returns:
            Created job
        """
        job = Job.create(xml_content, config or {})

        # Set up job directories
        job_output_dir = self.output_dir / job.id
        job.output_dir = str(job_output_dir)
        job.contracts_dir = str(job_output_dir / 'contracts')
        job.tests_dir = str(job_output_dir / 'test')

        # Save job
        with self._lock:
            self._jobs_cache[job.id] = job
        job.save(self.jobs_dir)

        return job

    def get_job(self, job_id: str) -> Optional[Job]:
        """Get job by ID."""
        with self._lock:
            if job_id in self._jobs_cache:
                return self._jobs_cache[job_id]

        # Load from disk
        job = Job.load(job_id, self.jobs_dir)
        if job:
            with self._lock:
                self._jobs_cache[job_id] = job
        return job

    def list_jobs(self, limit: int = 100) -> List[Job]:
        """List recent jobs."""
        jobs = []
        for job_file in sorted(self.jobs_dir.glob('*.json'), reverse=True)[:limit]:
            job_id = job_file.stem
            job = self.get_job(job_id)
            if job:
                jobs.append(job)
        return jobs

    def cancel_job(self, job_id: str) -> bool:
        """Cancel a job if it's still running."""
        job = self.get_job(job_id)
        if not job:
            return False

        if job.status in [JobStatus.QUEUED, JobStatus.VALIDATING, JobStatus.GENERATING]:
            job.update_status(JobStatus.CANCELLED, "Job cancelled by user")
            job.save(self.jobs_dir)
            return True

        return False

    def execute_job_async(self, job_id: str) -> None:
        """Execute job asynchronously."""
        self.executor.submit(self._execute_job, job_id)

    def _execute_job(self, job_id: str) -> None:
        """
        Execute the full deployment pipeline for a job.

        Phases:
        1. Input validation
        2. Contract generation
        3. Test generation
        4. Test execution
        5. Deployment (if requested)
        6. Frontend manifest generation
        """
        job = self.get_job(job_id)
        if not job:
            return

        config = job.config
        network = config.get('network', 'localhost')
        run_tests = config.get('run_tests', True)
        deploy = config.get('deploy', False)
        deployer_key = config.get('deployer_private_key', '')

        try:
            # Phase 1: Validation
            job.update_phase(JobPhase.INPUT_VALIDATION, 10, "Validating XML input...")
            job.update_status(JobStatus.VALIDATING)
            job.save(self.jobs_dir)

            is_valid, errors, _ = self.translator_service.validate_xml(job.xml_content)
            if not is_valid:
                job.fail("XML validation failed", errors)
                job.save(self.jobs_dir)
                return

            # Phase 2: Contract Generation
            job.update_phase(JobPhase.CONTRACT_GENERATION, 30, "Generating Solidity contracts...")
            job.update_status(JobStatus.GENERATING)
            job.save(self.jobs_dir)

            output_dir = Path(job.output_dir)
            success, errors, contract_files, test_files = self.translator_service.translate_to_solidity(
                job.xml_content,
                output_dir,
                generate_tests=run_tests
            )

            if not success:
                job.fail("Contract generation failed", errors)
                job.save(self.jobs_dir)
                return

            job.generated_contracts = [str(f) for f in contract_files]
            job.generated_tests = [str(f) for f in test_files]

            # Phase 3: Test Execution (if requested)
            if run_tests and test_files:
                job.update_phase(JobPhase.TEST_EXECUTION, 50, "Running Hardhat test pipeline...")
                job.update_status(JobStatus.TESTING)
                job.save(self.jobs_dir)

                # Run full test pipeline using HardhatTestRunner
                contracts_dir = Path(job.contracts_dir)
                tests_dir = Path(job.tests_dir)

                success, test_result, artifacts = self.test_runner_service.run_full_test_pipeline(
                    contracts_dir, tests_dir, network
                )

                job.test_result = test_result

                if not success:
                    error_msg = f"Tests failed: {test_result.failed_tests} failures" if test_result.failed_tests > 0 else "Test pipeline failed"
                    job.fail(error_msg, test_result.errors)
                    job.save(self.jobs_dir)
                    return

                job.update_phase(JobPhase.TEST_EXECUTION, 75, f"Tests passed: {test_result.passed_tests}/{test_result.total_tests}")
                job.save(self.jobs_dir)

            # Phase 4: Deployment (if requested and tests passed)
            if deploy:
                job.update_phase(JobPhase.DEPLOYMENT, 80, f"Deploying to {network}...")
                job.update_status(JobStatus.DEPLOYING)
                job.save(self.jobs_dir)

                # Get contract names from generated files
                contract_names = []
                for contract_file in job.generated_contracts:
                    # Extract contract name from file path
                    name = Path(contract_file).stem
                    if not name.startswith('I') and 'interface' not in name.lower():
                        contract_names.append(name)

                deployment_result = self.deployment_service.deploy(
                    network,
                    contract_names,
                    deployer_key
                )

                job.deployment_result = deployment_result

                if not deployment_result.success:
                    job.fail("Deployment failed", deployment_result.errors)
                    job.save(self.jobs_dir)
                    return

                # Generate frontend manifest
                job.update_phase(JobPhase.FRONTEND_GENERATION, 95, "Generating frontend manifest...")
                job.save(self.jobs_dir)

                artifacts = self.test_runner_service.get_artifacts()
                manifest = self.deployment_service.generate_frontend_manifest(
                    deployment_result, artifacts
                )
                job.frontend_manifest = manifest

                # Save deployment artifacts
                self.deployment_service.save_deployment_artifacts(
                    output_dir, deployment_result, artifacts
                )

            # Complete
            job.update_phase(None, 100, "Job completed successfully")
            job.update_status(JobStatus.COMPLETED)
            job.save(self.jobs_dir)

        except Exception as e:
            import traceback
            job.fail(f"Unexpected error: {str(e)}", [traceback.format_exc()])
            job.save(self.jobs_dir)

    def get_job_artifacts(self, job_id: str) -> Optional[Dict]:
        """Get contract artifacts for a job."""
        job = self.get_job(job_id)
        if not job or job.status != JobStatus.COMPLETED:
            return None

        return self.test_runner_service.get_artifacts()

    def shutdown(self):
        """Shutdown the executor."""
        self.executor.shutdown(wait=True)
