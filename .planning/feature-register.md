# Product feature register

Keep the full vision discoverable while delivering incrementally. This register summarizes [the product vision](../docs/product-vision.md) and [the current scope decision](decisions/20261015T085738Z-3/D002-anchor-problem.md); it is not an implementation checklist or a promise of delivery dates.

| Capability | Current commitment | Details still to decide |
| --- | --- | --- |
| Basic appointment booking | First increment, confirmed by user | Linked-line WhatsApp booking, exclusive expiring holds, staff review confirmed |
| Basic patient profiling | First increment, confirmed by user | Administrative profile and per-appointment intake confirmed; exact fields/identity open |
| Owner/Admin, Doctor, Receptionist, Patient | Owner/Admin added by Q42; operational roles retained | Role-specific permissions, memberships and journeys |
| English, French, Arabic, Spanish UI | Initial language list confirmed | Locale variants, language switching, translation review |
| Beta-user early access | Confirmed rollout stage | Recruitment, beta scope, success measures, exit criteria |
| Availability and calendar management | Medora is initial scheduling source, confirmed | Minimum setup, controls and calendar views |
| Rescheduling and cancellation | Basic cancellation/rescheduling requests in initial beta, confirmed | Immediate verified cancellation and staff notice; keep original while replacement is pending |
| Booking confirmations | Staff approval required after provisional reservation | Authorized staff review and staffed-hours/cutoff policy chosen; numerical settings open; confirmed booking survives visible/retried delivery failure |
| Reminders and notification preferences | Preserved planned capability; sequencing open | Timing, channels, opt-in behavior |
| Short patient intake and structured summaries | Doctor-approved intake, source-labelled profiles and staff corrections confirmed | Exact templates, correction rights, summary depth |
| Pre-consultation briefing and daily overview | Preserved planned capability; sequencing open | First-release breadth, presentation, update timing |
| Functional staff platform | Direct calendar, review-queue and patient-profile views confirmed; AI enhances platform | Detailed navigation and interaction design |
| Doctor/staff conversational assistant | Private staff conversations and optional sharing confirmed | Selected read-only messages to authorized same-practice colleagues confirmed; revocation/details open |
| Patient conversational appointment requests | WhatsApp agent handles booking and appointment inquiries in chat | Additional channels, conversation languages, human handoff |
| Request priority and human review queues | Preserved planned capability; sequencing open | Configured protocols, reviewer availability, escalation |
| Waiting lists and cancellation slot offers | Preserved planned capability; sequencing open | Eligibility and offer/acceptance behavior |
| Practice policies, templates, automation settings | Essential configuration before activation confirmed; optional guided test | Exact settings, ownership delegation and validation details |
| Multiple doctors/clinics and locations | Practice/clinic organization model confirmed; staged delivery | Practice membership, location scheduling, access boundaries |
| Calendar and authorized health-record integrations | Preserved planned capability; sequencing open | Integration scope, operational boundaries |
| Analytics and workload insights | Preserved planned capability; sequencing open | Measures and validated baselines |
| Advanced automation and clinically governed triage | Preserved later vision; no current implementation commitment | Governance, scope and human review requirements |
| Practice-linked communication line | WhatsApp only initially; personal/shared number requirement confirmed | Doctor/group routing confirmed; supported onboarding paths and handoff mechanism open |
| Booking for someone else | Communication contact may differ from patient, confirmed | Multiple-profile handling and authorization details |
| Optional conversational intake | After minimum-data reservation; nonessential answers may be skipped | Exact fields and practice templates |
| Returning-patient convenience | Reuse verified contact-patient details, confirmed | Staff verifies uncertain relationships before existing-record access/changes; exact evidence/corrections open |
| Agent language preference | Reply in user language and remember until changed, confirmed | Speaking-account/contact owner confirmed; uncertain/unsupported language handling open |
| Human takeover | Confirmed capability | Configured default/backup staff, authorized queue and silent context confirmed; transfer/failure details open |
| Per-patient WhatsApp groups | Optional verified extension after baseline one-to-one beta handoff | Configured default staff; invitations, tags and lifecycle details open |
| Practical practice questions | Approved hours/address/fees/preparation answers confirmed | Information maintenance, review and uncertainty handling |
| AI-generated additional translations | User-requested extension capability | Generation, review, publication, fallback behavior |

Safety, privacy, provenance, authorization, and truthful operation reporting remain cross-cutting requirements, as documented in AGENTS.md. No feature is implemented by virtue of appearing here. Update this register as decisions become explicit; preserve the record of changed or rejected scope.
