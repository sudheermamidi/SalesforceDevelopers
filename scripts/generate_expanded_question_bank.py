from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "question-bank-expanded"


TOPICS = {
    "apex": {
        "title": "Apex",
        "concepts": [
            "governor limits", "bulkification", "trigger order of execution", "SOQL selectivity",
            "DML partial success", "transaction boundaries", "Queueable Apex", "Batch Apex",
            "Future methods", "Scheduled Apex", "platform events", "Apex tests", "mock callouts",
            "test data factories", "sharing keywords", "CRUD and FLS enforcement", "Apex exceptions",
            "recursion guards", "custom metadata", "dynamic SOQL", "SOSL", "Database methods",
            "savepoints", "callouts", "continuations", "Apex REST", "managed packages",
            "CPU time", "heap size", "mixed DML", "with security_enforced", "user-mode DML",
            "selector classes", "service classes", "domain layer", "Unit of Work", "invocable Apex",
            "Flow and Apex boundaries", "change data capture", "record locking", "large data volumes",
        ],
        "scenarios": [
            "nightly Account and Contact synchronization", "high-volume Case reassignment",
            "external order-status callout", "duplicate Lead cleanup", "opportunity renewal automation",
            "healthcare patient task generation", "marketing consent update", "partner portal sharing update",
        ],
    },
    "lwc": {
        "title": "Lightning Web Components",
        "concepts": [
            "component lifecycle", "wire service", "imperative Apex", "Lightning Data Service",
            "UI API", "parent-child events", "Lightning Message Service", "public properties",
            "reactivity", "template directives", "navigation service", "toast messages",
            "record edit forms", "custom datatables", "Jest testing", "Apex caching",
            "performance optimization", "accessibility", "error handling", "spinners",
            "slots", "composition", "Experience Cloud", "static resources", "third-party libraries",
            "CSS scoping", "security", "field-level security", "offline considerations", "mobile layout",
        ],
        "scenarios": [
            "service console case triage", "sales dashboard", "healthcare appointment viewer",
            "guided lead intake", "marketing preference center", "agent productivity panel",
            "contract review workspace", "omni-channel supervisor wallboard",
        ],
    },
    "agentforce": {
        "title": "Agentforce",
        "concepts": [
            "agent topics", "agent actions", "grounding", "instructions", "human handoff",
            "trust boundaries", "audit logging", "action permissions", "Flow actions", "Apex actions",
            "external API actions", "Data Cloud grounding", "Knowledge grounding", "prompt safety",
            "testing agents", "conversation evaluation", "fallback behavior", "case summarization",
            "lead qualification", "service deflection", "PII and PHI handling", "business guardrails",
            "agent monitoring", "intent routing", "channel deployment", "Slack integration",
        ],
        "scenarios": [
            "healthcare appointment assistant", "service refund assistant", "sales coaching assistant",
            "marketing campaign assistant", "field-service scheduling assistant", "support knowledge assistant",
            "partner onboarding assistant", "care-gap outreach assistant",
        ],
    },
    "omnistudio": {
        "title": "OmniStudio",
        "concepts": [
            "OmniScripts", "FlexCards", "DataRaptor Extract", "DataRaptor Load",
            "DataRaptor Transform", "Integration Procedures", "Remote Actions", "Set Values",
            "Response Actions", "conditional views", "reusable OmniScripts", "versioning",
            "deployment", "debugging", "performance", "caching", "JSON nodes",
            "data mapping", "guided flows", "industry cloud use cases", "error handling",
        ],
        "scenarios": [
            "insurance claim intake", "patient onboarding", "guided selling", "service eligibility check",
            "loan application", "benefits enrollment", "contact-center script", "field agent checklist",
        ],
    },
    "sales-cloud": {
        "title": "Sales Cloud",
        "concepts": [
            "Lead conversion", "Opportunity stages", "Forecast categories", "Account teams",
            "Opportunity teams", "territory management", "duplicate rules", "matching rules",
            "campaign influence", "quotes", "products and price books", "pipeline reporting",
            "sales process", "approval processes", "assignment rules", "activity management",
            "Einstein scoring", "data quality", "role hierarchy", "sharing rules",
        ],
        "scenarios": [
            "B2B lead-to-cash process", "enterprise territory redesign", "renewal forecasting",
            "duplicate Lead prevention", "partner-sourced pipeline", "multi-currency rollout",
            "sales manager dashboard", "high-volume inbound lead routing",
        ],
    },
    "service-cloud": {
        "title": "Service Cloud",
        "concepts": [
            "Case lifecycle", "assignment rules", "escalation rules", "entitlements",
            "milestones", "Omni-Channel", "queues", "Knowledge", "macros", "quick text",
            "service console", "email-to-case", "web-to-case", "case teams", "SLA reporting",
            "contact center design", "chat", "messaging", "case deflection", "field service handoff",
        ],
        "scenarios": [
            "global support center migration", "SLA breach prevention", "VIP case routing",
            "knowledge-centered support", "refund approval workflow", "agent productivity console",
            "case backlog reduction", "customer portal support",
        ],
    },
    "marketing-cloud": {
        "title": "Marketing Cloud",
        "concepts": [
            "Data Extensions", "Contact Builder", "Journey Builder", "Automation Studio",
            "Email Studio", "Subscriber Key", "Contact Key", "AMPscript", "SQL query activities",
            "send classifications", "preference management", "suppression lists", "API events",
            "CloudPages", "Marketing Cloud Connect", "data retention", "deliverability",
            "personalization", "segmentation", "consent management",
        ],
        "scenarios": [
            "welcome journey", "abandoned cart journey", "patient reminder journey",
            "lead nurture campaign", "renewal campaign", "preference center", "re-engagement campaign",
            "cross-cloud campaign reporting",
        ],
    },
    "health-cloud": {
        "title": "Health Cloud",
        "concepts": [
            "patient data model", "Care Plans", "Care Teams", "clinical encounters",
            "provider relationships", "consent management", "Social Determinants of Health",
            "utilization management", "referrals", "health timelines", "care gaps",
            "PHI security", "FHIR integration", "provider search", "patient engagement",
            "care coordination", "household model", "medical records", "authorization workflows",
        ],
        "scenarios": [
            "patient onboarding", "care-gap closure", "referral management", "appointment scheduling",
            "chronic-care outreach", "payer prior authorization", "provider network management",
            "post-discharge follow-up",
        ],
    },
    "integration": {
        "title": "Integrations",
        "concepts": [
            "REST API", "SOAP API", "Bulk API", "Composite API", "GraphQL API",
            "Named Credentials", "External Credentials", "OAuth", "JWT bearer flow",
            "connected apps", "Platform Events", "Change Data Capture", "Outbound Messages",
            "External Services", "MuleSoft", "idempotency", "retry strategy", "rate limits",
            "API versioning", "error handling", "transaction boundaries", "event replay",
        ],
        "scenarios": [
            "ERP order synchronization", "EHR patient synchronization", "payment status callback",
            "real-time inventory check", "marketing consent sync", "partner API gateway",
            "case event streaming", "large migration using Bulk API",
        ],
    },
    "security": {
        "title": "Security and Sharing",
        "concepts": [
            "profiles", "permission sets", "permission set groups", "role hierarchy",
            "organization-wide defaults", "sharing rules", "manual sharing", "Apex managed sharing",
            "restriction rules", "scoping rules", "CRUD", "field-level security", "Shield encryption",
            "event monitoring", "login policies", "session settings", "OAuth scopes", "CSP",
            "secure Apex", "least privilege", "guest user security", "Experience Cloud sharing",
        ],
        "scenarios": [
            "healthcare PHI access model", "partner portal sharing", "sales territory visibility",
            "support queue visibility", "executive dashboard security", "marketing consent access",
            "field-level masking", "external integration user design",
        ],
    },
    "devops": {
        "title": "DevOps and Release Management",
        "concepts": [
            "Salesforce CLI", "source format", "scratch orgs", "sandboxes", "unlocked packages",
            "managed packages", "change sets", "metadata API", "CI/CD", "static code analysis",
            "Apex tests", "quality gates", "branching strategy", "destructive changes",
            "environment variables", "deployment validation", "rollback plan", "release notes",
            "data seeding", "permission deployment", "post-deploy steps",
        ],
        "scenarios": [
            "enterprise release train", "hotfix deployment", "package-based development",
            "sandbox refresh plan", "multi-team Git workflow", "regulated Health Cloud release",
            "failed deployment recovery", "automated regression test strategy",
        ],
    },
    "data-ldv": {
        "title": "Data, Migration, and Large Data Volumes",
        "concepts": [
            "data modelling", "lookup skew", "ownership skew", "data skew", "skinny tables",
            "selective indexes", "query plan", "archiving", "Big Objects", "Bulk API",
            "external IDs", "upsert", "duplicate management", "data quality", "record locking",
            "sharing recalculation", "batch windows", "migration reconciliation", "backup strategy",
            "data retention", "report performance", "partitioning strategy",
        ],
        "scenarios": [
            "50 million Case migration", "Account ownership skew remediation", "legacy CRM migration",
            "health record import", "marketing history archive", "duplicate cleanup program",
            "global Account hierarchy redesign", "reporting performance incident",
        ],
    },
}


BASIC_PATTERNS = [
    ("What is {concept} in {topic}?", "In {topic}, {concept} is a core capability or design concern that affects how the solution behaves at runtime. A strong answer should define it, name where it is configured or coded, and explain the business impact. In interviews, also mention one common mistake and one practical example."),
    ("Why is {concept} important for a Salesforce developer?", "{concept} matters because Salesforce runs on a shared, metadata-driven platform where design choices affect limits, security, maintainability, and user experience. A developer should know when it applies, how to validate it, and how it changes testing or deployment."),
    ("When would you use {concept}?", "Use {concept} when the requirement naturally matches its strengths and when simpler declarative options are not enough. Explain the trigger condition, affected users or data, expected volume, and how you would prove the design works."),
    ("What is a common beginner mistake with {concept}?", "A common mistake is treating {concept} as an isolated feature instead of considering data volume, permissions, lifecycle, and failure handling. A better answer connects the concept to testing, monitoring, and a real business workflow."),
]

INTERMEDIATE_PATTERNS = [
    ("How would you implement {concept} for a {scenario}?", "Start by clarifying the business rule, data model, entry point, and expected transaction volume. Then choose the Salesforce mechanism that best fits {concept}, add validation and security checks, write tests around success and failure paths, and document operational support steps."),
    ("How would you debug a production issue related to {concept} in a {scenario}?", "Check recent deployments, debug logs, user permissions, data shape, automation order, and integration history. Reproduce with a narrow record set, confirm whether the issue is data-specific or systemic, and apply a fix with regression tests and monitoring."),
    ("What test cases would you write for {concept} in a {scenario}?", "Cover the happy path, missing data, permission edge cases, bulk or high-volume inputs, and failure handling. For interview strength, mention test data isolation, assertions on outcomes rather than implementation details, and negative tests."),
    ("How do you decide between declarative configuration and code for {concept}?", "Prefer declarative configuration when it is maintainable, observable, and fits the platform behavior. Use code when the logic needs complex branching, reusable services, external integration, advanced testing seams, or better control over scale and transaction handling."),
]

ADVANCED_PATTERNS = [
    ("Design a scalable approach for {concept} in a {scenario}.", "A scalable design separates orchestration from domain logic, controls transaction size, respects sharing and security, and avoids synchronous bottlenecks. Use async processing, selective queries, idempotent updates, and operational dashboards when volume or reliability requires it."),
    ("What trade-offs would you evaluate before using {concept} in an enterprise org?", "Evaluate admin maintainability, runtime limits, data volume, release complexity, audit needs, and the skill level of the support team. The best answer explains why the selected approach is better than at least one alternative for the given constraints."),
    ("How would you secure {concept} for regulated data?", "Apply least privilege, enforce CRUD and field-level access, limit integration scopes, log sensitive actions, and avoid exposing restricted fields through UI, API, or AI grounding. For regulated data, also address consent, retention, masking, and audit requirements."),
    ("How would you optimize {concept} when the org has large data volumes?", "Use selective filters, indexed fields, async jobs, smaller transaction scopes, archiving, and careful sharing design. Validate with query plans, realistic data volumes, log analysis, and performance tests before production rollout."),
]

EXTREME_PATTERNS = [
    ("An enterprise has repeated failures in {scenario} involving {concept}. What is your incident-response and redesign plan?", "Triage impact first: affected users, data corruption risk, failed transactions, and rollback options. Stabilize with feature flags or narrowed scope, collect logs and replayable examples, identify the architectural cause, then redesign with idempotency, observability, test coverage, and a phased rollout."),
    ("Architect {concept} for a global, multi-cloud Salesforce program supporting a {scenario}.", "Define system boundaries, ownership of master data, security model, integration contracts, release governance, and nonfunctional requirements. The strongest design includes scale assumptions, failure modes, compliance controls, monitoring, and a migration path from the current state."),
    ("How would you challenge a proposed solution that uses {concept} for a {scenario}?", "Ask for evidence: volume numbers, security requirements, operational ownership, failure behavior, and user experience needs. Then compare alternatives objectively and identify where the proposal creates hidden cost, data risk, or release risk."),
    ("Create an interview whiteboard answer for {concept} in a mission-critical {scenario}.", "Start with requirements and constraints, draw the data flow, mark synchronous versus asynchronous steps, call out security enforcement points, and list observability signals. Finish with test strategy, deployment plan, rollback plan, and open questions."),
]


def make_question(topic_key: str, topic: dict[str, object], level: str, number: int, pattern_index: int) -> tuple[str, str]:
    concepts = topic["concepts"]
    scenarios = topic["scenarios"]
    concept = concepts[(number + pattern_index) % len(concepts)]
    scenario = scenarios[(number * 3 + pattern_index) % len(scenarios)]
    patterns = {
        "basic": BASIC_PATTERNS,
        "intermediate": INTERMEDIATE_PATTERNS,
        "advanced": ADVANCED_PATTERNS,
        "extreme": EXTREME_PATTERNS,
    }[level]
    question_template, answer_template = patterns[pattern_index % len(patterns)]
    values = {"topic": topic["title"], "concept": concept, "scenario": scenario}
    return question_template.format(**values), answer_template.format(**values)


def write_topic_file(topic_key: str, topic: dict[str, object]) -> int:
    path = OUT / f"{topic_key}.md"
    count = 0
    lines: list[str] = [
        f"# {topic['title']} Expanded Interview Q&A",
        "",
        "This file contains generated but practical interview questions and model answers.",
        "Use the answers as a baseline, then add project-specific examples from your own experience.",
        "",
    ]
    for level in ["basic", "intermediate", "advanced", "extreme"]:
        lines.append(f"## {level.title()} Questions")
        lines.append("")
        for i in range(1, 51):
            for pattern_index in range(4):
                count += 1
                question, answer = make_question(topic_key, topic, level, i, pattern_index)
                lines.append(f"### Q{count}. {question}")
                lines.append("")
                lines.append(f"**Answer:** {answer}")
                lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
    return count


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    total = 0
    index_lines = [
        "# Expanded Salesforce Interview Question Bank",
        "",
        "This folder contains thousands of question-and-answer pairs from basic to extremely high difficulty.",
        "",
        "| Topic | Questions | File |",
        "| --- | ---: | --- |",
    ]
    for topic_key, topic in TOPICS.items():
        count = write_topic_file(topic_key, topic)
        total += count
        index_lines.append(f"| {topic['title']} | {count} | `{topic_key}.md` |")
    index_lines.extend([
        "",
        f"Total questions and answers: {total}",
        "",
        "Difficulty guide:",
        "",
        "- Basic: definitions, when-to-use, common mistakes.",
        "- Intermediate: implementation, debugging, tests, declarative-vs-code decisions.",
        "- Advanced: scale, security, optimization, enterprise trade-offs.",
        "- Extreme: architecture, incident response, regulated-data, mission-critical design.",
    ])
    (OUT / "README.md").write_text("\n".join(index_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
