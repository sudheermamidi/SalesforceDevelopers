public inherited sharing class BulkifiedAccountContactService {
    public static void updateContactsForTierChanges(
        Map<Id, Account> oldMap,
        Map<Id, Account> newMap
    ) {
        Set<Id> changedAccountIds = new Set<Id>();

        for (Id accountId : newMap.keySet()) {
            Account oldAccount = oldMap.get(accountId);
            Account newAccount = newMap.get(accountId);
            if (oldAccount.Customer_Tier__c != newAccount.Customer_Tier__c) {
                changedAccountIds.add(accountId);
            }
        }

        if (changedAccountIds.isEmpty()) {
            return;
        }

        List<Contact> contactsToUpdate = [
            SELECT Id, AccountId, Customer_Tier__c
            FROM Contact
            WHERE AccountId IN :changedAccountIds
        ];

        for (Contact contactRecord : contactsToUpdate) {
            contactRecord.Customer_Tier__c = newMap.get(contactRecord.AccountId).Customer_Tier__c;
        }

        if (!contactsToUpdate.isEmpty()) {
            update contactsToUpdate;
        }
    }
}

