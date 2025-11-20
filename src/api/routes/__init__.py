"""
API routes package.
"""
from .jobs import jobs_bp
from .translate import translate_bp
from .health import health_bp

__all__ = ['jobs_bp', 'translate_bp', 'health_bp']
