from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "certification-coding-bank"


TRACKS = {
    "pd1": {
        "title": "Platform Developer I",
        "areas": ["Apex basics", "triggers", "SOQL", "DML", "testing", "declarative vs code", "data model", "LWC basics"],
        "scenario": "custom business logic on the Lightning Platform",
        "code": "apex",
    },
    "pd2": {
        "title": "Platform Developer II",
        "areas": ["advanced Apex", "async processing", "integration", "large data volumes", "design patterns", "security", "packaging", "performance"],
        "scenario": "enterprise-grade programmatic Salesforce solutions",
        "code": "apex",
    },
    "javascript-developer": {
        "title": "JavaScript Developer I",
        "areas": ["JavaScript fundamentals", "async JavaScript", "DOM", "modules", "testing", "LWC JavaScript", "events", "performance"],
        "scenario": "front-end JavaScript and LWC development",
        "code": "javascript",
    },
    "application-architect": {
        "title": "Application Architect",
        "areas": ["data model", "sharing", "role hierarchy", "declarative architecture", "application lifecycle", "governance", "security", "scalability"],
        "scenario": "scalable Salesforce application architecture",
        "code": "architecture",
    },
    "system-architect": {
        "title": "System Architect",
        "areas": ["integration", "identity", "development lifecycle", "deployment", "data architecture", "security", "performance", "enterprise governance"],
        "scenario": "multi-system enterprise Salesforce architecture",
        "code": "architecture",
    },
    "sales-cloud": {
        "title": "Sales Cloud Consultant",
        "areas": ["lead management", "opportunities", "forecasting", "territories", "campaigns", "quotes", "duplicate management", "pipeline reporting"],
        "scenario": "Sales Cloud implementation and consulting",
        "code": "config",
    },
    "service-cloud": {
        "title": "Service Cloud Consultant",
        "areas": ["case management", "entitlements", "milestones", "Omni-Channel", "Knowledge", "console", "macros", "SLA reporting"],
        "scenario": "Service Cloud support and contact-center implementation",
        "code": "config",
    },
    "health-cloud": {
        "title": "Health Cloud",
        "areas": ["patient 360", "care plans", "care teams", "consent", "clinical data", "FHIR", "PHI security", "referrals"],
        "scenario": "healthcare and life-sciences Salesforce implementation",
        "code": "config",
    },
    "omnistudio-vlocity": {
        "title": "OmniStudio and Vlocity",
        "areas": ["OmniScripts", "FlexCards", "DataRaptors", "Integration Procedures", "calculation matrices", "deployment", "performance", "debugging"],
        "scenario": "industry cloud guided process development",
        "code": "json",
    },
    "flows": {
        "title": "Salesforce Flows",
        "areas": ["record-triggered flows", "screen flows", "subflows", "fault paths", "entry criteria", "flow tests", "invocable Apex", "order of execution"],
        "scenario": "declarative automation design and troubleshooting",
        "code": "flow",
    },
    "agentforce": {
        "title": "Agentforce",
        "areas": ["topics", "actions", "grounding", "handoff", "trust", "testing", "monitoring", "Data Cloud grounding"],
        "scenario": "AI agent design on Salesforce",
        "code": "agent",
    },
    "marketing-cloud": {
        "title": "Marketing Cloud",
        "areas": ["Data Extensions", "Journey Builder", "Automation Studio", "AMPscript", "SQL", "Contact Builder", "deliverability", "consent"],
        "scenario": "multi-channel marketing implementation",
        "code": "sql",
    },
    "data-cloud": {
        "title": "Data Cloud",
        "areas": ["data streams", "DMOs", "identity resolution", "calculated insights", "segments", "activations", "governance", "AI readiness"],
        "scenario": "unified customer profile and activation",
        "code": "sql",
    },
    "integration-architect": {
        "title": "Integration Architect",
        "areas": ["REST", "Bulk API", "Composite API", "Platform Events", "CDC", "OAuth", "MuleSoft", "idempotency"],
        "scenario": "end-to-end Salesforce integration architecture",
        "code": "apex",
    },
    "sharing-visibility": {
        "title": "Sharing and Visibility Architect",
        "areas": ["OWD", "role hierarchy", "sharing rules", "restriction rules", "Apex managed sharing", "Experience Cloud sharing", "FLS", "Shield"],
        "scenario": "secure scalable visibility model",
        "code": "config",
    },
    "app-builder": {
        "title": "Platform App Builder",
        "areas": ["objects", "fields", "relationships", "page layouts", "dynamic forms", "approval processes", "Flow", "reports"],
        "scenario": "declarative application build",
        "code": "config",
    },
}


QUESTION_TYPES = [
    "single-choice style",
    "multi-select style",
    "scenario analysis",
    "troubleshooting",
    "implementation design",
    "coding interview",
    "debug this code",
    "best practice",
    "support incident",
    "architecture review",
]


def code_sample(kind: str, idx: int, area: str) -> str:
    if kind == "apex":
        return f"""```apex
public inherited sharing class InterviewSample{idx} {{
    @AuraEnabled(cacheable=true)
    public static List<Account> findAccounts(String searchKey) {{
        String key = '%' + String.escapeSingleQuotes(searchKey) + '%';
        return [
            SELECT Id, Name, Industry
            FROM Account
            WHERE Name LIKE :key
            ORDER BY Name
            LIMIT 50
        ];
    }}
}}
```"""
    if kind == "javascript":
        return f"""```javascript
export function normalizeRows(rows = []) {{
  return rows
    .filter((row) => row && row.Id)
    .map((row) => ({{ ...row, label: `${{row.Name}} - {area}` }}));
}}
```"""
    if kind == "sql":
        return f"""```sql
SELECT
  SubscriberKey,
  EmailAddress,
  MAX(EventDate) AS LastEngagementDate
FROM Engagement_Events
GROUP BY SubscriberKey, EmailAddress
```"""
    if kind == "json":
        return f"""```json
{{
  "integrationProcedure": "Interview_{idx}",
  "steps": ["ExtractData", "ApplyRules", "ReturnResponse"],
  "topic": "{area}"
}}
```"""
    if kind == "flow":
        return """```text
Start -> Get Records -> Decision -> Update Records
                 |             |
                 |             -> Fault Path -> Create Error Log
                 -> No Records -> End
```"""
    if kind == "agent":
        return f"""```text
Topic: {area} Support
Instruction: Answer only from approved Salesforce data and Knowledge.
Action: Create follow-up task only after user confirmation.
Fallback: Transfer to human when confidence is low.
```"""
    return """```text
Requirement -> Data Model -> Security Model -> Automation -> Integration -> Monitoring
```"""


def answer_for(track: dict[str, object], area: str, qtype: str, idx: int) -> str:
    title = track["title"]
    scenario = track["scenario"]
    base = (
        f"For {title}, the correct approach is to connect {area} to the business requirement, "
        f"the Salesforce data model, security, limits, and operational support. In a {scenario} scenario, "
        "start by clarifying volume, users, permissions, integration boundaries, and failure handling."
    )
    if "coding" in qtype or "debug" in qtype:
        return (
            base
            + " Review the snippet for bulk safety, null handling, security enforcement, naming, testability, "
            "and whether declarative automation would be more maintainable. In an interview, explain both the fix and the trade-off."
        )
    if "single" in qtype or "multi" in qtype:
        return (
            base
            + " Eliminate answers that ignore sharing, governor limits, lifecycle order, or maintainability. "
            "Prefer the option that satisfies the requirement with the least risky standard Salesforce capability."
        )
    if "troubleshooting" in qtype or "support" in qtype:
        return (
            base
            + " For support, inspect recent deployments, debug logs, failed flow interviews, integration logs, "
            "record access, validation rules, and representative data samples before changing metadata."
        )
    if "architecture" in qtype:
        return (
            base
            + " A senior answer covers data ownership, transaction boundaries, sync versus async design, auditability, "
            "release strategy, observability, and rollback."
        )
    return (
        base
        + " A strong implementation answer names the chosen Salesforce feature, why alternatives were rejected, "
        "how it is tested, and how admins or support teams will operate it after go-live."
    )


def write_track(slug: str, track: dict[str, object]) -> int:
    path = OUT / "questions" / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {track['title']} Original Certification-Style Q&A",
        "",
        "These are original practice questions for preparation. They are not copied exam dumps.",
        "",
    ]
    count = 0
    for level in ["Foundation", "Practitioner", "Advanced", "Expert", "Extreme"]:
        lines.extend([f"## {level}", ""])
        for i in range(1, 161):
            area = track["areas"][(i + len(level)) % len(track["areas"])]
            qtype = QUESTION_TYPES[(i + len(slug)) % len(QUESTION_TYPES)]
            count += 1
            lines.append(f"### Q{count}. [{qtype}] How should a Salesforce professional handle {area} for {track['scenario']}?")
            lines.append("")
            if "coding" in qtype or "debug" in qtype or i % 17 == 0:
                lines.append("**Example Code or Configuration Snippet:**")
                lines.append("")
                lines.append(code_sample(track["code"], count, area))
                lines.append("")
            lines.append(f"**Answer:** {answer_for(track, area, qtype, count)}")
            lines.append("")
            lines.append("**Interview Follow-Up:** Describe one risk, one test case, and one monitoring signal for this answer.")
            lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
    return count


def write_code_challenges() -> None:
    folder = OUT / "coding-interview"
    folder.mkdir(parents=True, exist_ok=True)
    challenges = {
        "apex-trigger-bulkification.md": [
            "# Apex Coding Interview: Trigger Bulkification",
            "",
            "Build a trigger and handler that updates Contact risk fields when Account tier changes.",
            "",
            "```apex",
            "trigger AccountTrigger on Account (after update) {",
            "    AccountContactTierService.handleAfterUpdate(Trigger.oldMap, Trigger.newMap);",
            "}",
            "```",
            "",
            "Expected answer: collect Account Ids, query Contacts once, update in one DML call, avoid recursion, and test 200 records.",
        ],
        "lwc-case-triage.md": [
            "# LWC Coding Interview: Case Triage",
            "",
            "Build an LWC that shows urgent cases, supports filters, and lets an agent claim a case.",
            "",
            "```javascript",
            "import { LightningElement, wire } from 'lwc';",
            "import getCases from '@salesforce/apex/CaseTriageController.getCases';",
            "export default class CaseTriage extends LightningElement {",
            "  @wire(getCases) cases;",
            "}",
            "```",
            "",
            "Expected answer: handle loading, error, refreshApex, FLS-safe Apex, pagination, and Jest tests.",
        ],
        "javascript-array-transform.md": [
            "# JavaScript Coding Interview: Transform Salesforce Rows",
            "",
            "Write a function that groups Opportunity rows by StageName and totals Amount.",
            "",
            "```javascript",
            "export function totalByStage(rows) {",
            "  return rows.reduce((acc, row) => {",
            "    const stage = row.StageName || 'Unknown';",
            "    acc[stage] = (acc[stage] || 0) + Number(row.Amount || 0);",
            "    return acc;",
            "  }, {});",
            "}",
            "```",
            "",
            "Expected answer: discuss null handling, numeric conversion, immutability trade-offs, and tests.",
        ],
        "flow-fault-path.md": [
            "# Flow Interview Exercise: Fault Path and Error Logging",
            "",
            "Design a record-triggered Flow that updates related records and logs failures.",
            "",
            "Expected answer: entry criteria, Get Records selectivity, Update Records, fault connector, custom Error Log object, admin alert, and tests.",
        ],
        "omnistudio-ip-design.md": [
            "# OmniStudio Interview Exercise: Integration Procedure Design",
            "",
            "Design an Integration Procedure for eligibility checks.",
            "",
            "Expected answer: DataRaptor Extract, Set Values, conditional remote action, response transform, cache settings, and debug strategy.",
        ],
    }
    for name, lines in challenges.items():
        (folder / name).write_text("\n".join(lines), encoding="utf-8")


def write_diagrams() -> None:
    folder = OUT / "diagrams"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "README.md").write_text(
        "\n".join(
            [
                "# Images and Flowcharts",
                "",
                "These Mermaid diagrams render directly in GitHub Markdown.",
                "",
                "## Salesforce Delivery Lifecycle",
                "",
                "```mermaid",
                "flowchart LR",
                "  Req[Requirement] --> Model[Data Model]",
                "  Model --> Sec[Security and Sharing]",
                "  Sec --> Auto[Flow Apex LWC OmniStudio]",
                "  Auto --> Test[Test Automation]",
                "  Test --> Deploy[CI/CD Deployment]",
                "  Deploy --> Monitor[Monitoring and Support]",
                "  Monitor --> Improve[Backlog Improvements]",
                "```",
                "",
                "## Service Cloud Case Flow",
                "",
                "```mermaid",
                "flowchart TD",
                "  Case[New Case] --> Assign[Assignment Rule]",
                "  Assign --> Omni[Omni-Channel Queue]",
                "  Omni --> Agent[Agent Works Case]",
                "  Agent --> Knowledge[Knowledge Suggestion]",
                "  Agent --> Milestone{SLA Met?}",
                "  Milestone -->|Yes| Close[Close Case]",
                "  Milestone -->|No| Escalate[Escalate and Notify]",
                "```",
                "",
                "## Agentforce Safe Action Pattern",
                "",
                "```mermaid",
                "sequenceDiagram",
                "  participant User",
                "  participant Agent",
                "  participant Grounding as Trusted Grounding",
                "  participant Action as Approved Action",
                "  participant Human as Human Agent",
                "  User->>Agent: Ask for help",
                "  Agent->>Grounding: Retrieve permitted context",
                "  Grounding-->>Agent: Return trusted data",
                "  Agent->>User: Confirm proposed action",
                "  alt User confirms and policy allows",
                "    Agent->>Action: Execute Flow or Apex action",
                "  else Low confidence or restricted data",
                "    Agent->>Human: Handoff with summary",
                "  end",
                "```",
            ]
        ),
        encoding="utf-8",
    )
    (folder / "salesforce-lifecycle.svg").write_text(
        """<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="220" role="img" aria-label="Salesforce lifecycle flowchart">
<rect width="1100" height="220" fill="#f7fbff"/>
<g font-family="Arial" font-size="16" fill="#14324a">
<g fill="#d8ecff" stroke="#2f74b5" stroke-width="2">
<rect x="25" y="75" width="130" height="60" rx="8"/><rect x="185" y="75" width="130" height="60" rx="8"/>
<rect x="345" y="75" width="130" height="60" rx="8"/><rect x="505" y="75" width="130" height="60" rx="8"/>
<rect x="665" y="75" width="130" height="60" rx="8"/><rect x="825" y="75" width="130" height="60" rx="8"/>
</g>
<text x="55" y="110">Requirement</text><text x="220" y="110">Design</text><text x="382" y="110">Build</text>
<text x="547" y="110">Test</text><text x="700" y="110">Deploy</text><text x="855" y="110">Support</text>
<g stroke="#14324a" stroke-width="2" marker-end="url(#arrow)">
<line x1="155" y1="105" x2="185" y2="105"/><line x1="315" y1="105" x2="345" y2="105"/>
<line x1="475" y1="105" x2="505" y2="105"/><line x1="635" y1="105" x2="665" y2="105"/><line x1="795" y1="105" x2="825" y2="105"/>
</g>
</g>
<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#14324a"/></marker></defs>
</svg>""",
        encoding="utf-8",
    )


def write_resources() -> None:
    (OUT / "resources.md").write_text(
        "\n".join(
            [
                "# Salesforce Documentation, Certification, and YouTube Materials",
                "",
                "Use these links for official study. The question bank in this repo is original practice material, not copied exam content.",
                "",
                "## Official Credential Pages",
                "",
                "- Platform Developer I: https://trailhead.salesforce.com/credentials/platformdeveloperi",
                "- Platform Developer II: https://trailhead.salesforce.com/credentials/platformdeveloperii",
                "- JavaScript Developer I: https://trailhead.salesforce.com/credentials/javascriptdeveloperi",
                "- Application Architect: https://trailhead.salesforce.com/credentials/applicationarchitect",
                "- Sales Cloud Consultant: https://trailhead.salesforce.com/credentials/salescloudconsultant",
                "- Service Cloud Consultant: https://trailhead.salesforce.com/credentials/servicecloudconsultant",
                "- OmniStudio Developer: https://trailhead.salesforce.com/credentials/omnistudiodeveloper",
                "- Health Cloud Accredited Professional: https://trailhead.salesforce.com/credentials/healthcloudaccreditedprofessional",
                "",
                "## Official Documentation",
                "",
                "- Apex Developer Guide: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/",
                "- LWC Developer Guide: https://developer.salesforce.com/docs/platform/lwc/guide",
                "- Flow Builder: https://help.salesforce.com/s/articleView?id=sf.flow_builder.htm&type=5",
                "- OmniStudio Help: https://help.salesforce.com/s/articleView?id=sf.os_omnistudio.htm&type=5",
                "- REST API: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/",
                "- SOQL and SOSL: https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/",
                "- Data Cloud: https://help.salesforce.com/s/articleView?id=sf.c360_a_data_cloud.htm&type=5",
                "- Agentforce: https://www.salesforce.com/agentforce/",
                "",
                "## YouTube Study Links",
                "",
                "- Salesforce Developers: https://www.youtube.com/@SalesforceDevelopers",
                "- Trailhead: https://www.youtube.com/@Trailhead",
                "- Apex Hours: https://www.youtube.com/@ApexHours",
                "- Salesforce Admins: https://www.youtube.com/@SalesforceAdmins",
                "- PD1 search: https://www.youtube.com/results?search_query=Salesforce+Platform+Developer+I+certification+study",
                "- PD2 search: https://www.youtube.com/results?search_query=Salesforce+Platform+Developer+II+certification+study",
                "- JavaScript Developer I search: https://www.youtube.com/results?search_query=Salesforce+JavaScript+Developer+I+certification",
                "- Architect search: https://www.youtube.com/results?search_query=Salesforce+Application+Architect+System+Architect+study",
                "- Flow search: https://www.youtube.com/results?search_query=Salesforce+Flow+advanced+tutorial",
                "- OmniStudio search: https://www.youtube.com/results?search_query=Salesforce+OmniStudio+Vlocity+tutorial",
            ]
        ),
        encoding="utf-8",
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    total = 0
    index_lines = [
        "# Certification and Coding Interview Bank",
        "",
        "Original Salesforce certification-style and coding interview practice.",
        "These are not copied certification dumps; they are generated practice prompts with model-answer guidance.",
        "",
        "| Track | Questions | File |",
        "| --- | ---: | --- |",
    ]
    for slug, track in TRACKS.items():
        count = write_track(slug, track)
        total += count
        index_lines.append(f"| {track['title']} | {count} | `questions/{slug}.md` |")
    index_lines.extend(
        [
            "",
            f"Total original questions and answers in this section: {total}",
            "",
            "Also included:",
            "",
            "- `coding-interview/` for hands-on code and configuration prompts.",
            "- `diagrams/` for Mermaid flowcharts and an SVG lifecycle image.",
            "- `resources.md` for official Salesforce documentation, certification pages, and YouTube study links.",
        ]
    )
    (OUT / "README.md").write_text("\n".join(index_lines), encoding="utf-8")
    write_code_challenges()
    write_diagrams()
    write_resources()


if __name__ == "__main__":
    main()
