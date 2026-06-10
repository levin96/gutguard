---
name: gold-miner
description: Automates the "Gold Mining" framework to identify, validate, and develop high-potential product concepts using community data (Reddit) and AI synthesis. Use when a user wants to find a "million dollar idea" or explore market pain points.
---

# Gold Miner Skill

This skill implements the 5-step "Gold Mining" methodology for finding and validating product ideas autonomously.

## The Gold Mining Workflow

### Step 1: Find a Market
Identify a broad, high-demand market (e.g., Health, Wealth, Relationships, SaaS, Productivity).
- **Action**: Brainstorm or ask the user for a starting market.

### Step 2: Validate the Market (Reddit Search)
Find specific communities where people discuss frustrations.
- **Action**: Use `google_web_search` with site-specific queries.
- **Reference**: See `references/reddit_analysis_guide.md` for search patterns.

### Step 3: Gather Data
Collect qualitative data from community discussions.
- **Action**: Use `web_fetch` on high-relevance Reddit threads identified in Step 2.
- **Goal**: Identify recurring complaints, "unmet needs," and strong emotional triggers.

### Step 4: Process Data (Synthesis)
Turn raw frustrations into actionable product concepts.
- **Action**: Synthesize the gathered data using the inversion technique.
- **Reference**: See `references/synthesis_framework.md` for the synthesis template and output structure.

### Step 5: Generate Landing Page
Create a testing artifact for the top concept.
- **Action**: Use `write_file` to generate a landing page using the template.
- **Asset**: Use `assets/landing_page_template/index.html` as the base.

## Guidelines for Autonomous Execution

- **Be Empirical**: Base all product concepts on direct quotes or observed patterns from community data.
- **Be Surgical**: Don't read every thread; focus on those with high comment counts and "how do I" or "sucks" keywords.
- **Deliver Concrete Results**: Each session should end with a prioritized list of concepts and at least one ready-to-use landing page HTML file.

## Expected Output Format

1. **Market Summary**: The sub-niche identified.
2. **The "Gold" (Pain Points)**: Top 3-5 recurring frustrations found.
3. **Product Concepts**: 1-3 synthesized solutions with Name, Pitch, and Magic Moment.
4. **Validation Artifact**: Path to the generated `landing_page.html`.
