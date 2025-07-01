# LeadInsights_AI 
LeadSight AI is a smart B2B lead enrichment tool designed for sales and business development professionals. It enhances lead data with valuable context like company details, LinkedIn URLs, WHOIS data, and scoring logic to help prioritize high-impact opportunities.

## 🔧 Setup Instructions

1. **Clone the repo:**
```bash
git clone https://github.com/yourusername/leadinsights-ai.git
cd leadinsights-ai
Install dependencies:
pip install -r requirements.txt
Run the app:
streamlit run app.py
Dataset:
You can use the provided enriched_sample_dataset.csv to test the functionality.
Features

Upload a CSV of company names and websites.

Enrich with WHOIS and LinkedIn (via Google search logic).

Score leads based on domain match, LinkedIn presence, and recency.

View and filter high-potential leads.

Download enriched & filtered leads.

Live Demo 

Hosted on Hugging Face Spaces: https://huggingface.co/spaces/IMantasha/LeadInsightsAI





---

### walkthrough_report.md

```markdown
# LeadSight AI - Approach Report

## Problem Statement
Sales teams often lack enriched, actionable data to evaluate B2B leads. Manual research is time-consuming, and irrelevant leads waste time and money.

## Our Solution
LeadSight AI streamlines the lead enrichment process using free tools (WHOIS + Google search) to extract high-impact data:
- LinkedIn presence (for professional verification)
- Domain age (for trust factor)
- Website match (to reduce spam or mismatches)

## Data Preprocessing
- Deduplication of records
- Validity checks on URLs and domains
- Google Search used to extract best-guess LinkedIn URLs
- WHOIS lookup done using `whois` package

## Scoring Logic
- +10 points: LinkedIn found
- +5 points: Domain matches company name
- +5 points: Recent domain registration (<5 yrs)

## Output
- Score assigned to each lead
- UI allows filtering by high score
- CSV downloadable with all enriched insights

## Model Used
No ML model used. Rule-based scoring logic + enrichment scripts.

## Evaluation


### 📹 Video Walkthrough

Watch the quick demo here:  
 [Loom Video Walkthrough](https://www.loom.com/share/048786f16dc44f0b978fb53229124d41?t=165)

- Performance tested with 100 leads: avg. enrichment < 1 sec/lead
- Filtered high-priority leads based on score >15
- Compatible with future CRM integrations



