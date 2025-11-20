"""
Health check and system status routes.
"""
from flask import Blueprint, jsonify, current_app
import subprocess
import shutil

health_bp = Blueprint('health', __name__, url_prefix='/api/v1')


@health_bp.route('/health', methods=['GET'])
def health_check():
    """Basic health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'dao-deployment-platform',
    })


@health_bp.route('/status', methods=['GET'])
def system_status():
    """
    Detailed system status including dependencies.
    """
    status = {
        'status': 'healthy',
        'dependencies': {},
        'config': {}
    }

    # Check Node.js
    try:
        result = subprocess.run(
            ['node', '--version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        status['dependencies']['node'] = {
            'available': result.returncode == 0,
            'version': result.stdout.strip() if result.returncode == 0 else None
        }
    except Exception:
        status['dependencies']['node'] = {'available': False, 'version': None}

    # Check npm
    try:
        result = subprocess.run(
            ['npm', '--version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        status['dependencies']['npm'] = {
            'available': result.returncode == 0,
            'version': result.stdout.strip() if result.returncode == 0 else None
        }
    except Exception:
        status['dependencies']['npm'] = {'available': False, 'version': None}

    # Check npx/hardhat
    try:
        result = subprocess.run(
            ['npx', 'hardhat', '--version'],
            capture_output=True,
            text=True,
            timeout=10
        )
        status['dependencies']['hardhat'] = {
            'available': result.returncode == 0,
            'version': result.stdout.strip() if result.returncode == 0 else None
        }
    except Exception:
        status['dependencies']['hardhat'] = {'available': False, 'version': None}

    # Configuration info
    config = current_app.config
    status['config'] = {
        'templates_dir_exists': config.get('TEMPLATES_DIR', '').exists() if hasattr(config.get('TEMPLATES_DIR', ''), 'exists') else False,
        'max_concurrent_jobs': config.get('MAX_CONCURRENT_JOBS', 5),
        'default_network': config.get('DEFAULT_NETWORK', 'localhost'),
        'available_networks': list(config.get('NETWORKS', {}).keys()),
    }

    # Overall status
    all_deps_ok = all(
        dep.get('available', False)
        for dep in status['dependencies'].values()
    )
    status['status'] = 'healthy' if all_deps_ok else 'degraded'

    return jsonify(status)


@health_bp.route('/networks', methods=['GET'])
def list_networks():
    """List available blockchain networks."""
    config = current_app.config
    networks = config.get('NETWORKS', {})

    return jsonify({
        'default': config.get('DEFAULT_NETWORK', 'localhost'),
        'networks': {
            name: {
                'chain_id': net_config.get('chain_id'),
                'url': net_config.get('url', '').split('@')[-1] if net_config.get('url') else None,  # Hide auth info
            }
            for name, net_config in networks.items()
        }
    })
