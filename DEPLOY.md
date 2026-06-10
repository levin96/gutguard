# How to Deploy GutGuard (Step-by-Step)

I have prepared the code for a professional deployment using **Netlify**. This will give you a live URL and handle all your waitlist signups automatically.

## Prerequisites
1. A **GitHub** account.
2. A **Netlify** account (Free).

## Step 1: Initialize Git and Push to GitHub
Run these commands in your terminal:

```bash
# Initialize git
git init

# Add all files (the web folder and netlify.toml)
git add web/ netlify.toml

# Commit your changes
git commit -m "Initial GutGuard landing page"

# Create a new repository on GitHub.com and then link it:
# git remote add origin https://github.com/YOUR_USERNAME/gutguard.git
# git branch -M main
# git push -u origin main
```

## Step 2: Connect to Netlify
1. Log in to [Netlify](https://app.netlify.com/).
2. Click **"Add new site"** -> **"Import an existing project"**.
3. Select **GitHub** and find your `gutguard` repository.
4. Netlify will automatically detect the `netlify.toml` file and use the `web` folder.
5. Click **"Deploy site"**.

## Step 3: Verify the Waitlist
1. Once deployed, visit your new URL (e.g., `fancy-restroom-123.netlify.app`).
2. Enter a test email in the waitlist form.
3. You should be redirected to the `/success` page.
4. Check your Netlify Dashboard under **"Forms"** to see your new lead!

## Why Netlify?
- **Fast**: Worldwide CDN ensures the site loads instantly.
- **Form Handling**: No backend required. Netlify captures every email and lets you export them as CSV.
- **PWA Ready**: I've included a `manifest.json`. Users can "Add to Home Screen" on their phones.

---
**Next Goal**: Once you have your URL, go to `GUTGUARD_STRATEGY.md` and start the Reddit outreach!
