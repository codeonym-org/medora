# Product feature register

Keep the full vision discoverable while delivering incrementally. This register summarizes [the product vision](../docs/product-vision.md) and [the current scope decision](decisions/20261015T085738Z-3/D002-anchor-problem.md); it is not an implementation checklist or a promise of delivery dates.

| Capability | Current commitment | Details still to decide |
| --- | --- | --- |
| Basic appointment booking | First increment, confirmed by user | WhatsApp conversational booking, exclusive expiring reservations and staff review confirmed |
| Basic patient profiling | First increment, confirmed by user | Administrative profile and per-appointment intake confirmed; exact fields/identity open |
| Doctor, Receptionist, Patient roles | Confirmed product roles | Role-specific permissions, memberships and journeys |
| English, French, Arabic, Spanish UI | Initial language list confirmed | Locale variants, language switching, translation review |
| Beta-user early access | Confirmed rollout stage | Recruitment, beta scope, success measures, exit criteria |
| Availability and calendar management | In product vision; needed to support booking | Minimal first-increment controls and calendar views |
| Rescheduling and cancellation | In product vision; release assignment open | Patient agreement to replacement and ability to cancel confirmed; ordinary cancellation details open |
| Booking confirmations | Staff approval required after provisional reservation | Doctor/authorized receptionist review confirmed; working-hours deadline and notification failures open |
| Reminders and notification preferences | Preserved planned capability; sequencing open | Timing, channels, opt-in behavior |
| Short patient intake and structured summaries | In product vision; profiling boundary being clarified | Required/optional fields, attribution, summary depth |
| Pre-consultation briefing and daily overview | Preserved planned capability; sequencing open | First-release breadth, presentation, update timing |
| Doctor/staff conversational assistant | Private staff conversations and optional sharing confirmed | Selected read-only messages to authorized same-practice colleagues confirmed; revocation/details open |
| Patient conversational appointment requests | WhatsApp agent handles booking and appointment inquiries in chat | Additional channels, conversation languages, human handoff |
| Request priority and human review queues | Preserved planned capability; sequencing open | Configured protocols, reviewer availability, escalation |
| Waiting lists and cancellation slot offers | Preserved planned capability; sequencing open | Eligibility and offer/acceptance behavior |
| Practice policies, templates, automation settings | In product vision; needed as workflows require them | Minimum first-increment configuration |
| Multiple doctors/clinics and locations | Practice/clinic organization model confirmed; staged delivery | Practice membership, location scheduling, access boundaries |
| Calendar and authorized health-record integrations | Preserved planned capability; sequencing open | Integration scope, operational boundaries |
| Analytics and workload insights | Preserved planned capability; sequencing open | Measures and validated baselines |
| Advanced automation and clinically governed triage | Preserved later vision; no current implementation commitment | Governance, scope and human review requirements |
| AI-generated additional translations | User-requested extension capability | Generation, review, publication, fallback behavior |

Safety, privacy, provenance, authorization, and truthful operation reporting remain cross-cutting requirements, as documented in AGENTS.md. No feature is implemented by virtue of appearing here. Update this register as decisions become explicit; preserve the record of changed or rejected scope.
