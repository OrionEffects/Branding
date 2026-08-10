# Human-in-Loop Social Media Publishing Workflow

## Overview

This is an **improved, human-supervised workflow** that automates the content pipeline while ensuring quality control and maintaining your brand's voice. Instead of fully automated publishing that might miss critical details, this workflow:

✅ **Automates:** Content fetching, AI strategy, image generation  
✅ **Pauses for Review:** Creates a GitHub Issue for human approval  
✅ **Publishes Only After Approval:** Human confirms before posting  
✅ **Allows Quick Edits:** Change caption, image, or hashtags inline  

---

## Workflow Architecture

### Phase 1: Automated Preparation (2-3 minutes)
```
1. Fetch content from Google Sheets (READY status)
   ↓
2. Generate AI caption + CTA strategy
   ↓
3. Check for image (use provided or generate)
   ↓
4. Create GitHub Issue with preview
   ↓
5. ⏸️ PAUSE - Awaiting Human Review
```

### Phase 2: Human Review & Approval (1-24 hours)
```
⏸️ GitHub Issue created with:
   - Generated caption
   - Call-to-action
   - Hashtags
   - Image preview
   
👤 You review and either:
   ✅ Comment "/approve" to proceed
   ✏️ Request changes inline
   ❌ Comment "/reject" to cancel
```

### Phase 3: Automated Publishing (1-2 minutes after approval)
```
6. Publish to Instagram for Business
   ↓
7. Publish to Facebook Page
   ↓
8. Update Google Sheets (mark PUBLISHED + date)
   ↓
9. Close GitHub Issue with confirmation
```

---

## Key Features

### 1. **Smart Image Handling**
- **Prefer provided images:** If you add an image URL to Google Sheets, it uses that
- **Fallback to generation:** If no image provided, attempts AI generation
- **Manual upload option:** You can always provide a better image in the review

### 2. **Content Approval Checklist**
The GitHub Issue includes:
- [ ] Caption Review
- [ ] CTA Check
- [ ] Hashtags verification
- [ ] Image Quality assessment
- [ ] Image Accessibility check
- [ ] Brand alignment review

### 3. **Quick Edit Capability**
In the GitHub Issue, you can comment:
```
/approve                    # Publish as-is
/reject                     # Cancel and reset to DRAFT

Caption to: "New caption text here"
Image URL: https://example.com/image.png
Hashtags to: #NewTag #AnotherTag
```

### 4. **Timeout Protection**
- Workflow waits max 24 hours for approval
- After 24 hours, content resets to DRAFT
- Prevents accidentally publishing old content

### 5. **Failure Recovery**
- If any step fails, status reverts to DRAFT
- You can fix and re-trigger manually
- No failed posts published

---

## Google Sheets Setup for Human-Loop

### Expected Column Structure

| Col | Header | Example | Notes |
|-----|--------|---------|-------|
| A | Status | READY | DRAFT / READY / PUBLISHED |
| B | Topic | "Summer Sale" | Content subject |
| C | Description | "Announce summer..." | Content brief |
| D | Brand_Guidelines | "Professional, vibrant" | Tone/style |
| E | Image_Style | "3D, glowing" | Image description |
| F | Hashtags | "#OrionEffects #VFX" | Social tags |
| G | Image_URL | https://... | OPTIONAL: Provide your own image |
| H | Notes | "Urgent post" | Additional context for reviewer |
| I | Publication_Date | (auto-filled) | Filled by workflow |

### Example Row
```
Status: READY
Topic: New Effects Pack Launch
Description: Announcing our latest AI-powered effects suite
Brand_Guidelines: Modern, cutting-edge, professional
Image_Style: Sleek 3D rendering with neon accents
Hashtags: #OrionEffects #AIEffects #VideoProduction #CreativeTools
Image_URL: https://cdn.orioneffects.com/effects-pack-hero.png
Notes: High priority - coordinate with email blast
```

---

## Workflow Execution Steps

### Step 1: Daily Trigger (9 AM UTC)
Workflow runs automatically every day at 9 AM UTC (or manually via `workflow_dispatch`)

### Step 2: Fetch Content
```
✅ Scans Google Sheet
✅ Finds first row marked "READY"
✅ Extracts all content fields
✅ Outputs for next steps
```

**What if no READY rows?**
- Workflow exits gracefully
- No error, just skips the day

### Step 3: AI Strategy Generation
```
Input: Topic, Description, Brand Guidelines
↓
Gemini AI generates:
  - Caption (max 150 chars)
  - Hook (catchy intro)
  - CTA (call-to-action)
↓
Output: JSON with all three
```

**Example AI Output:**
```json
{
  "caption": "Introducing Orion Quantum FX - Transform your vision with AI-powered effects. Try free for 30 days.",
  "hook": "✨ Revolutionary effects just dropped",
  "cta": "Start your free trial today →"
}
```

### Step 4: Image Handling
```
IF Google Sheet has Image_URL:
  ✅ Use provided image
  
ELSE IF no URL provided:
  → Attempt AI image generation
     (using Image_Style description)
  
IF generation fails:
  ⚠️ Workflow continues anyway
  → Human can provide image in review
```

### Step 5: Create Review Issue
**Automated GitHub Issue created with:**

```
Title: 📱 Content Review: New Effects Pack Launch

Body includes:
- Topic name
- Generated caption
- Call-to-action
- Hashtags
- Image preview/URL
- Additional notes
- Human approval checklist
- Instructions for approval/changes
```

**Example Issue:**
```
## 📱 Daily Social Media Content Review

Topic: New Effects Pack Launch

### 📝 Generated Caption
✨ Introducing Orion Quantum FX - Transform your vision with AI-powered 
effects. Try free for 30 days.

### 💬 Call to Action
Start your free trial today →

### 🏷️ Hashtags
#OrionEffects #AIEffects #VideoProduction #CreativeTools

### 🖼️ Image
✅ Using provided image: https://cdn.orioneffects.com/effects-pack-hero.png

### 👤 Human Review Checklist
- [ ] Caption Review
- [ ] CTA Check
- [ ] Hashtags
- [ ] Image Quality
- [ ] Image Accessibility
- [ ] Overall Branding

## ✅ Next Steps

IF APPROVED: Comment `/approve`
IF CHANGES: Comment with edits
IF REJECT: Comment `/reject`
```

### Step 6: Human Approves (You!)
**You have 24 hours to review and respond.**

#### Option A: Approve As-Is
```
Comment in GitHub Issue:
/approve
```
✅ Workflow resumes immediately  
✅ Posts to Instagram + Facebook

#### Option B: Request Changes
```
Comment:
Caption to: "Better caption here"
Image URL: https://mycdn.com/better-image.png
Hashtags to: #Tag1 #Tag2

/approve
```
✅ Workflow uses your changes  
✅ Posts to both platforms

#### Option C: Reject & Reset
```
Comment:
/reject
```
❌ Workflow cancels  
❌ Google Sheet resets to DRAFT  
✅ You can edit and re-mark READY tomorrow

### Step 7: Automated Publishing
Once approved:
```
1. Create Instagram media container
2. Upload caption + image
3. Publish to Instagram
4. Publish to Facebook with same content
5. Store Instagram ID + Facebook ID in Google Sheet
```

### Step 8: Update Tracking
```
✅ Google Sheet Status → PUBLISHED
✅ Publication Date → Today's date (auto)
✅ Instagram ID → Stored in column
✅ Facebook ID → Stored in column
```

### Step 9: Close Issue
```
GitHub Issue auto-closes with message:
✅ PUBLISHED - Content successfully posted!
```

---

## Timeline Example

### Day 1: Content Preparation
```
8:00 AM - You add content row to Google Sheet (Status: READY)
9:00 AM - Workflow triggers
9:03 AM - GitHub Issue #42 created: "📱 Content Review: Summer Sale"
```

### Day 1: Human Review
```
10:30 AM - You review issue #42
11:00 AM - You comment: "/approve"
11:02 AM - Workflow resumes, posts to Instagram & Facebook
11:05 AM - Issue closes: "✅ PUBLISHED"
```

### Result
```
✅ Instagram post live
✅ Facebook post live
✅ Google Sheet updated with publication date
✅ Social media IDs stored for reference
```

---

## Error Handling & Recovery

### Scenario 1: AI Generation Fails
```
Status: ⚠️ Image generation failed
Action: Workflow continues, GitHub Issue created
Your Action: Provide image URL in review
Result: Posts with your image
```

### Scenario 2: API Error (Instagram/Facebook)
```
Status: ❌ Publishing failed
Action: Google Sheet status reverts to DRAFT
Your Action: Fix API token, re-mark as READY
Result: Try again tomorrow or manually trigger
```

### Scenario 3: Human Rejects Content
```
Status: ❌ Rejected
Action: Google Sheet status → DRAFT
Your Action: Edit content in sheet, re-mark READY
Result: Reprocesses tomorrow with edits
```

### Scenario 4: 24-Hour Timeout (No Response)
```
Status: ⏸️ Workflow cancelled
Action: Google Sheet status → DRAFT
Your Action: Check GitHub Issue, respond or reprocess
Result: Content saved for re-review
```

---

## Best Practices for Human Reviewers

### ✅ DO:
- Review every morning (~9:05 AM UTC) when issue appears
- Use provided checklist to ensure quality
- Request changes if anything doesn't align with brand
- Provide specific feedback in comments
- Approve quickly to maintain social media consistency

### ❌ DON'T:
- Leave pending longer than 4-8 hours (content gets stale)
- Ignore platform-specific requirements (captions length, hashtag limits)
- Skip the image quality check
- Forget to update notes if scheduling for future reference

### 💡 TIPS:
- Set a calendar reminder for 9 AM UTC daily
- Monitor review issue notifications
- Keep brand guidelines handy for quick reference
- Screenshot approved content for your records
- Review Instagram/Facebook engagement after posting

---

## Customization Options

### Adjust Schedule
Edit `.github/workflows/social-media-publisher-human-loop.yml`:
```yaml
schedule:
  - cron: '0 9 * * *'  # Change 9 to your preferred hour
```

### Extend Approval Timeout
Current: 24 hours  
To change: Modify polling logic in Step 7

### Auto-Approve Certain Content
Add metadata field to auto-approve low-risk content:
```
Auto_Approve: true
```

### Add Slack/Email Notifications
Integrate GitHub → Slack bot to notify on new review issues

---

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Issue not created | API token missing scopes | Check GitHub token permissions |
| Workflow hangs at review | Comment format wrong | Use exact "/approve" syntax |
| Image not showing in issue | Image URL broken | Test URL in browser first |
| Caption too long for Instagram | Character limit | AI generator uses max 150 chars |
| Post doesn't appear for hours | Facebook/Instagram review | Check platform activity logs |

---

## Next Steps

1. ✅ Add workflow file to `.github/workflows/social-media-publisher-human-loop.yml`
2. ✅ Configure all 7 GitHub Secrets (see `SETUP_GITHUB_SECRETS.md`)
3. ✅ Create sample Google Sheet with READY content
4. ✅ Test with `workflow_dispatch` (manual trigger)
5. ✅ Review generated issue and approve
6. ✅ Verify posts appear on Instagram/Facebook
7. ✅ Set daily calendar reminder for review

---

## Summary: Why Human-in-Loop is Better

| Aspect | Fully Automated | Human-in-Loop |
|--------|-----------------|---------------|
| Speed | 5 min total | 5 min + review time |
| Quality Control | None | Full review checklist |
| Brand Safety | Risky | ✅ Verified |
| Edits | Impossible | ✅ Quick changes |
| Image Quality | Hit-or-miss | ✅ Curated |
| Recovery | Publish failed post | ✅ Prevent bad posts |
| Learning | None | Learns from feedback |

**Best of Both Worlds:** Automation handles heavy lifting, humans ensure excellence.

