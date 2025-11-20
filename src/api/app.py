"""
Flask application factory for DAO Deployment Platform API.
"""
import logging
from flask import Flask, jsonify
from flask_cors import CORS

from .config import get_config
from .routes import jobs_bp, translate_bp, health_bp
from .services import JobService


def create_app(config=None):
    """
    Create and configure the Flask application.

    Args:
        config: Optional configuration object or dictionary

    Returns:
        Configured Flask application
    """
    app = Flask(__name__)

    # Load configuration
    if config is None:
        config = get_config()

    if isinstance(config, dict):
        app.config.update(config)
    else:
        app.config.from_object(config)

    # Ensure paths exist
    for path_key in ['OUTPUT_DIR', 'JOBS_DIR', 'HARDHAT_PROJECT_DIR']:
        path = app.config.get(path_key)
        if path:
            path.mkdir(parents=True, exist_ok=True)

    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG if app.config.get('DEBUG') else logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)

    # Enable CORS
    CORS(app, origins=app.config.get('CORS_ORIGINS', ['localhost:3000']))

    # Initialize services
    job_service = JobService(
        jobs_dir=app.config['JOBS_DIR'],
        output_dir=app.config['OUTPUT_DIR'],
        templates_dir=app.config['TEMPLATES_DIR'],
        hardhat_project_dir=app.config['HARDHAT_PROJECT_DIR'],
        networks=app.config['NETWORKS'],
        max_workers=app.config.get('MAX_CONCURRENT_JOBS', 5)
    )
    app.config['job_service'] = job_service

    # Register blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(jobs_bp)
    app.register_blueprint(translate_bp)

    # Error handlers
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({'error': 'Bad request', 'message': str(error)}), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found', 'message': str(error)}), 404

    @app.errorhandler(500)
    def internal_error(error):
        logger.error(f"Internal error: {error}")
        return jsonify({'error': 'Internal server error'}), 500

    # Shutdown handler
    @app.teardown_appcontext
    def shutdown_services(exception=None):
        job_service = app.config.get('job_service')
        if job_service:
            job_service.shutdown()

    # Root route
    @app.route('/')
    def index():
        return jsonify({
            'service': 'DAO Deployment Platform API',
            'version': app.config.get('API_VERSION', 'v1'),
            'endpoints': {
                'health': '/api/v1/health',
                'status': '/api/v1/status',
                'networks': '/api/v1/networks',
                'jobs': '/api/v1/jobs',
                'translate': '/api/v1/translate',
            }
        })

    logger.info("DAO Deployment Platform API initialized")
    return app


def run_development_server():
    """Run the development server."""
    app = create_app()
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )


if __name__ == '__main__':
    run_development_server()
