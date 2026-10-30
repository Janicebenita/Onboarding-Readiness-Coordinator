import unittest
from agent import assess_readiness


class OnboardingTests(unittest.TestCase):
    def test_completed_but_unverified_item_is_not_ready(self):
        result = assess_readiness({"required_items": ["identity"], "completed_items": ["identity"]})
        self.assertEqual(result["status"], "not-ready")
        self.assertFalse(result["approval_granted"])


if __name__ == "__main__":
    unittest.main()
