from django.core.cache import cache
import logging

logger = logging.getLogger('shopper')

WORKFLOW_STATES = ["applied", "interview_started", "interview_completed", "onboarding_requested", "onboarding_completed", "hired", "rejected"]

