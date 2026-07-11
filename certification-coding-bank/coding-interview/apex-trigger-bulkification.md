# Apex Coding Interview: Trigger Bulkification

Build a trigger and handler that updates Contact risk fields when Account tier changes.

```apex
trigger AccountTrigger on Account (after update) {
    AccountContactTierService.handleAfterUpdate(Trigger.oldMap, Trigger.newMap);
}
```

Expected answer: collect Account Ids, query Contacts once, update in one DML call, avoid recursion, and test 200 records.