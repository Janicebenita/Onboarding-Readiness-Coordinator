# Onboarding Readiness Coordinator Explainability

## Decision and Reasoning Process

The agent's decision process compares each onboarding requirement with its recorded status, owner, and due date. Its reasoning prioritizes overdue, blocking, and unassigned tasks according to the approved checklist.

## Inputs and Data Sources Used

Input data includes the onboarding checklist, start date, task owners, completion records, and authorized HR instructions. Only approved internal data sources are used, with sensitive data limited to what is necessary.

## Outputs and Supporting Evidence

The output contains readiness status, outstanding tasks, responsible owners, deadlines, and reminder suggestions. Evidence comes from the recorded task status and confirmation history.

## Limits, Constraints, and Known Issues

A limitation is that a recorded status may be outdated or incorrect. The agent is constrained from approving identity, legal, payroll, security, or compliance documentation.

## Uncertainty and Human Review

Uncertainty is reported when confirmations or ownership details are missing. Authorized HR staff must verify completion and handle sensitive exceptions.

## Implementation in This Repository

`agent.py` implements `assess_readiness(record)`. It compares required, completed, and independently verified item sets; separates missing from awaiting-verification items; returns only `ready-for-human-review` when every item is verified; retains all three sets as evidence; never grants approval; and requires authorized HR review. `test_agent.py` verifies that completed-but-unverified material remains not ready.

There is no HRIS, identity-verification, payroll, or access-provisioning connector. Authorized staff must verify every status and execute all consequential actions.
