from __future__ import annotations

import csv
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "datasets" / "generated"
random.seed(42)


INDUSTRIES = ["Healthcare", "Manufacturing", "Financial Services", "Retail", "Education", "Technology"]
TIERS = ["Bronze", "Silver", "Gold", "Platinum"]
PRIORITIES = ["Low", "Medium", "High", "Critical"]
CASE_TYPES = ["Billing", "Technical", "Clinical", "Shipping", "Access", "Complaint"]
STAGES = ["Prospecting", "Qualification", "Proposal", "Negotiation", "Closed Won", "Closed Lost"]
SPECIALTIES = ["Cardiology", "Primary Care", "Orthopedics", "Pediatrics", "Dermatology", "Neurology"]


def write_csv(path: Path, headers: list[str], rows) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        writer.writerows(rows)


def account_rows(count: int):
    for i in range(1, count + 1):
        yield [
            f"ACC-{i:08d}",
            f"Acme Practice Group {i}",
            random.choice(INDUSTRIES),
            random.choice(TIERS),
            f"{random.randint(10, 9999)} Market Street",
            random.choice(["Austin", "Chicago", "San Diego", "Atlanta", "Boston", "Seattle"]),
            random.choice(["TX", "IL", "CA", "GA", "MA", "WA"]),
            random.randint(5, 5000),
            random.randint(25000, 9000000),
            f"External-{i:08d}",
        ]


def contact_rows(count: int, account_count: int):
    for i in range(1, count + 1):
        account_id = random.randint(1, account_count)
        yield [
            f"CON-{i:08d}",
            f"First{i}",
            f"Last{i}",
            f"person{i}@example.com",
            f"+1-555-{random.randint(100,999)}-{random.randint(1000,9999)}",
            f"ACC-{account_id:08d}",
            random.choice(["Decision Maker", "Influencer", "Practitioner", "Billing Contact"]),
            random.choice(["Email", "Phone", "SMS", "Portal"]),
            random.choice(["Active", "Inactive", "Do Not Contact"]),
        ]


def opportunity_rows(count: int, account_count: int):
    for i in range(1, count + 1):
        account_id = random.randint(1, account_count)
        stage = random.choice(STAGES)
        amount = random.randint(5000, 750000)
        yield [
            f"OPP-{i:08d}",
            f"Expansion Deal {i}",
            f"ACC-{account_id:08d}",
            stage,
            amount,
            random.randint(5, 95) if not stage.startswith("Closed") else (100 if stage == "Closed Won" else 0),
            f"2026-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
            random.choice(["New Business", "Renewal", "Upsell", "Cross-sell"]),
        ]


def case_rows(count: int, account_count: int, contact_count: int):
    for i in range(1, count + 1):
        yield [
            f"CAS-{i:08d}",
            f"ACC-{random.randint(1, account_count):08d}",
            f"CON-{random.randint(1, contact_count):08d}",
            random.choice(PRIORITIES),
            random.choice(CASE_TYPES),
            random.choice(["New", "Working", "Escalated", "Waiting on Customer", "Closed"]),
            random.choice(["Phone", "Email", "Web", "Agentforce", "Chat"]),
            f"Customer needs help with scenario {i}. Include enough text for search and triage practice.",
            random.randint(1, 240),
        ]


def health_rows(count: int, contact_count: int):
    for i in range(1, count + 1):
        yield [
            f"HCP-{i:08d}",
            f"CON-{random.randint(1, contact_count):08d}",
            random.choice(SPECIALTIES),
            random.choice(["Low", "Medium", "High"]),
            random.choice(["Consent Granted", "Consent Pending", "Consent Revoked"]),
            random.choice(["Annual wellness", "Follow-up", "Care gap closure", "Medication review"]),
            f"2026-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
            f"Synthetic care note {i} for Health Cloud interview practice and reporting drills.",
        ]


def main() -> None:
    account_count = 350_000
    contact_count = 700_000
    case_headers = ["ExternalId", "AccountExternalId", "ContactExternalId", "Priority", "Type", "Status", "Origin", "Description", "AgeHours"]

    write_csv(
        OUT / "accounts_synthetic.csv",
        ["ExternalId", "Name", "Industry", "Tier", "BillingStreet", "BillingCity", "BillingState", "Employees", "AnnualRevenue", "LegacySystemId"],
        account_rows(account_count),
    )
    write_csv(
        OUT / "contacts_synthetic.csv",
        ["ExternalId", "FirstName", "LastName", "Email", "Phone", "AccountExternalId", "Role", "PreferredChannel", "Status"],
        contact_rows(contact_count, account_count),
    )
    write_csv(
        OUT / "opportunities_synthetic.csv",
        ["ExternalId", "Name", "AccountExternalId", "StageName", "Amount", "Probability", "CloseDate", "Type"],
        opportunity_rows(450_000, account_count),
    )
    write_csv(OUT / "cases_synthetic_part1.csv", case_headers, case_rows(325_000, account_count, contact_count))
    write_csv(OUT / "cases_synthetic_part2.csv", case_headers, case_rows(325_000, account_count, contact_count))
    write_csv(
        OUT / "health_cloud_synthetic.csv",
        ["ExternalId", "PatientContactExternalId", "Specialty", "RiskLevel", "ConsentStatus", "CarePlanFocus", "NextAppointmentDate", "CareNote"],
        health_rows(450_000, contact_count),
    )


if __name__ == "__main__":
    main()
