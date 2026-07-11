# Apex Interview Questions

## Fundamentals

1. What is Apex and when should you use it instead of Flow?
2. Explain governor limits and why they exist in Salesforce.
3. What is the difference between `with sharing`, `without sharing`, and `inherited sharing`?
4. How do you bulkify Apex code?
5. What is the difference between `Database.insert(records, false)` and `insert records`?
6. Explain the order of execution in Salesforce.
7. What happens when a trigger performs DML on records of the same object?
8. How do you avoid trigger recursion?
9. What is a savepoint and rollback?
10. How do you enforce CRUD and field-level security in Apex?

## Async Apex

1. Compare Future methods, Queueable Apex, Batch Apex, and Scheduled Apex.
2. When would you chain Queueable jobs?
3. What are the limits of Future methods?
4. How do you test asynchronous Apex?
5. How do you handle partial failures in Batch Apex?

## Example Answer

Question: Why is this trigger not bulkified?

```apex
trigger AccountTrigger on Account (after update) {
    for (Account acc : Trigger.new) {
        List<Contact> contacts = [SELECT Id FROM Contact WHERE AccountId = :acc.Id];
        for (Contact c : contacts) {
            c.Description = 'Updated';
            update c;
        }
    }
}
```

Answer: It runs SOQL and DML inside loops. In bulk updates, this can exceed governor
limits. A better design collects Account Ids, queries Contacts once, updates the list,
and performs one DML operation.

## Real-Time Scenario

An integration updates 20,000 Accounts every night. Each Account update should update
related Contacts and publish a Platform Event when a high-value customer changes tier.
Design the Apex approach, explain governor-limit handling, partial failure strategy,
monitoring, and test coverage.

