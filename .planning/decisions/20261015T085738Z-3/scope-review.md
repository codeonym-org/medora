# Product foundation — scope review

This is a review draft of confirmed decisions and explicitly open work. It is not final user confirmation, an implementation plan, or a claim of production readiness. The [session index](session.md) links every decision and original reply.

## Platform and people

Medora is a functional practice-management platform enhanced by integrated AI agents. Practices/clinics organize doctors, receptionists and optional locations. A person can have separate practice memberships; records remain practice-scoped. Owner/Admin is an explicit practice account responsibility added in Q42, alongside Doctor, Receptionist and Patient roles. Role combinations and precise permissions are still open.

Staff have usable calendars, request queues, patient profiles and private assistant conversations. Patient booking is natural WhatsApp conversation, without requiring a separate booking UI. Staff can manage operational records directly.

## Initial patient journey

A practice connects a WhatsApp line and configures the doctors it represents. The line may be personally used or shared; supported onboarding modes require verification. The line holder is the communication contact and may book for another patient. Reuse verified returning contact-patient details, and verify uncertain access before disclosing existing information or changing bookings.

The agent checks actual Medora availability, obtains minimum booking information and creates an exclusive provisional reservation. Authorized doctors/receptionists review it. Patient-facing status remains pending until approval and successful execution. A configured staffed-hours budget and pre-appointment cutoff bound the hold; expiry releases the slot and triggers notification.

Patients can make basic rescheduling requests through WhatsApp. Replacement times require agreement; the patient can decline and cancel. Verified cancellation executes immediately and notifies staff. Keeping the original appointment during rescheduling is still awaiting Q45.

## Profiles and conversation

Start with identity/contact details, appointment history, patient-reported visit reasons and short appointment-specific intake. Doctors approve questions and authorized staff may correct source-labelled information. Optional intake follows reservation; missing nonessential replies alone do not block confirmation. Full medical-record management remains outside the initial increment.

The agent answers approved practical practice information and routes uncertain questions to staff. Reply in the speaking user's language, remember the preference until changed, and keep it distinct from the represented patient's profile. Initial staff UI locales are English, French, Arabic and Spanish; future AI-generated translations stay registered.

## Human review and collaboration

A configured default staff member owns handoffs; a backup and shared authorized queue provide coverage. Agent context may update silently while humans converse; replies wait for invocation/control return. A tag alone is not authority for schedule/record changes.

Staff conversations are private. Selected read-only messages can be shared with named authorized same-practice colleagues, respecting record permissions. Optional patient groups are accepted for eligible consenting participants, with a one-to-one fallback; whether they arrive after baseline beta handoff is pending Q46.

## Operations and rollout

Medora is the initial authoritative schedule. External calendar synchronization is later work. Essential configuration precedes booking activation; setup can be saved/resumed and a guided test is optional. Successfully confirmed appointments remain confirmed if a notification fails; delivery state stays distinct, staff see failures and retries follow policy.

Build incrementally while preserving the full feature register. Beta users receive early access before broader advertising. There are no current practitioner validation partners. The beta countries remain explicitly undecided.

## Open decisions for this round

- Q45: preserve the original appointment while a replacement is pending.
- Q46: baseline one-to-one beta handoff before optional group delivery.
- Q47: explicitly defer the detailed topics below to durable focused follow-ups rather than silently finalizing them.

## Proposed focused follow-ups — not yet accepted as deferrals

- **Booking policy detail:** numerical durations/buffers/notice periods, exact hold/cutoff values, replacement-offer expiry and exceptions. Resolve before implementing the affected booking rules.
- **Identity and permissions:** verification evidence, caregiver authorization, role combinations, admin/clinical access boundaries and sharing revocation. Resolve before enabling the relevant access/actions.
- **Communication and handoff:** group invitation/lifecycle, invocation semantics, return-to-agent control, backup reassignment, retry limits and escalation. Resolve before implementing or enabling those flows; integration eligibility stays in the existing technical follow-up.
- **Profile detail:** minimum fields, approved templates, correction/audit presentation and contradictions. Resolve before collecting actual intake.
- **Beta acceptance:** observable workflow/reliability gates, synthetic validation, recruitment, feedback and public-release criteria. Resolve before inviting real beta users; country selection has its own existing follow-up.

All existing clinical-safety, privacy, provenance and truthful-operation constraints continue to apply. No technical stack has been selected and no application is implemented.
