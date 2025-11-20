#!/usr/bin/env python3
"""
Runner script for the DAO Deployment Platform API.

Usage:
    python run_api.py                    # Development server
    python run_api.py --production       # Production mode (use with gunicorn)
    python run_api.py --host 0.0.0.0     # Custom host
    python run_api.py --port 8080        # Custom port
"""
import argparse
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.api.app import create_app


def main():
    parser = argparse.ArgumentParser(description='Run DAO Deployment Platform API')
    parser.add_argument('--host', default='127.0.0.1', help='Host to bind to')
    parser.add_argument('--port', type=int, default=5000, help='Port to bind to')
    parser.add_argument('--production', action='store_true', help='Run in production mode')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    args = parser.parse_args()

    # Set environment
    if args.production:
        os.environ['FLASK_ENV'] = 'production'
    elif args.debug:
        os.environ['FLASK_ENV'] = 'development'

    # Create and run app
    app = create_app()

    if args.production:
        print(f"Production mode - use gunicorn to run:")
        print(f"  gunicorn -w 4 -b {args.host}:{args.port} 'src.api.app:create_app()'")
    else:
        print(f"Starting DAO Deployment Platform API on http://{args.host}:{args.port}")
        print("API Documentation:")
        print("  - Health check: GET /api/v1/health")
        print("  - System status: GET /api/v1/status")
        print("  - Create job: POST /api/v1/jobs")
        print("  - Get job: GET /api/v1/jobs/<job_id>")
        print("  - Validate XML: POST /api/v1/translate/validate")
        print("  - Generate contracts: POST /api/v1/translate/contracts")
        print()

        app.run(
            host=args.host,
            port=args.port,
            debug=not args.production
        )


if __name__ == '__main__':
    main()
