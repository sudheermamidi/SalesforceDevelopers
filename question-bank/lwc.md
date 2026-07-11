# Lightning Web Components Interview Questions

## Core Concepts

1. What is the difference between LWC and Aura?
2. Explain the LWC lifecycle hooks.
3. When do you use `@api`, `@track`, and `@wire`?
4. What is Lightning Data Service?
5. Compare `getRecord`, `getObjectInfo`, and Apex wire methods.
6. What is the difference between wire and imperative Apex calls?
7. How do parent and child components communicate?
8. How do unrelated components communicate?
9. How do you show toast messages and navigate to records?
10. How do you make an LWC secure and performant?

## Example Question

Question: Why should a cacheable Apex method not perform DML?

Answer: `@AuraEnabled(cacheable=true)` methods are expected to be read-only and
cacheable by the client. DML changes server state and breaks that contract. Use a
separate imperative Apex method for mutations.

## Practical Exercise

Build a Case triage LWC:

- Display open high-priority Cases.
- Allow filtering by queue, priority, and age.
- Show SLA status using colored badges.
- Allow the agent to assign a Case to self.
- Enforce field-level security in Apex.
- Include Jest tests for client logic and Apex tests for server logic.

