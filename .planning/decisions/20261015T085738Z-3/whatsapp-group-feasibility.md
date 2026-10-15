# WhatsApp group feasibility — product evidence

Checked 2026-10-15T14:38:24Z. This is a product-feasibility check, not a stack decision or a working integration. Findings were read from official Meta documentation; direct `.md` representations were used when browser requests failed.

## Verified facts

- Meta restricts automated groups to Official Business Accounts. Its overview lists eight participants, 10,000 groups per business number, and one Cloud API business per group. Business app numbers and Multi-solution Conversations numbers are excluded. The participant list cannot be hidden. [Official overview](https://developers.facebook.com/documentation/business-messaging/whatsapp/groups)
- Participants choose to join using an invitation; the API cannot add them directly. [Group management](https://developers.facebook.com/documentation/business-messaging/whatsapp/groups/reference)
- Incoming group messages identify the group and sender. [Group messaging](https://developers.facebook.com/documentation/business-messaging/whatsapp/groups/groups-messaging)

## Implications and uncertainties

The assistant infers that an eligible integration could retain conversation context while suppressing automatic replies. That is application behavior, not a verified built-in agent feature. Native tag/mention detection has not been verified in the reviewed references; the absence of an example does not prove impossibility.

Ordinary staff joining as invited WhatsApp users appears consistent with the invitation model, but staff-specific behavior was not separately verified. No interpretation of whether the business counts within the eight-participant cap is asserted.

An automatic group cannot be assumed for every personally used/shared linked number. The assistant recommends an optional group flow for eligible practices with opt-in participants and a one-to-one handoff fallback. These recommendations await the user decision in D022. Group membership, disclosure, lifecycle, tags, and authorized updates need explicit product rules.

## Sources

Each fact above links to its source. Recheck current official requirements during integration planning; no credentials, messages, groups, or external account state were changed.
