# [Organization name]: SOC 2 readiness worksheet

Adapted from SOC 2 Readiness for a One-Person Platform, version 1.1.2 (2026-11-20), jakelawrence.xyz/research/soc2-readiness, licensed CC BY 4.0.

> This is a self-assessment, not an audit. Only an independent CPA firm can issue a SOC 2 report, and this platform has not engaged one. Nothing on this page claims compliance.

Categories in scope: Security, Availability, Confidentiality, Processing integrity, Privacy.

| Ref | Control | Designed (Type I) | Operating (Type II) |
|---|---|---|---|
| CC1.1 | Written standards, enforced | Ready | Ready |
| CC1.3, CC1.4 | Roles, background checks and training | Gap | Gap |
| CC2.1, CC2.2 | A current description of the system | Ready | Partial |
| CC2.3 | Telling users what is happening | Ready | Ready |
| CC3.1, CC3.2 | A risk assessment that repeats | Partial | Gap |
| CC4.1, CC4.2 | Checking that the controls still work | Ready | Partial |
| CC5.2, CC5.3 | Policies deployed as tests | Ready | Ready |
| CC6.1, CC6.3 | Least-privilege access | Ready | Ready |
| CC6.2, CC6.3 | Reviewing who has access | Partial | Gap |
| CC6.1 | Credentials encrypted and accounted for | Ready | Partial |
| CC6.6 | Protecting the edges | Ready | Ready |
| CC6.7 | Encryption in transit | Ready | Ready |
| CC7.1, CC6.8 | Finding vulnerabilities | Gap | Gap |
| CC7.2 | Noticing when something breaks | Ready | Partial |
| CC7.3, CC7.4, CC7.5 | Responding to incidents | Partial | Partial |
| CC8.1 | Every change tested and approved | Partial | Partial |
| CC9.2 | Vendor risk | Partial | Gap |
| A1.2, A1.3 | Backups that restore | Ready | Partial |
| A1.1 | Capacity and cost limits | Ready | Ready |
| C1.1 | Confidential records walled off | Ready | Ready |
| C1.2 | Disposal on a schedule | Partial | Partial |
| PI1.2, PI1.3 | Accurate processing | Ready | Ready |
| P1.1, P2.1 | Notice and choice | Partial | Partial |

## Security

### CC1.1: Written standards, enforced

**The criterion asks:** The organization writes down what it expects of the people who run the system and holds them to it.

**What we do:** [Describe your control. The reference answer: A written list of lines the site never crosses is enforced in code: every outbound channel runs the same check before anything is sent, and a test keeps the written list and the code in step.]

**Open gap:** Nobody signs an acknowledgment of the standards.

**If you are one person:** The only person bound by the standards is the person who wrote them, so an acknowledgment would be a signature on one's own memo.

### CC1.3, CC1.4: Roles, background checks and training

**The criterion asks:** Reporting lines and roles are defined, people with access are screened, and everyone takes security training when hired and every year after.

**What we do:** [Describe your control. The reference answer: None of this exists in a form an auditor could test. There is one person: no org chart, no hiring process, no training record.]

**Open gap:** An org chart, a background check, and a dated training record, even for a company of one.

**If you are one person:** An auditor will still test the one person against these criteria. The fix is paperwork rather than code: a written role, a screening record and an annual training certificate.

### CC2.1, CC2.2: A current description of the system

**The criterion asks:** The organization knows and documents what the system is, where its boundaries are, and who can reach what.

**What we do:** [Describe your control. The reference answer: A written threat model names every kind of actor, what each can reach and what bounds it. A public system map shows the parts and how they connect.]

**Open gap:** The threat model was last verified on July 4, 2026. Nothing schedules the next review.

### CC2.3: Telling users what is happening

**The criterion asks:** Users are told about the system's commitments and about incidents that affect them.

**What we do:** [Describe your control. The reference answer: A public status page reports each component as up, degraded or down, from a health check every three hours, and a privacy page lists what the site stores in a visitor's browser.]

### CC3.1, CC3.2: A risk assessment that repeats

**The criterion asks:** Risks to the system are identified and analyzed, and the assessment is repeated as things change.

**What we do:** [Describe your control. The reference answer: The threat model names its known gaps instead of hiding them, and the one path that merges code without a person has its remaining risk written down and accepted.]

**Open gap:** The assessment was written once. There is no second one to show that it repeats, and no calendar that makes it.

### CC4.1, CC4.2: Checking that the controls still work

**The criterion asks:** The organization evaluates whether its controls are present and functioning, and acts on what it finds.

**What we do:** [Describe your control. The reference answer: Every scheduled job is listed in a catalog that a test keeps in step with the real schedules, and a dashboard sorts each job into fired, failing or silent.]

**Open gap:** The scheduled jobs were all switched off from July 29 to October 8, 2026 to cut the monthly bill, so the dashboard has a gap in its record for that period. They run again now, but a few stay off on purpose.

### CC5.2, CC5.3: Policies deployed as tests

**The criterion asks:** Control activities are put in place through technology and through written policies that people follow.

**What we do:** [Describe your control. The reference answer: Policies here are tests that run on every change: the credential inventory, rate-limit coverage, the boundary around client records, the lines the site never crosses. The build fails if any one of them breaks.]

### CC6.1, CC6.3: Least-privilege access

**The criterion asks:** Access to information and systems is limited to what each person or process needs.

**What we do:** [Describe your control. The reference answer: Access is an ordered ladder: none, view, edit, admin. A member of a shared board sees only that board, and an unknown board and a board you are not on both answer "not found". Automated agents act only through tokens scoped to a grant.]

### CC6.2, CC6.3: Reviewing who has access

**The criterion asks:** Access is granted through a process, removed when it is no longer needed, and reviewed on a schedule.

**What we do:** [Describe your control. The reference answer: Grants are recorded, and every use of an agent's access token is written to an audit log. But nobody reviews the full list of who can reach what on a schedule.]

**Open gap:** A dated, recurring access review with a record of what was removed.

**If you are one person:** The reviewer and the person whose access is being reviewed would be the same person.

### CC6.1: Credentials encrypted and accounted for

**The criterion asks:** Credentials that protect the system are themselves protected.

**What we do:** [Describe your control. The reference answer: Stored credentials are encrypted with AES-256-GCM, changed from an admin screen without a redeploy, and every change is logged. A test fails when code uses a credential the ledger has never heard of.]

**Open gap:** Keys are rotated when someone decides to, not on a calendar.

### CC6.6: Protecting the edges

**The criterion asks:** The system is protected against threats from outside its boundaries.

**What we do:** [Describe your control. The reference answer: Every route that writes data must be rate-limited, gated behind sign-in, verified by a signature, or listed with a written reason. A test fails on any new route that is none of these. Inbound webhooks are checked with a constant-time comparison.]

**Open gap:** The rate limiter keeps a separate count on each server instance, so a caller spread across instances gets more than the limit. The security doc says so.

### CC6.7: Encryption in transit

**The criterion asks:** Information moving between the system and its users is protected.

**What we do:** [Describe your control. The reference answer: Every response tells browsers to use HTTPS only, for two years, subdomains included.]

**Open gap:** There is no full Content Security Policy. The config explains why one was not added blind.

### CC7.1, CC6.8: Finding vulnerabilities

**The criterion asks:** The organization detects new vulnerabilities and unauthorized or malicious software.

**What we do:** [Describe your control. The reference answer: Nothing scans for them. No automated dependency updates or vulnerability scans are configured, and the install step in CI skips npm's own audit.]

**Open gap:** A dependency scanner on every pull request, and a record of what was found and fixed.

### CC7.2: Noticing when something breaks

**The criterion asks:** The system is monitored for anomalies that could mean an attack, an error or an outage.

**What we do:** [Describe your control. The reference answer: Errors go through one reporting function. A watcher compares the live deployment with the latest commit and alerts when production stalls, and it runs off the hosting provider so it still fires during that provider's outage.]

**Open gap:** Both watchers run on schedule, but the health check looks every three hours and the deploy watcher twice a day, so an outage can go unheard for hours. Every alert reaches one person, and nobody else is watching when that person is away.

### CC7.3, CC7.4, CC7.5: Responding to incidents

**The criterion asks:** Incidents are evaluated and contained, then fixed, and the lessons are written down.

**What we do:** [Describe your control. The reference answer: A failed check opens an incident, which moves through one state machine until it is resolved, and alerts page the operator by Telegram.]

**Open gap:** There is no written response plan and no postmortem convention. The security doc names the missing convention as a gap.

### CC8.1: Every change tested and approved

**The criterion asks:** Changes to the system are authorized and designed, then tested and approved, with a record kept, before they reach production.

**What we do:** [Describe your control. The reference answer: Every change lands through a pull request that must pass lint, the full test suite and a build that matches production. One narrow path merges small agent-written fixes without a person, and it fails closed.]

**Open gap:** Nobody but the author approves a change. The one automated reviewer was switched off when its API budget went to zero.

**If you are one person:** Separation of duties needs a second person: whoever writes a change should not be the one who approves it.

### CC9.2: Vendor risk

**The criterion asks:** Risks from vendors and business partners are assessed and managed.

**What we do:** [Describe your control. The reference answer: The credential ledger names every outside service the site holds a key for, so the vendor list is complete and a test keeps it that way.]

**Open gap:** Nobody collects the vendors' own SOC 2 reports or writes down a review of them.

## Availability

### A1.2, A1.3: Backups that restore

**The criterion asks:** Data is backed up, and recovery is tested.

**What we do:** [Describe your control. The reference answer: A weekly job dumps the business-critical tables, encrypts the archive, copies it offsite, then restores it into a scratch database and checks the rows, because a backup that cannot restore is not a backup. A runbook sets recovery targets for each zone. Portfolio OS, the business record, has its own nightly encrypted export and restore test, and records each result.]

**Open gap:** The job was paused from July 29 to October 8, 2026. Since the schedule came back, every weekly restore test has passed, six in a row from October 11 to November 15. A Type II period is usually three months or more, so the record is real but still short.

### A1.1: Capacity and cost limits

**The criterion asks:** Capacity is managed so the system can meet its commitments.

**What we do:** [Describe your control. The reference answer: AI spend is logged on every call, and a brake stops paid calls at the monthly ceiling before a runaway bill can take the service down. Public endpoints are rate-limited.]

## Confidentiality

### C1.1: Confidential records walled off

**The criterion asks:** Confidential information is identified and protected.

**What we do:** [Describe your control. The reference answer: A client's records can be imported only by that client's own module. A test scans the codebase and fails if anything else reaches in, and it also fails if it scanned too few files to mean anything.]

### C1.2: Disposal on a schedule

**The criterion asks:** Confidential information is disposed of when it is no longer needed.

**What we do:** [Describe your control. The reference answer: A written retention policy deletes dinner-guest replies 30 days after the event and retires stale scraped listings, and unclaimed anonymous boards are deleted after 30 days.]

**Open gap:** The mail inbox declares a retention period it does not enforce. The deletion sweeps run again as of October 8, 2026 after a pause since July 29.

## Processing integrity

### PI1.2, PI1.3: Accurate processing

**The criterion asks:** Inputs and processing are complete and accurate.

**What we do:** [Describe your control. The reference answer: Money is stored as whole cents, never as floating-point dollars. Published figures are recomputed on every change. Payment webhooks are accepted only with a valid signature.]

## Privacy

### P1.1, P2.1: Notice and choice

**The criterion asks:** People are told what personal information is collected and are given choices about it.

**What we do:** [Describe your control. The reference answer: A privacy page lists every cookie the site sets. The one optional analytics cookie stays off unless the visitor accepts it.]

**Open gap:** The notice covers the browser. It does not describe the personal information held in the private household and client tools.

## Changes

- 1.1.2 (2026-11-20): All 23 controls re-read against the run history, grades unchanged. Detection: the gap said the health check had stopped, which stopped being true on October 8; the gap now names what still keeps it partial (how long an outage can go unheard, and one person on the receiving end). Backups: six weekly restore tests have passed since the schedule came back (October 11 to November 15), so the gap now counts them instead of saying there are none. The page no longer says a test fails at the review date; that test was retired on October 16.
- 1.1.1 (2026-10-31): All 23 controls re-read, grades unchanged. Health check cadence: the agent tick that runs the site-health sweep moved from hourly to every three hours (an Actions spend cut), so the status page now reads a check up to three hours old; the evidence line follows the workflow.
- 1.1.0 (2026-10-08): All 23 controls regraded after the July 29 schedule freeze was lifted: 43 scheduled jobs run again. Health check regraded to ready; backups and retention sweeps from gap to partial, because a restored schedule is not yet a period of evidence.
- 1.0.0 (2026-09-23): First assessment: 23 controls across all five Trust Services Categories, graded for design and for operation.
