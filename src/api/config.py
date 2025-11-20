"""
Configuration for the DAO Deployment Platform API.
"""
import os
from pathlib import Path


class Config:
    """Base configuration."""

    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = False
    TESTING = False

    # API settings
    API_VERSION = 'v1'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload

    # Paths
    BASE_DIR = Path(__file__).parent.parent.parent
    TEMPLATES_DIR = BASE_DIR / 'Templates'
    OUTPUT_DIR = BASE_DIR / 'output'
    JOBS_DIR = BASE_DIR / 'jobs'

    # Hardhat settings
    HARDHAT_PROJECT_DIR = BASE_DIR / 'hardhat_workspace'
    HARDHAT_TIMEOUT = 300  # 5 minutes timeout for test execution

    # Blockchain settings
    DEFAULT_NETWORK = 'localhost'
    NETWORKS = {
        'localhost': {
            'url': 'http://127.0.0.1:8545',
            'chain_id': 31337,
        },
        'sepolia': {
            'url': os.environ.get('SEPOLIA_RPC_URL', ''),
            'chain_id': 11155111,
        },
        'goerli': {
            'url': os.environ.get('GOERLI_RPC_URL', ''),
            'chain_id': 5,
        },
        'mainnet': {
            'url': os.environ.get('MAINNET_RPC_URL', ''),
            'chain_id': 1,
        },
    }

    # Deployment settings
    DEPLOYER_PRIVATE_KEY = os.environ.get('DEPLOYER_PRIVATE_KEY', '')
    GAS_LIMIT = 8000000

    # Job settings
    JOB_RETENTION_HOURS = 24
    MAX_CONCURRENT_JOBS = 5

    # CORS settings
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*').split(',')


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False

    def __init__(self):
        if not os.environ.get('SECRET_KEY'):
            raise ValueError("SECRET_KEY must be set in production")


def get_config():
    """Get configuration based on environment."""
    env = os.environ.get('FLASK_ENV', 'development')
    configs = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
    }
    return configs.get(env, DevelopmentConfig)()
