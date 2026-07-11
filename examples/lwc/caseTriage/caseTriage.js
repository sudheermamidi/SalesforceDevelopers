import { LightningElement, wire } from 'lwc';
import getUrgentCases from '@salesforce/apex/CaseTriageController.getUrgentCases';
import claimCase from '@salesforce/apex/CaseTriageController.claimCase';
import { ShowToastEvent } from 'lightning/platformShowToastEvent';
import { refreshApex } from '@salesforce/apex';

export default class CaseTriage extends LightningElement {
    wiredCasesResult;
    cases = [];
    isLoading = false;

    @wire(getUrgentCases)
    wiredCases(result) {
        this.wiredCasesResult = result;
        if (result.data) {
            this.cases = result.data;
        }
    }

    async handleClaim(event) {
        this.isLoading = true;
        try {
            await claimCase({ caseId: event.currentTarget.dataset.id });
            this.dispatchEvent(new ShowToastEvent({
                title: 'Case claimed',
                message: 'The case is now assigned to you.',
                variant: 'success'
            }));
            await refreshApex(this.wiredCasesResult);
        } catch (error) {
            this.dispatchEvent(new ShowToastEvent({
                title: 'Unable to claim case',
                message: error.body?.message || 'Review permissions and try again.',
                variant: 'error'
            }));
        } finally {
            this.isLoading = false;
        }
    }
}

