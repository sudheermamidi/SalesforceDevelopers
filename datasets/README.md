# Synthetic Salesforce Practice Datasets

These CSV files are generated for interview and hands-on practice. They contain fake
records only.

Use them for:

- Data Loader import and export practice.
- Bulk API practice.
- SOQL filtering and reporting drills.
- Duplicate and matching-rule exercises.
- Account, Contact, Opportunity, Case, and health-service workflow modelling.

Generate datasets:

```powershell
python scripts/generate_synthetic_salesforce_data.py
```

The generator writes several CSV files under `datasets/generated/`. The combined size is
intentionally above 150 MB for realistic data-loading practice while keeping each file
below common GitHub file-size limits.

