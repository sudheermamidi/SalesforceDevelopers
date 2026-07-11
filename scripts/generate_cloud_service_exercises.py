from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "cloud-service-live-exercises"


CLOUDS = [
    {
        "slug": "sales-cloud",
        "name": "Sales Cloud",
        "focus": "lead-to-cash, pipeline management, forecasting, activity capture, account planning",
        "objects": "Lead, Account, Contact, Opportunity, Product, Pricebook, Quote, Campaign",
        "advanced": [
            "enterprise territory management and account teams",
            "forecast category governance",
            "duplicate prevention across lead sources",
            "high-volume lead assignment",
            "multi-currency opportunity reporting",
        ],
        "scenarios": [
            "A SaaS company receives 50,000 inbound leads per month and needs automated routing, duplicate prevention, and SLA tracking.",
            "A global manufacturer wants territory-based visibility, partner-sourced pipeline tracking, and regional forecast rollups.",
            "A sales operations team needs renewal opportunities generated automatically with product history and health score context.",
        ],
    },
    {
        "slug": "service-cloud",
        "name": "Service Cloud",
        "focus": "case management, entitlements, milestones, knowledge, Omni-Channel, contact-center productivity",
        "objects": "Case, Entitlement, Milestone, Knowledge, Contact, Account, Queue, User",
        "advanced": [
            "Omni-Channel capacity and skills-based routing",
            "entitlement milestone breach handling",
            "case deflection with Knowledge and Agentforce",
            "console performance and macros",
            "multi-channel support operations",
        ],
        "scenarios": [
            "A contact center has SLA breaches because urgent cases sit in the wrong queue for more than two hours.",
            "A support team wants Knowledge suggestions, macros, and case summaries embedded in the service console.",
            "A global support org must route cases by product, language, customer tier, and agent capacity.",
        ],
    },
    {
        "slug": "marketing-cloud",
        "name": "Marketing Cloud",
        "focus": "journeys, segmentation, subscriber identity, personalization, consent, cross-cloud data",
        "objects": "Contact, Data Extension, Subscriber, Journey, Campaign, Lead, Contact Point Consent",
        "advanced": [
            "Contact Key and Subscriber Key governance",
            "Marketing Cloud Connect synchronization",
            "Journey Builder entry criteria and re-entry rules",
            "AMPscript personalization and fallback logic",
            "deliverability and suppression strategy",
        ],
        "scenarios": [
            "A retail company wants a welcome journey triggered by Sales Cloud lead creation with personalized content.",
            "A healthcare provider needs appointment reminders that respect consent and suppress opted-out patients.",
            "A marketing team wants abandoned-cart and renewal campaigns with engagement data synced back to CRM.",
        ],
    },
    {
        "slug": "health-cloud",
        "name": "Health Cloud",
        "focus": "patient 360, care coordination, care plans, consent, referrals, provider network workflows",
        "objects": "Account, Contact, CarePlan, CareTeam, ClinicalEncounter, HealthcareProvider, ContactPointConsent",
        "advanced": [
            "PHI access model and audit requirements",
            "FHIR-based integration patterns",
            "care-gap closure workflow",
            "provider relationship modelling",
            "patient consent and communication preferences",
        ],
        "scenarios": [
            "A care management team needs a patient onboarding process with consent, risk assessment, and care-team assignment.",
            "A hospital needs post-discharge follow-up tasks based on clinical events from an EHR.",
            "A payer needs prior authorization workflows with provider, member, and clinical-document context.",
        ],
    },
    {
        "slug": "data-cloud",
        "name": "Data Cloud",
        "focus": "data ingestion, identity resolution, segmentation, calculated insights, activation, AI grounding",
        "objects": "Data Stream, Data Lake Object, Data Model Object, Unified Individual, Segment, Activation Target",
        "advanced": [
            "identity resolution rules",
            "data mapping and harmonization",
            "calculated insights",
            "segment activation",
            "Agentforce grounding with unified data",
        ],
        "scenarios": [
            "A company wants a unified customer profile from Sales Cloud, Service Cloud, website events, and marketing data.",
            "A support leader wants customer-health segments activated into Service Cloud queues.",
            "An Agentforce assistant needs grounded answers using unified profile and interaction history.",
        ],
    },
    {
        "slug": "agentforce",
        "name": "Agentforce",
        "focus": "AI agents, topics, actions, grounding, human handoff, trust, monitoring",
        "objects": "Agent, Topic, Action, Flow, Apex, Knowledge, Case, Account, Data Cloud Profile",
        "advanced": [
            "safe action design",
            "agent testing and evaluation",
            "grounding source governance",
            "human handoff design",
            "auditability and prompt safety",
        ],
        "scenarios": [
            "A service agent should summarize a case, recommend a knowledge article, and escalate when confidence is low.",
            "A sales assistant should qualify leads, create follow-up tasks, and coach reps using CRM context.",
            "A healthcare assistant should answer appointment questions while respecting consent and PHI boundaries.",
        ],
    },
    {
        "slug": "experience-cloud",
        "name": "Experience Cloud",
        "focus": "customer, partner, and employee portals with secure self-service",
        "objects": "User, Account, Contact, Case, Knowledge, Experience Site, Sharing Set, External Account Hierarchy",
        "advanced": [
            "external user sharing architecture",
            "guest user security",
            "site performance",
            "self-registration and identity",
            "portal case deflection",
        ],
        "scenarios": [
            "A partner portal needs deal registration, opportunity collaboration, and account-specific visibility.",
            "A customer community needs case creation, case status, and Knowledge deflection.",
            "A healthcare member portal needs secure appointment and care-plan visibility.",
        ],
    },
    {
        "slug": "commerce-cloud",
        "name": "Commerce Cloud",
        "focus": "digital commerce, catalog, cart, checkout, order integration, personalization",
        "objects": "Product, Pricebook, Catalog, Cart, Order, Account, Contact, Promotion",
        "advanced": [
            "B2B account-based pricing",
            "cart and checkout extensibility",
            "order management integration",
            "inventory availability",
            "commerce personalization",
        ],
        "scenarios": [
            "A B2B distributor needs account-specific catalogs, negotiated pricing, and approval-based checkout.",
            "A retailer needs cart abandonment journeys connected to Marketing Cloud.",
            "A support team needs order status visible in Service Cloud from commerce transactions.",
        ],
    },
    {
        "slug": "field-service",
        "name": "Field Service",
        "focus": "work orders, scheduling, dispatch, mobile technicians, assets, service appointments",
        "objects": "WorkOrder, ServiceAppointment, ServiceResource, ServiceTerritory, Asset, ProductConsumed",
        "advanced": [
            "optimization and scheduling policies",
            "mobile offline design",
            "asset service history",
            "parts consumption",
            "service territory capacity",
        ],
        "scenarios": [
            "A utility company needs emergency work orders routed to certified technicians by territory.",
            "A medical-device company needs asset maintenance visits with parts consumption and mobile offline support.",
            "A dispatcher needs real-time schedule optimization and SLA visibility.",
        ],
    },
    {
        "slug": "financial-services-cloud",
        "name": "Financial Services Cloud",
        "focus": "households, financial accounts, goals, referrals, relationship groups, advisor productivity",
        "objects": "Person Account, Household, FinancialAccount, FinancialGoal, RelationshipGroup, InteractionSummary",
        "advanced": [
            "household data modelling",
            "advisor book-of-business visibility",
            "compliance notes and interaction summaries",
            "financial account aggregation",
            "referral lifecycle",
        ],
        "scenarios": [
            "A wealth firm needs advisor dashboards for household assets, goals, and next-best actions.",
            "A bank needs referral tracking from branch staff to mortgage specialists.",
            "An insurance team needs policyholder relationship visibility and regulated interaction logging.",
        ],
    },
    {
        "slug": "revenue-cloud",
        "name": "Revenue Cloud and CPQ",
        "focus": "products, bundles, pricing, quotes, approvals, contracts, billing handoff",
        "objects": "Product, Pricebook, Quote, QuoteLine, Contract, Order, Opportunity, Approval",
        "advanced": [
            "bundle configuration rules",
            "price rules and discount governance",
            "quote approval architecture",
            "amendment and renewal handling",
            "ERP billing integration",
        ],
        "scenarios": [
            "A SaaS company needs guided product bundles, discount approvals, and automated renewals.",
            "A manufacturer needs complex pricing by region, customer tier, and contract terms.",
            "A finance team needs quote-to-order handoff with tax and billing integration.",
        ],
    },
    {
        "slug": "manufacturing-cloud",
        "name": "Manufacturing Cloud",
        "focus": "sales agreements, account forecasts, run-rate business, partner planning",
        "objects": "SalesAgreement, AccountForecast, Account, Opportunity, Product, Partner",
        "advanced": [
            "sales agreement lifecycle",
            "forecast reconciliation",
            "volume commitments",
            "partner visibility",
            "ERP demand-plan integration",
        ],
        "scenarios": [
            "A manufacturer needs sales agreements with planned versus actual quantity tracking.",
            "A planning team needs account forecasts synced with ERP demand planning.",
            "A channel team needs partner-specific visibility into committed volumes.",
        ],
    },
    {
        "slug": "salesforce-platform",
        "name": "Salesforce Platform",
        "focus": "custom apps, metadata, automation, security, APIs, mobile, extensibility",
        "objects": "Custom Object, Flow, Apex, LWC, Permission Set, Custom Metadata, Platform Event",
        "advanced": [
            "metadata-driven architecture",
            "platform limits and scale design",
            "custom app security model",
            "automation governance",
            "extension strategy with Apex, Flow, and LWC",
        ],
        "scenarios": [
            "An operations team needs a custom onboarding app with approvals, task automation, and audit reporting.",
            "A product team wants reusable platform services shared across multiple Salesforce clouds.",
            "An enterprise architecture team needs automation governance across hundreds of flows and triggers.",
        ],
    },
    {
        "slug": "mulesoft",
        "name": "MuleSoft",
        "focus": "API-led connectivity, system/process/experience APIs, orchestration, monitoring",
        "objects": "API, Connector, Flow, Policy, Runtime, Anypoint Exchange, Salesforce Connector",
        "advanced": [
            "API-led connectivity layers",
            "policy and rate-limit design",
            "error handling and retries",
            "contract-first API design",
            "Salesforce integration observability",
        ],
        "scenarios": [
            "A company needs Salesforce to integrate with ERP, billing, and warehouse systems through reusable APIs.",
            "A healthcare provider needs EHR data exposed safely to Health Cloud and Experience Cloud.",
            "A support team needs an API gateway strategy for partner case creation and status updates.",
        ],
    },
    {
        "slug": "analytics-tableau",
        "name": "Analytics and Tableau",
        "focus": "CRM Analytics, Tableau dashboards, data visualization, embedded analytics, KPI governance",
        "objects": "Dataset, Dashboard, Lens, Dataflow, Recipe, Tableau Workbook, Report",
        "advanced": [
            "semantic KPI governance",
            "row-level security",
            "embedded analytics",
            "data refresh strategy",
            "executive dashboard performance",
        ],
        "scenarios": [
            "A leadership team needs a cross-cloud executive dashboard for pipeline, cases, revenue, and churn risk.",
            "A service leader needs SLA breach analytics with drill-down to queue, agent, and customer tier.",
            "A healthcare executive needs care-gap and patient engagement analytics with restricted access.",
        ],
    },
    {
        "slug": "education-cloud",
        "name": "Education Cloud",
        "focus": "student lifecycle, recruitment, advising, engagement, advancement, institutional relationships",
        "objects": "Contact, Account, Program, Course, Application, Case, Advising Note, Campaign",
        "advanced": [
            "student 360 data model",
            "advisor security and caseload visibility",
            "application lifecycle automation",
            "engagement scoring",
            "integration with student information systems",
        ],
        "scenarios": [
            "A university needs applicant tracking from inquiry to enrollment with advisor handoff.",
            "An advising team needs early-alert cases and intervention plans for at-risk students.",
            "An advancement team needs donor engagement visibility connected to alumni relationships.",
        ],
    },
    {
        "slug": "nonprofit-cloud",
        "name": "Nonprofit Cloud",
        "focus": "fundraising, programs, case management, outcomes, donor and constituent engagement",
        "objects": "Account, Contact, Gift, Campaign, Program, Benefit, Case, Outcome",
        "advanced": [
            "constituent relationship modelling",
            "gift and recurring donation lifecycle",
            "program outcome tracking",
            "grant reporting",
            "volunteer and case-management visibility",
        ],
        "scenarios": [
            "A nonprofit needs donor management with recurring gifts, campaigns, and impact reporting.",
            "A program team needs participant intake, services delivered, and outcome measurement.",
            "A volunteer coordinator needs shift registration and constituent engagement history.",
        ],
    },
    {
        "slug": "public-sector-solutions",
        "name": "Public Sector Solutions",
        "focus": "licenses, permits, inspections, benefits, grants, citizen service, compliance",
        "objects": "Application, License, Permit, Inspection, Case, Account, Contact, Benefit",
        "advanced": [
            "citizen portal security",
            "application intake and eligibility rules",
            "inspection scheduling",
            "caseworker workload management",
            "audit and compliance reporting",
        ],
        "scenarios": [
            "A city needs online permit applications with document upload, review, inspection, and approval.",
            "A benefits agency needs eligibility screening and caseworker assignment.",
            "A regulatory agency needs license renewal workflows with audit history.",
        ],
    },
    {
        "slug": "consumer-goods-cloud",
        "name": "Consumer Goods Cloud",
        "focus": "retail execution, store visits, inventory checks, promotions, field rep productivity",
        "objects": "RetailStore, Visit, Account, Product, Promotion, InventoryCheck, AssessmentTask",
        "advanced": [
            "visit planning and execution",
            "offline mobile tasks",
            "promotion compliance",
            "store inventory visibility",
            "field rep performance analytics",
        ],
        "scenarios": [
            "A beverage company needs field reps to complete store visits with promotion compliance photos.",
            "A retail execution team needs route planning, task checklists, and inventory issue capture.",
            "A manager needs dashboards for visit completion, shelf availability, and promotion performance.",
        ],
    },
    {
        "slug": "communications-cloud",
        "name": "Communications Cloud",
        "focus": "subscriber lifecycle, guided selling, order capture, service requests, telecom product models",
        "objects": "Account, Contact, Product, Asset, Order, Case, Quote, ServiceAccount",
        "advanced": [
            "complex product catalogue",
            "asset-based ordering",
            "service eligibility checks",
            "omnichannel subscriber support",
            "order fallout management",
        ],
        "scenarios": [
            "A telecom provider needs guided selling for internet, mobile, and bundle offers.",
            "A subscriber support team needs asset visibility and service-change workflows.",
            "An operations team needs order fallout cases when provisioning fails.",
        ],
    },
    {
        "slug": "energy-utilities-cloud",
        "name": "Energy and Utilities Cloud",
        "focus": "customer programs, service connections, outage support, field work, utility account management",
        "objects": "Account, ServicePoint, Premise, Case, WorkOrder, ProgramEnrollment, Asset",
        "advanced": [
            "service point and premise modelling",
            "outage communication workflow",
            "program enrollment automation",
            "meter and asset integration",
            "field-service coordination",
        ],
        "scenarios": [
            "A utility needs service-start and service-stop workflows with identity verification.",
            "A grid operations team needs outage cases connected to affected premises and proactive notifications.",
            "A sustainability program needs customer enrollment, eligibility checks, and rebate tracking.",
        ],
    },
    {
        "slug": "automotive-cloud",
        "name": "Automotive Cloud",
        "focus": "vehicle lifecycle, dealer engagement, customer mobility, service history, connected data",
        "objects": "Vehicle, Account, Contact, Lead, Opportunity, Case, Asset, ServiceAppointment",
        "advanced": [
            "vehicle-owner relationship model",
            "dealer network visibility",
            "service history integration",
            "connected-vehicle data use cases",
            "consent and preference handling",
        ],
        "scenarios": [
            "An OEM needs a vehicle owner 360 with warranty, service history, and dealer interactions.",
            "A dealer network needs lead routing and handoff visibility.",
            "A customer care team needs proactive service cases from connected-vehicle alerts.",
        ],
    },
]


DEVELOPMENT_AREAS = [
    {
        "slug": "apex-development",
        "name": "Apex Development",
        "focus": "domain logic, triggers, services, async processing, testing, integrations",
        "advanced": ["trigger frameworks", "selector-service-domain patterns", "unit of work", "async orchestration", "secure Apex"],
    },
    {
        "slug": "lwc-development",
        "name": "LWC Development",
        "focus": "component architecture, LDS, Apex integration, UX state, testing, accessibility",
        "advanced": ["wire caching", "Lightning Message Service", "Jest tests", "console navigation", "performance profiling"],
    },
    {
        "slug": "omnistudio-development",
        "name": "OmniStudio Development",
        "focus": "guided processes, FlexCards, OmniScripts, DataRaptors, Integration Procedures",
        "advanced": ["reusable OmniScripts", "IP caching", "remote actions", "JSON transforms", "deployment strategy"],
    },
    {
        "slug": "integration-development",
        "name": "Integration Development",
        "focus": "REST, Bulk API, Platform Events, Named Credentials, middleware, retries",
        "advanced": ["idempotency", "event replay", "OAuth/JWT", "Composite API", "dead-letter handling"],
    },
    {
        "slug": "flow-development",
        "name": "Flow and Automation",
        "focus": "record-triggered flows, screen flows, invocable Apex, orchestration, approvals",
        "advanced": ["flow trigger order", "fault paths", "subflows", "flow tests", "Apex boundaries"],
    },
    {
        "slug": "devops-release",
        "name": "DevOps and Release Engineering",
        "focus": "Salesforce CLI, metadata, packages, CI/CD, environments, validation, rollback",
        "advanced": ["source tracking", "unlocked packages", "destructive changes", "quality gates", "release governance"],
    },
]


SUPPORT_AREAS = [
    {
        "slug": "production-support",
        "name": "Production Support",
        "focus": "incident triage, logs, user issues, automation failures, deployment rollback",
        "advanced": ["debug log strategy", "failed flow interviews", "Apex exception monitoring", "data repair", "hotfix governance"],
    },
    {
        "slug": "data-support",
        "name": "Data and Migration Support",
        "focus": "imports, exports, reconciliation, duplicates, LDV performance, record locks",
        "advanced": ["Bulk API batches", "external IDs", "query plan analysis", "ownership skew", "reconciliation reports"],
    },
    {
        "slug": "security-support",
        "name": "Security and Access Support",
        "focus": "profile and permission issues, sharing, field visibility, integration users, audit",
        "advanced": ["restriction rules", "debugging implicit sharing", "permission set groups", "login forensics", "least privilege reviews"],
    },
    {
        "slug": "release-support",
        "name": "Release Support",
        "focus": "deployment validation, smoke testing, post-deploy checks, rollback, release notes",
        "advanced": ["deployment dependency mapping", "test class failures", "metadata conflicts", "sandbox refresh planning", "backout plans"],
    },
]


def exercise_block(name: str, focus: str, objects: str | None, advanced: list[str], scenario: str, number: int) -> list[str]:
    object_line = f"- Core objects/components: {objects}" if objects else "- Core components: choose the relevant metadata, automation, code, and integration assets."
    return [
        f"### Live Example Exercise {number}: {scenario}",
        "",
        "**Business Goal**",
        "",
        f"Build or troubleshoot a realistic Salesforce solution for this scenario. The focus is {focus}.",
        "",
        "**Expected Architecture**",
        "",
        object_line,
        "- Entry points: UI, automation, API, scheduled process, or AI agent depending on the scenario.",
        "- Security: profile/permission set access, record sharing, field-level security, and audit requirements.",
        "- Operations: monitoring, error handling, retry or rollback plan, and support handoff notes.",
        "",
        "**Hands-On Tasks**",
        "",
        "1. Draw the data model and integration or automation flow.",
        "2. Configure the minimum viable solution in a sandbox or Trailhead playground.",
        "3. Add validation, duplicate handling, or entitlement rules where relevant.",
        "4. Build at least one report or dashboard to prove the process works.",
        "5. Write test cases, support runbook notes, and interview talking points.",
        "",
        "**Advanced Topics to Discuss**",
        "",
        *[f"- {item}" for item in advanced],
        "",
        "**Support Drill**",
        "",
        "A user reports that the process worked yesterday but fails today for only some records. "
        "Identify the logs, setup areas, data samples, permissions, and recent deployments you would inspect first.",
        "",
        "**Senior Interview Questions**",
        "",
        f"1. What trade-offs would you make when designing {name} for enterprise scale?",
        "2. Which parts should be declarative, and which parts justify custom development?",
        "3. How would you monitor failures and prove business value after go-live?",
        "4. What data-volume, security, or compliance risk could break this design?",
        "",
    ]


def write_cloud(cloud: dict[str, object]) -> None:
    lines = [
        f"# {cloud['name']} Live Exercises and Advanced Topics",
        "",
        f"Focus: {cloud['focus']}.",
        "",
        "Use these exercises for interview preparation, sandbox practice, and support-role readiness.",
        "",
        "## Advanced Topic Checklist",
        "",
        *[f"- {item}" for item in cloud["advanced"]],
        "",
        "## Live Example Exercises",
        "",
    ]
    for idx, scenario in enumerate(cloud["scenarios"], start=1):
        lines.extend(exercise_block(cloud["name"], cloud["focus"], cloud["objects"], cloud["advanced"], scenario, idx))
    (OUT / "clouds" / f"{cloud['slug']}.md").write_text("\n".join(lines), encoding="utf-8")


def write_area(area: dict[str, object], folder: str) -> None:
    scenarios = [
        f"Build a production-ready pattern for {area['focus']}.",
        f"Troubleshoot a failed business process involving {area['focus']}.",
        f"Prepare a senior interview whiteboard explanation for {area['focus']}.",
    ]
    lines = [
        f"# {area['name']} Live Exercises and Advanced Topics",
        "",
        f"Focus: {area['focus']}.",
        "",
        "## Advanced Topic Checklist",
        "",
        *[f"- {item}" for item in area["advanced"]],
        "",
        "## Live Example Exercises",
        "",
    ]
    for idx, scenario in enumerate(scenarios, start=1):
        lines.extend(exercise_block(area["name"], area["focus"], None, area["advanced"], scenario, idx))
    (OUT / folder / f"{area['slug']}.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    (OUT / "clouds").mkdir(parents=True, exist_ok=True)
    (OUT / "development").mkdir(parents=True, exist_ok=True)
    (OUT / "support").mkdir(parents=True, exist_ok=True)

    for cloud in CLOUDS:
        write_cloud(cloud)
    for area in DEVELOPMENT_AREAS:
        write_area(area, "development")
    for area in SUPPORT_AREAS:
        write_area(area, "support")

    index = [
        "# Cloud Services, Development, and Support Live Exercises",
        "",
        "This section contains live-style Salesforce exercises for cloud services, development areas, and support responsibilities.",
        "Each file includes realistic business scenarios, hands-on tasks, advanced topics, support drills, and senior interview questions.",
        "",
        "## Cloud Service Exercises",
        "",
        *[f"- [{cloud['name']}](clouds/{cloud['slug']}.md)" for cloud in CLOUDS],
        "",
        "## Development Area Exercises",
        "",
        *[f"- [{area['name']}](development/{area['slug']}.md)" for area in DEVELOPMENT_AREAS],
        "",
        "## Support Area Exercises",
        "",
        *[f"- [{area['name']}](support/{area['slug']}.md)" for area in SUPPORT_AREAS],
        "",
        "## How to Practice",
        "",
        "1. Pick one exercise and explain the business problem in plain English.",
        "2. Sketch the data model and automation or integration path.",
        "3. Build a small proof of concept in a Salesforce sandbox or Trailhead playground.",
        "4. Prepare support notes: logs to check, failure modes, rollback plan, and monitoring.",
        "5. Answer the senior interview questions without reading notes.",
    ]
    (OUT / "README.md").write_text("\n".join(index), encoding="utf-8")


if __name__ == "__main__":
    main()
