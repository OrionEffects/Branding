# Meta (Instagram & Facebook) API Setup Guide

## Overview

To publish to Instagram for Business and Facebook Page via the Meta Graph API, you need:
- A Meta Business Account
- An Instagram Business Account connected to the Business Account
- A Facebook Page
- An Access Token with proper permissions

## Step 1: Create/Access Meta Business Account

1. Go to [Meta Business Suite](https://business.facebook.com/)
2. Click "Create Account" if you don't have one
3. Fill in business details
4. Verify your business (may take 1-2 days)

## Step 2: Set Up Instagram Business Account

### Option A: Convert Existing Instagram Account
1. Go to Instagram Settings → Account Type and Tools → Switch to Professional Account
2. Select "Business" as your account type
3. Connect to your Meta Business Account

### Option B: Create New Business Account
1. In Meta Business Suite, go to Instagram Accounts
2. Click "Add" → "Create New Instagram Account"
3. Follow the prompts

## Step 3: Connect Instagram to Facebook Page

1. In Meta Business Suite, go to Instagram Accounts
2. Select your Instagram Business Account
3. Go to Settings → Linked Accounts
4. Link to your Facebook Page

## Step 4: Create a Meta App

1. Go to [Meta Developers](https://developers.facebook.com/)
2. Click "My Apps" → "Create App"
3. Choose "Business" as app type
4. Name it: "Orion Effects Social Media"
5. Fill in app details and create

## Step 5: Generate Access Token

### Method 1: Using Meta Graph API Explorer (Easiest for Testing)

1. Go to [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
2. Select your app from the dropdown
3. Next to "Get Token", click dropdown → "Get User Access Token"
4. Check these permissions:
   - `instagram_basic`
   - `instagram_content_publish`
   - `pages_read_engagement`
   - `pages_manage_posts`
   - `pages_manage_metadata`
5. Click "Generate Access Token"
6. Copy the token

### Method 2: Using App Roles (Better for Production)

1. In your Meta App → Settings → Basic
2. Copy your App ID and App Secret
3. Create a System User in Business Settings:
   - Go to Settings → Users → System Users
   - Click "Add"
   - Assign role: Admin
4. Generate access token for system user
5. This token won't expire (recommended)

## Step 6: Get Your Account IDs

### Instagram Business Account ID

1. In Meta Graph API Explorer:
```
GET /me/instagram_business_accounts
```
2. Look for the `id` field in the response
3. Save this as `INSTAGRAM_BUSINESS_ACCOUNT_ID`

### Facebook Page ID

1. In Meta Graph API Explorer:
```
GET /me/accounts
```
2. Find your Facebook Page in the response
3. The `id` field is your `FACEBOOK_PAGE_ID`

## Step 7: Grant Permissions to Access Token

For your access token to work, it needs these permissions:

**For Instagram:**
- `instagram_business_content_publish` - Publish to Instagram
- `instagram_basic` - Read basic info

**For Facebook:**
- `pages_manage_posts` - Publish posts
- `pages_read_engagement` - Read page metrics

To add permissions:
1. Go to your Meta App → Roles → Admin Roles
2. Add your user with these permissions
3. Regenerate the access token with these scopes

## Step 8: Test Your Tokens

### Test Instagram Token
```bash
curl -X GET "https://graph.instagram.com/YOUR_INSTAGRAM_ID?access_token=YOUR_TOKEN&fields=id,username,name"
```

### Test Facebook Token
```bash
curl -X GET "https://graph.facebook.com/YOUR_PAGE_ID?access_token=YOUR_TOKEN&fields=id,name,category"
```

Both should return your account info.

## GitHub Secrets to Add

```
INSTAGRAM_ACCESS_TOKEN = [long-access-token]
INSTAGRAM_BUSINESS_ACCOUNT_ID = [numeric-id]
FACEBOOK_ACCESS_TOKEN = [long-access-token]
FACEBOOK_PAGE_ID = [numeric-id]
```

## Important Notes

⚠️ **Token Expiration**
- User Access Tokens expire after ~60 days
- System User tokens don't expire (recommended)
- To refresh: regenerate in Meta App settings

⚠️ **Permissions**
- Ensure your token has all required permissions
- If API calls fail with "permission" errors, check token scope

⚠️ **Image URLs**
- Instagram and Facebook need publicly accessible image URLs
- Store generated images in:
  - Google Cloud Storage
  - AWS S3
  - Cloudinary
  - Imgur
  - Any public CDN

📌 **Best Practice**
- Use System User tokens for automation
- Store tokens in GitHub Secrets (never commit them)
- Rotate tokens monthly
- Monitor API usage in Meta App Dashboard

## Troubleshooting

| Error | Solution |
|-------|----------|
| `Invalid OAuth access token` | Token expired or has wrong permissions |
| `Must provide media_id or image_url` | Image URL not provided or not accessible |
| `User does not have permission to post` | Token lacks `pages_manage_posts` permission |
| `The resource does not exist` | Wrong account ID or page ID |

## Resources

- [Meta Graph API Docs](https://developers.facebook.com/docs/graph-api/)
- [Instagram Graph API](https://developers.facebook.com/docs/instagram-api)
- [Facebook Pages API](https://developers.facebook.com/docs/facebook-login/access-tokens)
- [Permissions Reference](https://developers.facebook.com/docs/permissions)
