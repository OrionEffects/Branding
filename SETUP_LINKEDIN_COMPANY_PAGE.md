# LinkedIn Company Page Publishing Setup

This workflow publishes one approved post to the Orion Effects LinkedIn Company Page at 09:00 Europe/Lisbon time.

## Required GitHub secrets

Add these repository secrets:

`LINKEDIN_ACCESS_TOKEN`
A LinkedIn OAuth access token authorized to publish for the organization.

`LINKEDIN_ORGANIZATION_URN`
The company page identifier in this format:

`urn:li:organization:YOUR_ORGANIZATION_ID`

## Important permissions

The LinkedIn app and access token must have the currently required LinkedIn permissions/products for organization posting, and the LinkedIn member completing authorization must be an eligible administrator of the Orion Effects page.

Do not store passwords or tokens in repository files.

## Content calendar

Edit `content/linkedin-posts.json`.

A post must contain:

- `id`
- `publish_date` in `YYYY-MM-DD`
- `publish_time` in `HH:MM`
- `status`
- `text`

Only posts with `status` equal to `APPROVED` are eligible.

## Safety rules

- One due approved post maximum per run.
- A post with a stored `linkedin_post_id` cannot be published again.
- Multiple due approved posts cause the workflow to fail rather than guess.
- Publishing status is committed back to the repository after success.

## Testing

Before adding real credentials, use GitHub Actions and run `Publish Approved LinkedIn Company Page Post` manually with `dry_run` enabled.

After adding credentials, create one test post for a future date and mark it `APPROVED` only when you are ready.

## Timezone

The workflow checks every five minutes, but the publisher evaluates the actual current time in `Europe/Lisbon`. This keeps the intended 09:00 Lisbon schedule aligned across Portugal's daylight-saving changes.

## Media

The first version publishes text posts. Image and animated infographic publishing should be added after the text publishing authorization is successfully tested, because LinkedIn media upload uses a separate asset upload flow.
