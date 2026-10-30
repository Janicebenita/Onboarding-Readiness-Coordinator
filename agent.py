"""Assess supplied onboarding prerequisites without approving them."""
from __future__ import annotations


def assess_readiness(record: dict) -> dict:
    required = [str(value) for value in record.get("required_items", [])]
    completed = {str(value) for value in record.get("completed_items", [])}
    verified = {str(value) for value in record.get("verified_items", [])}
    missing = [item for item in required if item not in completed]
    awaiting_verification = [item for item in required if item in completed and item not in verified]
    status = "ready-for-human-review" if not missing and not awaiting_verification else "not-ready"
    return {"person_id": record.get("person_id"), "status": status, "missing_items": missing, "awaiting_verification": awaiting_verification, "evidence": {"required": required, "completed": sorted(completed), "verified": sorted(verified)}, "approval_granted": False, "authorized_hr_review_required": True}
