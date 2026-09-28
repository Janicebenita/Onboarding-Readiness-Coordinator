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
