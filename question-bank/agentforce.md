# Agentforce Interview Questions

## Concepts

1. What problem does Agentforce solve in Salesforce?
2. Explain the difference between a chatbot, copilot, and autonomous agent.
3. What are topics, actions, instructions, and grounding?
4. How should an Agentforce agent use Salesforce data safely?
5. How do you design human handoff for service scenarios?
6. What is the role of Data Cloud in AI readiness?
7. How do you prevent an agent from making unsafe changes?
8. How would you test an agent before production rollout?
9. What metrics would you track after deployment?
10. How do you design actions that call Apex, Flow, or external APIs?

## Example Answer

Question: A service agent should summarize a customer issue and recommend next steps.
What should be grounded?

Answer: Ground the agent on Case fields, related Contact and Account context, Knowledge
articles, entitlement status, recent interactions, and permitted policy documents. The
agent should not use unverified external information for customer-specific decisions.

## Real-Time Scenario

Design an Agentforce service agent for a healthcare provider. The agent can answer
appointment questions, summarize care gaps, create follow-up tasks, and escalate to a
human nurse. Explain consent checks, audit logging, PHI handling, action permissions,
and fallback behavior.

