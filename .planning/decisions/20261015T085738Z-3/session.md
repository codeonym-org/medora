---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3",
  "title": "Medora product functionality and initial scope",
  "status": "active",
  "created_at": "2026-10-15T08:57:38Z",
  "updated_at": "2026-10-15T14:38:24Z",
  "repository": "codeonym-org/medora",
  "issue_number": 3,
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "participants": [
    "user",
    "assistant"
  ],
  "facilitator": "assistant",
  "origin": {
    "conversation_url": null,
    "message_reference": "User message invoking grill-me and requesting durable planning schemas",
    "related_task": "Explore product functionality; persist planning instructions"
  },
  "predecessor_sessions": [],
  "supersedes": [],
  "superseded_by": [],
  "related_follow_ups": [
    ".planning/follow-ups/20261015T102802Z-select-internationalization-and-localization-libraries/follow-up.md",
    ".planning/follow-ups/20261015T110819Z-ai-generated-additional-ui-translations/follow-up.md",
    ".planning/follow-ups/20261015T121349Z-choose-beta-operating-countries/follow-up.md",
    ".planning/follow-ups/20261015T142428Z-validate-whatsapp-linked-line-onboarding/follow-up.md"
  ]
}
---

# Purpose and context

Sharpen Medora's first useful product experience through a recorded interview. The product vision is broad; first-user needs and initial operating assumptions remain unsettled.

## Scope and constraints

In scope: functionality, product ideas, target practices, patient/staff workflows, delegation boundaries, and validation. Out of scope: technical stack selection and application implementation. Existing administrative-role, clinical-safety, privacy, and truthful-confirmation constraints remain in effect.

The user explicitly requested persistent decision and follow-up logs; see [D000](D000-planning-memory-and-scope.md).

## Decision tree

- First practice and daily operator → roles, receptionist collaboration, onboarding, permissions.
- Anchor problem → primary journey, minimum useful scope, observable success.
- Pilot market and languages → communication needs and local operating assumptions.
- Access to practitioners → evidence collection and pilot validation.
- Once these roots are answered: contact channels, existing schedule practices, booking/rescheduling/cancellation rules, human handoff coverage, intake and briefing boundaries, and adoption.

These later branches are candidate questions, not assumed decisions; refine their prerequisites after round 1.

## Decision index and rounds

| ID / link | Round | Question | Predecessors | Status | Outcome |
| --- | --- | --- | --- | --- | --- |
| [D000](D000-planning-memory-and-scope.md) | 0 | Scope and durable records | None | confirmed | Preserve logs; no stack selection |
| [D001](D001-first-practice.md) | 1–3 | Roles and practice grouping | Root | confirmed | Practice organization, three roles, scoped memberships |
| [D002](D002-anchor-problem.md) | 1–2 | Initial scope | Root | confirmed | Preserve vision; basic booking and profiling first |
| [D003](D003-pilot-market.md) | 1–3 | Market and languages | Root | deferred | Four UI languages confirmed; geography deferred |
| [D004](D004-validation-access.md) | 1 | Practitioner access | Root | confirmed | No current access; advertise once working |
| [D005](D005-release-readiness.md) | 2 | Early release | D004 | confirmed | Beta early access |
| [D006](D006-booking-entry.md) | 3–4 | Patient/staff booking entry | D002 | confirmed | WhatsApp conversation is the core patient journey; private staff chat |
| [D007](D007-basic-patient-profile.md) | 3–4 | Basic profile | D002 | confirmed | Administrative profile, appointment history, visit-specific intake |
| [D008](D008-staff-chat-privacy.md) | 4 | Staff conversation visibility | D001, D006 | confirmed | Private by default; user may explicitly share |
| [D009](D009-routine-booking-authority.md) | 4 | Booking confirmation | D001, D002 | confirmed | Reserve provisionally; staff review; notify outcome |
| [D010](D010-provisional-reservation-policy.md) | 5 / Q17 | Holds and expiry | D009 | confirmed | Exclusive holds, configured expiry, notify on release |
| [D011](D011-staff-approval-permissions.md) | 5 / Q18 | Approval roles | D001, D009 | confirmed | Doctor and authorized receptionist approval |
| [D012](D012-conversation-sharing-scope.md) | 5 / Q19 | Sharing scope | D001, D008 | confirmed | Selected read-only messages to authorized same-practice colleagues |
| [D013](D013-replacement-slot-agreement.md) | 5 / Q20 | Replacement-time agreement | D009 | confirmed | Patient accepts replacement or may cancel |
| [D014](D014-review-deadline-outside-working-hours.md) | 6 / Q21 | Requests outside opening hours | D010 | confirmed | Delegated choice: staffed-hours budget capped before appointment |
| [D015](D015-practice-and-doctor-routing.md) | 6 / Q22 | Which practice are they messaging? | D001, D006 | confirmed | Practice-linked WhatsApp line, personal/shared number |
| [D016](D016-booking-for-someone-else.md) | 6 / Q23 | Booking for someone else | D006, D007 | confirmed | Communication contact can book for another patient |
| [D017](D017-optional-conversational-intake.md) | 6 / Q24 | Intake without blocking booking | D007, D009 | confirmed | Reserve with minimum data; optional intake afterwards |
| [D018](D018-linked-line-doctor-routing.md) | 7 / Q25 | Routing a linked line | D001, D015 | confirmed | Doctor/group routing, preserve patient preference |
| [D019](D019-contact-with-multiple-patient-profiles.md) | 7 / Q26 | Returning patients | D007, D016 | confirmed | Reuse verified returning-patient details |
| [D020](D020-patient-conversation-languages.md) | 7 / Q27 | Patient conversation languages | D006, D003 | confirmed | Reply in user language; remember until changed |
| [D021](D021-staff-takeover-of-patient-chat.md) | 7 / Q28 | Human takeover | D006, D011, D015 | confirmed | Human takeover confirmed; group mechanism proposed |
| [D022](D022-optional-patient-group-handoff.md) | 8 / Q29 | Optional groups | D021 | unanswered | Pending |
| [D023](D023-handoff-staff-assignment.md) | 8 / Q30 | Which staff joins? | D001, D011, D021 | unanswered | Pending |
| [D024](D024-agent-context-during-human-handoff.md) | 8 / Q31 | Agent awareness during handoff | D007, D021 | unanswered | Pending |
| [D025](D025-remembered-language-preference-owner.md) | 8 / Q32 | Whose language preference? | D016, D020 | unanswered | Pending |

## Current frontier

Round 8: Q29 (D022 optional groups/fallback), Q30 (D023 responsible staff), Q31 (D024 silent context versus directed-message processing), Q32 (D025 owner of remembered language preference). All prepared and unanswered. Research for group feasibility is complete at the product level; native tag detection remains unverified.

## Unresolved or deferred branches

Group dependence/fallback, responsible handoff staff, agent awareness and preference ownership are current product questions. Group invitation/join/lifecycle details depend on whether the optional group flow is accepted. Exact identity verification, practice-configured intake, patient practical questions, availability rules, failed notifications, beta acceptance, membership/location setup, cancellation details and sharing revocation remain open branches. Country selection and technical integration/provider choices stay in follow-ups.

## Shared understanding

The core patient journey is natural WhatsApp conversation: the agent handles appointment requests and appointment questions directly. A separate patient booking UI is not required. The agent reserves a slot provisionally; staff confirmation/rejection/changes determine the outcome, which the agent communicates. Staff have private management conversations and may explicitly share material; details remain open. Basic profiling includes identity/contact details, appointment history, patient-reported visit reasons, and short appointment-specific intake; full clinical-record features are outside the first increment. The accepted practice model, three roles, English code, EN/FR/AR/ES UI, and beta early access remain. Geography is explicitly deferred.

Round 5 confirms exclusive pending holds with practice-configured expiry and patient notification on release; doctors and authorized receptionists handle routine review. Sharing initially means selected read-only messages to named authorized colleagues in the same practice. A patient must agree to a replacement time and may cancel if it does not fit their schedule. No monetary cancellation policy is inferred.

Round 6: Medora attaches to a practice-linked external communication line, with WhatsApp the only initial app. A number may be personal or shared; account/API compatibility is not assumed. The line holder is the communication contact and may book for someone else. Minimum booking information permits a provisional hold; optional conversational intake follows without blocking staff confirmation. The user delegated Q21: use a staffed-hours review budget capped by a pre-appointment cutoff, releasing/notifying at the earlier limit. Numerical settings remain open.

Round 7 confirms line-to-doctor/group routing and reuse of verified returning-patient details. The agent replies in the user's own language, remembers it until changed, and is not limited to the four UI locales by that instruction. Human takeover is confirmed. A per-patient group with staff and tag-driven awareness is a proposal, not an accepted universal mechanism; account eligibility, invitation limits and unverified native tagging need to be reflected in the design.

## Final user confirmation

Pending. The session is active.

## Related follow-ups and work

Issue: https://github.com/codeonym-org/medora/issues/3. Draft PR: https://github.com/codeonym-org/medora/pull/4.

[Select internationalization/localization libraries later](../../follow-ups/20261015T102802Z-select-internationalization-and-localization-libraries/follow-up.md).

[Feature register](../../feature-register.md). [Additional AI translations](../../follow-ups/20261015T110819Z-ai-generated-additional-ui-translations/follow-up.md).

[Beta operating countries](../../follow-ups/20261015T121349Z-choose-beta-operating-countries/follow-up.md).

[WhatsApp linked-line onboarding research](../../follow-ups/20261015T142428Z-validate-whatsapp-linked-line-onboarding/follow-up.md).

[Official-source WhatsApp group feasibility](whatsapp-group-feasibility.md).

## History

- 2026-10-15T08:57:38Z — Assistant created session, recorded the supplied scope, and prepared round 1.

- 2026-10-15T10:28:02Z — Assistant saved all first-round answers, preserved both Q4 messages, recorded partial decisions, captured the library follow-up, and prepared round 2.

- 2026-10-15T11:08:19Z — Round 2 replies saved verbatim. Initial scope/languages/beta access recorded; organization recommendation and round 3 questions prepared. Full feature register and translation-extension follow-up added.

- 2026-10-15T12:13:49Z — Saved round 3 replies verbatim, confirmed the practice model, clarified accepted channel direction, kept profile scope open, captured geography deferral, and prepared round 4.

- 2026-10-15T13:46:49Z — Recorded round 4 replies, corrected the mistaken patient-UI framing, confirmed profile scope/private staff conversations/staff-reviewed reservations, and prepared round 5.

- 2026-10-15T13:52:30Z — Saved round 5 replies; confirmed expiry, approval, sharing and patient replacement/cancellation choices; prepared round 6.

- 2026-10-15T14:24:28Z — Saved round 6 replies, selected the delegated review-clock policy, clarified linked-line/contact concepts, and prepared round 7; integration feasibility is deferred.

- 2026-10-15T14:38:24Z — Saved round 7 replies, researched the proposed group flow against official documentation, and prepared round 8 without treating tentative group behavior as confirmed.
