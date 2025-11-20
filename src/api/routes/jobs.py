"""
Job management API routes.
"""
from flask import Blueprint, request, jsonify, current_app, send_file
from pathlib import Path
import os

jobs_bp = Blueprint('jobs', __name__, url_prefix='/api/v1/jobs')


@jobs_bp.route('', methods=['POST'])
def create_job():
    """
    Create a new deployment job.

    Accepts XML content via:
    - multipart/form-data with 'file' field
    - JSON body with 'xml_content' field

    Optional config fields:
    - network: Target network (default: localhost)
    - run_tests: Whether to run tests (default: true)
    - deploy: Whether to deploy after tests pass (default: false)
    - deployer_private_key: Private key for deployment
    """
    job_service = current_app.config['job_service']

    # Get XML content
    xml_content = None
    config = {}

    if request.content_type and 'multipart/form-data' in request.content_type:
        # File upload
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        xml_content = file.read().decode('utf-8')

        # Get config from form data
        config = {
            'network': request.form.get('network', 'localhost'),
            'run_tests': request.form.get('run_tests', 'true').lower() == 'true',
            'deploy': request.form.get('deploy', 'false').lower() == 'true',
            'deployer_private_key': request.form.get('deployer_private_key', ''),
        }
    else:
        # JSON body
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        xml_content = data.get('xml_content')
        if not xml_content:
            return jsonify({'error': 'xml_content is required'}), 400

        config = {
            'network': data.get('network', 'localhost'),
            'run_tests': data.get('run_tests', True),
            'deploy': data.get('deploy', False),
            'deployer_private_key': data.get('deployer_private_key', ''),
        }

    # Create job
    job = job_service.create_job(xml_content, config)

    # Execute asynchronously
    job_service.execute_job_async(job.id)

    return jsonify({
        'job_id': job.id,
        'status': job.status.value,
        'message': 'Job created and queued for processing',
    }), 202


@jobs_bp.route('', methods=['GET'])
def list_jobs():
    """List all jobs."""
    job_service = current_app.config['job_service']
    limit = request.args.get('limit', 100, type=int)

    jobs = job_service.list_jobs(limit)

    return jsonify({
        'jobs': [job.to_dict() for job in jobs],
        'total': len(jobs),
    })


@jobs_bp.route('/<job_id>', methods=['GET'])
def get_job(job_id):
    """Get job status and details."""
    job_service = current_app.config['job_service']

    job = job_service.get_job(job_id)
    if not job:
        return jsonify({'error': 'Job not found'}), 404

    return jsonify(job.to_dict())


@jobs_bp.route('/<job_id>/cancel', methods=['POST'])
def cancel_job(job_id):
    """Cancel a running job."""
    job_service = current_app.config['job_service']

    success = job_service.cancel_job(job_id)
    if not success:
        return jsonify({'error': 'Cannot cancel job'}), 400

    return jsonify({'message': 'Job cancelled'})


@jobs_bp.route('/<job_id>/contracts', methods=['GET'])
def get_job_contracts(job_id):
    """Get generated contract files for a job."""
    job_service = current_app.config['job_service']

    job = job_service.get_job(job_id)
    if not job:
        return jsonify({'error': 'Job not found'}), 404

    if not job.generated_contracts:
        return jsonify({'error': 'No contracts generated yet'}), 404

    contracts = {}
    for contract_path in job.generated_contracts:
        path = Path(contract_path)
        if path.exists():
            with open(path, 'r') as f:
                contracts[path.name] = f.read()

    return jsonify({'contracts': contracts})


@jobs_bp.route('/<job_id>/tests', methods=['GET'])
def get_job_tests(job_id):
    """Get generated test files for a job."""
    job_service = current_app.config['job_service']

    job = job_service.get_job(job_id)
    if not job:
        return jsonify({'error': 'Job not found'}), 404

    if not job.generated_tests:
        return jsonify({'error': 'No tests generated yet'}), 404

    tests = {}
    for test_path in job.generated_tests:
        path = Path(test_path)
        if path.exists():
            with open(path, 'r') as f:
                tests[path.name] = f.read()

    return jsonify({'tests': tests})


@jobs_bp.route('/<job_id>/artifacts', methods=['GET'])
def get_job_artifacts(job_id):
    """Get compiled contract artifacts (ABI, bytecode)."""
    job_service = current_app.config['job_service']

    job = job_service.get_job(job_id)
    if not job:
        return jsonify({'error': 'Job not found'}), 404

    artifacts = job_service.get_job_artifacts(job_id)
    if not artifacts:
        return jsonify({'error': 'Artifacts not available'}), 404

    return jsonify({'artifacts': artifacts})


@jobs_bp.route('/<job_id>/manifest', methods=['GET'])
def get_job_manifest(job_id):
    """Get frontend deployment manifest."""
    job_service = current_app.config['job_service']

    job = job_service.get_job(job_id)
    if not job:
        return jsonify({'error': 'Job not found'}), 404

    if not job.frontend_manifest:
        return jsonify({'error': 'Manifest not available'}), 404

    return jsonify(job.frontend_manifest)


@jobs_bp.route('/<job_id>/download', methods=['GET'])
def download_job_output(job_id):
    """Download all job outputs as a ZIP file."""
    job_service = current_app.config['job_service']

    job = job_service.get_job(job_id)
    if not job:
        return jsonify({'error': 'Job not found'}), 404

    if not job.output_dir or not Path(job.output_dir).exists():
        return jsonify({'error': 'Output not available'}), 404

    # Create ZIP file
    import shutil
    output_dir = Path(job.output_dir)
    zip_path = output_dir.parent / f'{job_id}.zip'

    shutil.make_archive(
        str(zip_path.with_suffix('')),
        'zip',
        str(output_dir)
    )

    return send_file(
        str(zip_path),
        as_attachment=True,
        download_name=f'dao-deployment-{job_id}.zip'
    )
