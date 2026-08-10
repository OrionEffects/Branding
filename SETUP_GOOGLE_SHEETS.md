# Google Sheets API Setup Guide

## Step 1: Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click the project dropdown at the top
3. Click "NEW PROJECT"
4. Name it: "Orion Effects Social Media"
5. Click CREATE

## Step 2: Enable Google Sheets API

1. In the Cloud Console, search for "Google Sheets API"
2. Click on it and select "ENABLE"
3. Wait for it to enable (a few seconds)

## Step 3: Enable Google AI / Generative AI API

1. Search for "Generative AI API" or "Vertex AI API"
2. Click ENABLE on both (they're related)
3. Also enable "Google AI Studio API" if available

## Step 4: Create API Key

1. Go to "Credentials" in the left sidebar
2. Click "CREATE CREDENTIALS" → "API Key"
3. A new API key will be created
4. Copy this key - you'll need it for GitHub Secrets

## Step 5: Get Your Google Sheet ID

1. Open your content Google Sheet in Google Sheets
2. Look at the URL: `https://docs.google.com/spreadsheets/d/SHEET_ID/edit`
3. Copy the SHEET_ID part (long string between `/d/` and `/edit`)

## Step 6: Share Sheet with Service Account (Optional but Recommended)

For better security:
1. In Google Cloud Console → Service Accounts
2. Create a new service account
3. Download the JSON key
4. Share your Google Sheet with the service account email
5. Use the JSON key's `private_key` and `client_email` for auth

## GitHub Secrets to Add

Once you have the API key and Sheet ID:

```
GOOGLE_SHEETS_API_KEY = [your-api-key]
GOOGLE_SHEET_ID = [your-sheet-id]
GOOGLE_AI_API_KEY = [your-api-key-for-gemini-and-imagen]
```

**Note:** You can use the same API key for both Google Sheets and Google AI if it has both APIs enabled.

## Test Your Setup

1. Run this in your terminal:
```bash
curl "https://sheets.googleapis.com/v4/spreadsheets/YOUR_SHEET_ID/values/Sheet1?key=YOUR_API_KEY"
```

2. Should return your sheet data as JSON if working correctly
