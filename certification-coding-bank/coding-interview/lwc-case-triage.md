# LWC Coding Interview: Case Triage

Build an LWC that shows urgent cases, supports filters, and lets an agent claim a case.

```javascript
import { LightningElement, wire } from 'lwc';
import getCases from '@salesforce/apex/CaseTriageController.getCases';
export default class CaseTriage extends LightningElement {
  @wire(getCases) cases;
}
```

Expected answer: handle loading, error, refreshApex, FLS-safe Apex, pagination, and Jest tests.