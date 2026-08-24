# Orion Effects LinkedIn Publishing Workflow V1

## Purpose

A human-supervised LinkedIn content system. AI and automation prepare content; a human controls the final public action.

## Source of truth

Google Sheet: **Content creation master file**
Tab: **Content Strategy Orion Effects**

Current columns:

| Column | Field |
|---|---|
| A | Post # |
| B | Content Pillar |
| C | Topic |
| D | Marketing Objective |
| E | Caption |
| F | Image Prompt |
| G | CTA |
| H | Status |

## Status model

`Planned → READY FOR FIRST POST → IN REVIEW → READY TO PUBLISH → PUBLISHED`

A rejected item returns to `Planned` or is revised before being marked ready again.

## Operating flow

```text
GOOGLE SHEET
Content Strategy Orion Effects
        |
        | Status = READY FOR FIRST POST
        v
CONTENT PREPARATION
Caption + CTA + Image Prompt
        |
        v
GITHUB ISSUE
Human Review Centre
        |
        +-- /reject --> REVISION REQUIRED
        |
        +-- /approve --> READY TO PUBLISH
                              |
                              v
                       HUMAN LINKEDIN POST
                              |
                              v
                         /published
                              |
                              v
                     ISSUE CLOSED / PUBLISHED
```

## Input

The Google Sheet is the management-facing input queue. A row becomes eligible when its status is changed to `READY FOR FIRST POST`.

## Review output

GitHub Issues are the human review queue. Each issue should contain the topic, caption, CTA, image direction or creative, and review checklist.

Commands:

* `/approve` — mark ready for manual LinkedIn publishing
* `/reject` — send back for revision
* `/published` — confirm the human published it and close the issue

## Public output

The final public output is the post on the Orion Effects LinkedIn Company Page. V1 intentionally keeps this step manual. No Orion Effects mailbox or LinkedIn API credential is required for this stage.

## Technical audit

GitHub Actions is the engine-room audit trail. It is for troubleshooting and workflow history, not the normal business dashboard.

## Daily operator view

Normal operation should require only three places:

1. Google Sheet — content calendar and status
2. GitHub Issues — review and approval
3. LinkedIn — final manual publishing

## V1 safety rule

No content is considered approved for external publishing until a human explicitly approves it. No test content should be posted externally.
