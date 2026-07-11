# JavaScript Coding Interview: Transform Salesforce Rows

Write a function that groups Opportunity rows by StageName and totals Amount.

```javascript
export function totalByStage(rows) {
  return rows.reduce((acc, row) => {
    const stage = row.StageName || 'Unknown';
    acc[stage] = (acc[stage] || 0) + Number(row.Amount || 0);
    return acc;
  }, {});
}
```

Expected answer: discuss null handling, numeric conversion, immutability trade-offs, and tests.