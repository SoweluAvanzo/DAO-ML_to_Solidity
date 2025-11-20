"""
Job model for tracking deployment pipeline status.
"""
import json
import uuid
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional, Dict, Any, List
from dataclasses import dataclass, field, asdict


class JobStatus(str, Enum):
    """Job status enumeration."""
    QUEUED = "queued"
    VALIDATING = "validating"
    GENERATING = "generating"
    TESTING = "testing"
    DEPLOYING = "deploying"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class JobPhase(str, Enum):
    """Job phases for detailed tracking."""
    INPUT_VALIDATION = "input_validation"
    CONTRACT_GENERATION = "contract_generation"
    TEST_GENERATION = "test_generation"
    TEST_EXECUTION = "test_execution"
    COMPILATION = "compilation"
    DEPLOYMENT = "deployment"
    FRONTEND_GENERATION = "frontend_generation"


@dataclass
class TestResult:
    """Test execution result."""
    passed: bool
    total_tests: int
    passed_tests: int
    failed_tests: int
    duration_ms: int
    gas_used: Optional[int] = None
    output: str = ""
    errors: List[str] = field(default_factory=list)


@dataclass
class DeploymentResult:
    """Deployment result with contract addresses."""
    success: bool
    network: str
    transaction_hash: Optional[str] = None
    block_number: Optional[int] = None
    gas_used: Optional[int] = None
    contracts: Dict[str, str] = field(default_factory=dict)  # name -> address
    errors: List[str] = field(default_factory=list)


@dataclass
class Job:
    """Deployment job model."""
    id: str
    status: JobStatus
    created_at: datetime
    updated_at: datetime

    # Input data
    xml_content: str = ""
    config: Dict[str, Any] = field(default_factory=dict)

    # Progress tracking
    current_phase: Optional[JobPhase] = None
    progress_percent: int = 0
    message: str = ""

    # Results
    validation_errors: List[str] = field(default_factory=list)
    generated_contracts: List[str] = field(default_factory=list)
    generated_tests: List[str] = field(default_factory=list)
    test_result: Optional[TestResult] = None
    deployment_result: Optional[DeploymentResult] = None

    # Output paths
    output_dir: Optional[str] = None
    contracts_dir: Optional[str] = None
    tests_dir: Optional[str] = None

    # Frontend manifest
    frontend_manifest: Optional[Dict[str, Any]] = None

    @classmethod
    def create(cls, xml_content: str, config: Optional[Dict[str, Any]] = None) -> 'Job':
        """Create a new job."""
        now = datetime.utcnow()
        return cls(
            id=str(uuid.uuid4()),
            status=JobStatus.QUEUED,
            created_at=now,
            updated_at=now,
            xml_content=xml_content,
            config=config or {},
        )

    def update_status(self, status: JobStatus, message: str = ""):
        """Update job status."""
        self.status = status
        self.message = message
        self.updated_at = datetime.utcnow()

    def update_phase(self, phase: JobPhase, progress: int, message: str = ""):
        """Update current phase and progress."""
        self.current_phase = phase
        self.progress_percent = progress
        self.message = message
        self.updated_at = datetime.utcnow()

    def fail(self, message: str, errors: Optional[List[str]] = None):
        """Mark job as failed."""
        self.status = JobStatus.FAILED
        self.message = message
        if errors:
            self.validation_errors.extend(errors)
        self.updated_at = datetime.utcnow()

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        result = {
            'id': self.id,
            'status': self.status.value,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'current_phase': self.current_phase.value if self.current_phase else None,
            'progress_percent': self.progress_percent,
            'message': self.message,
            'validation_errors': self.validation_errors,
            'generated_contracts': self.generated_contracts,
            'generated_tests': self.generated_tests,
            'config': self.config,
        }

        if self.test_result:
            result['test_result'] = asdict(self.test_result)

        if self.deployment_result:
            result['deployment_result'] = asdict(self.deployment_result)

        if self.frontend_manifest:
            result['frontend_manifest'] = self.frontend_manifest

        return result

    def save(self, jobs_dir: Path):
        """Save job to file system."""
        job_file = jobs_dir / f"{self.id}.json"
        jobs_dir.mkdir(parents=True, exist_ok=True)

        data = self.to_dict()
        data['xml_content'] = self.xml_content
        data['output_dir'] = self.output_dir
        data['contracts_dir'] = self.contracts_dir
        data['tests_dir'] = self.tests_dir

        with open(job_file, 'w') as f:
            json.dump(data, f, indent=2, default=str)

    @classmethod
    def load(cls, job_id: str, jobs_dir: Path) -> Optional['Job']:
        """Load job from file system."""
        job_file = jobs_dir / f"{job_id}.json"
        if not job_file.exists():
            return None

        with open(job_file, 'r') as f:
            data = json.load(f)

        job = cls(
            id=data['id'],
            status=JobStatus(data['status']),
            created_at=datetime.fromisoformat(data['created_at']),
            updated_at=datetime.fromisoformat(data['updated_at']),
            xml_content=data.get('xml_content', ''),
            config=data.get('config', {}),
            current_phase=JobPhase(data['current_phase']) if data.get('current_phase') else None,
            progress_percent=data.get('progress_percent', 0),
            message=data.get('message', ''),
            validation_errors=data.get('validation_errors', []),
            generated_contracts=data.get('generated_contracts', []),
            generated_tests=data.get('generated_tests', []),
            output_dir=data.get('output_dir'),
            contracts_dir=data.get('contracts_dir'),
            tests_dir=data.get('tests_dir'),
            frontend_manifest=data.get('frontend_manifest'),
        )

        if data.get('test_result'):
            job.test_result = TestResult(**data['test_result'])

        if data.get('deployment_result'):
            job.deployment_result = DeploymentResult(**data['deployment_result'])

        return job
