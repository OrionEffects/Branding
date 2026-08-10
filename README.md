# Orion Effects Branding

Social media content automation for Orion Effects brand.

## Setup Instructions

This repository contains GitHub Actions workflows for automated daily social media publishing.

### Configuration Required

1. **Google Sheets API**
   - Create a Google Cloud project and enable the Google Sheets API
   - Generate an API key and add it as `GOOGLE_SHEETS_API_KEY` secret
   - Add your spreadsheet ID as `GOOGLE_SHEET_ID` secret

2. **Google AI Studio (Gemini)**
   - Enable the Generative AI API in Google Cloud
   - Create an API key and add it as `GOOGLE_AI_API_KEY` secret

3. **Meta (Instagram & Facebook)**
   - Create a Meta App and get an access token
   - Add `INSTAGRAM_ACCESS_TOKEN` and `INSTAGRAM_BUSINESS_ACCOUNT_ID` secrets
   - Add `FACEBOOK_ACCESS_TOKEN` and `FACEBOOK_PAGE_ID` secrets

### Google Sheets Structure

Your content sheet should have columns:
- A: Status (READY, PUBLISHED, or DRAFT)
- B: Topic
- C: Description
- D: Brand Guidelines
- E: Image Style
- F: Hashtags
- G: Publication Date (auto-filled)

The workflow processes rows marked "READY" daily.
