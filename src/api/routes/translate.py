"""
Translation API routes for synchronous operations.
"""
from flask import Blueprint, request, jsonify, current_app
from pathlib import Path
import tempfile

translate_bp = Blueprint('translate', __name__, url_prefix='/api/v1/translate')


@translate_bp.route('/validate', methods=['POST'])
def validate_xml():
    """
    Validate DAO-ML XML without generating contracts.

    Returns validation result with any errors.
    """
    job_service = current_app.config['job_service']
    translator_service = job_service.translator_service

    # Get XML content
    xml_content = None
    if request.content_type and 'multipart/form-data' in request.content_type:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        file = request.files['file']
        xml_content = file.read().decode('utf-8')
    else:
        data = request.get_json()
        if not data or 'xml_content' not in data:
            return jsonify({'error': 'xml_content is required'}), 400
        xml_content = data['xml_content']

    # Validate
    is_valid, errors, _ = translator_service.validate_xml(xml_content)

    return jsonify({
        'valid': is_valid,
        'errors': errors,
    })


@translate_bp.route('/model', methods=['POST'])
def generate_model():
    """
    Generate internal model from XML and return as JSON.

    Useful for debugging and model inspection.
    """
    job_service = current_app.config['job_service']
    translator_service = job_service.translator_service

    # Get XML content
    xml_content = None
    if request.content_type and 'multipart/form-data' in request.content_type:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        file = request.files['file']
        xml_content = file.read().decode('utf-8')
    else:
        data = request.get_json()
        if not data or 'xml_content' not in data:
            return jsonify({'error': 'xml_content is required'}), 400
        xml_content = data['xml_content']

    # Generate model
    success, errors, json_string = translator_service.generate_model_json(xml_content)

    if not success:
        return jsonify({
            'error': 'Model generation failed',
            'errors': errors,
        }), 400

    import json
    return jsonify({
        'model': json.loads(json_string) if json_string else {},
    })


@translate_bp.route('/contracts', methods=['POST'])
def generate_contracts():
    """
    Generate Solidity contracts synchronously.

    Returns generated contract source code directly.
    For large DAOs or when you need test execution, use the async jobs API instead.
    """
    job_service = current_app.config['job_service']
    translator_service = job_service.translator_service

    # Get XML content
    xml_content = None
    generate_tests = True

    if request.content_type and 'multipart/form-data' in request.content_type:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        file = request.files['file']
        xml_content = file.read().decode('utf-8')
        generate_tests = request.form.get('generate_tests', 'true').lower() == 'true'
    else:
        data = request.get_json()
        if not data or 'xml_content' not in data:
            return jsonify({'error': 'xml_content is required'}), 400
        xml_content = data['xml_content']
        generate_tests = data.get('generate_tests', True)

    # Create temporary output directory
    with tempfile.TemporaryDirectory() as temp_dir:
        output_dir = Path(temp_dir)

        # Generate contracts
        success, errors, contract_files, test_files = translator_service.translate_to_solidity(
            xml_content,
            output_dir,
            generate_tests=generate_tests
        )

        if not success:
            return jsonify({
                'error': 'Contract generation failed',
                'errors': errors,
            }), 400

        # Read generated files
        contracts = {}
        for contract_path in contract_files:
            path = Path(contract_path)
            if path.exists():
                with open(path, 'r') as f:
                    contracts[path.name] = f.read()

        tests = {}
        for test_path in test_files:
            path = Path(test_path)
            if path.exists():
                with open(path, 'r') as f:
                    tests[path.name] = f.read()

        return jsonify({
            'contracts': contracts,
            'tests': tests,
            'contract_count': len(contracts),
            'test_count': len(tests),
        })


@translate_bp.route('/generate-and-test', methods=['POST'])
def generate_and_test():
    """
    Generate Solidity contracts and run Hardhat tests synchronously.

    This endpoint combines contract generation with test execution.
    Returns generated contracts, test results, and compiled artifacts.
    """
    job_service = current_app.config['job_service']
    translator_service = job_service.translator_service
    test_runner_service = job_service.test_runner_service

    # Get XML content
    xml_content = None
    network = 'hardhat'

    if request.content_type and 'multipart/form-data' in request.content_type:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        file = request.files['file']
        xml_content = file.read().decode('utf-8')
        network = request.form.get('network', 'hardhat')
    else:
        data = request.get_json()
        if not data or 'xml_content' not in data:
            return jsonify({'error': 'xml_content is required'}), 400
        xml_content = data['xml_content']
        network = data.get('network', 'hardhat')

    # Create output directory
    import uuid
    output_id = str(uuid.uuid4())[:8]
    output_dir = job_service.output_dir / f'generate_test_{output_id}'
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        # Step 1: Generate contracts and tests
        success, errors, contract_files, test_files = translator_service.translate_to_solidity(
            xml_content,
            output_dir,
            generate_tests=True
        )

        if not success:
            return jsonify({
                'error': 'Contract generation failed',
                'errors': errors,
                'phase': 'generation'
            }), 400

        # Read generated contracts
        contracts = {}
        for contract_path in contract_files:
            path = Path(contract_path)
            if path.exists():
                with open(path, 'r') as f:
                    contracts[path.name] = f.read()

        # Read generated tests
        tests = {}
        for test_path in test_files:
            path = Path(test_path)
            if path.exists():
                with open(path, 'r') as f:
                    tests[path.name] = f.read()

        # Step 2: Run tests if we have test files
        if not test_files:
            return jsonify({
                'success': True,
                'contracts': contracts,
                'tests': tests,
                'test_result': None,
                'message': 'Contracts generated but no tests to run',
                'output_dir': str(output_dir)
            })

        # Run full test pipeline
        contracts_dir = output_dir / 'contracts'
        tests_dir = output_dir / 'test'

        test_success, test_result, artifacts = test_runner_service.run_full_test_pipeline(
            contracts_dir, tests_dir, network
        )

        # Prepare response
        response = {
            'success': test_success,
            'contracts': contracts,
            'tests': tests,
            'test_result': {
                'passed': test_result.passed,
                'total_tests': test_result.total_tests,
                'passed_tests': test_result.passed_tests,
                'failed_tests': test_result.failed_tests,
                'duration_ms': test_result.duration_ms,
                'gas_used': test_result.gas_used,
                'output': test_result.output,
                'errors': test_result.errors
            },
            'artifacts': {
                name: {
                    'abi': data.get('abi', []),
                    'has_bytecode': bool(data.get('bytecode'))
                }
                for name, data in artifacts.items()
            },
            'output_dir': str(output_dir)
        }

        if not test_success:
            response['error'] = f'Tests failed: {test_result.failed_tests} failures'

        return jsonify(response), 200 if test_success else 400

    except Exception as e:
        import traceback
        return jsonify({
            'error': f'Unexpected error: {str(e)}',
            'traceback': traceback.format_exc(),
            'phase': 'unknown'
        }), 500
