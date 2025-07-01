# LeadInsights_AI – Project Report

##  Challenge Overview

Caprae Capital’s AI-Readiness Challenge asked participants to analyze and enhance the lead generation process shown in [SaasquatchLeads](https://www.saasquatchleads.com/) and create a value-driven tool in under 5 hours. The goal was to focus on practical AI application and demonstrate how intelligent tools can help identify, enrich, and prioritize high-value leads.

---

##  Objective

The aim was to build a lightweight, accurate, and user-friendly tool that enriches company domain data with actionable insights — without using external APIs, scraping, or sensitive integrations — in a way that aligns with Caprae's value creation thesis in post-acquisition SaaS and M&A environments.

---

##  Approach

###  Key Design Decisions:

- **No API keys, No scraping**: To ensure compliance, simplicity, and replicability, the tool relies on WHOIS data for enrichment.
- **Streamlit Web App**: A simple, intuitive UI that allows users to upload CSVs, enrich leads, view results, and download them—all in a few clicks.
- **Data Enrichment Focus**: WHOIS data provides critical fields like company email, organization, country, and registration details.
- **Lead Scoring Logic**: Custom logic assigns a score (0–100) based on completeness of email, org, and other enrichment fields to prioritize outreach.
- **Download & Export**: Clean export of enriched leads to CSV, supporting smooth integration into downstream sales workflows.

---

##  Technical Summary

- **Frontend**: Streamlit for UI
- **Backend**: Python with `python-whois` for domain parsing
- **Modules**:
  - `enrich.py`: Handles domain enrichment with robust error handling
  - `utils.py`: Contains scoring logic based on data presence and quality
  - `app.py`: Orchestrates the full app using Streamlit
- **Data Output**:
  - Domain
  - Email
  - Organization
  - Country
  - LinkedIn (placeholder: "Not searched")
  - Lead Score

---

##  Business Alignment

This tool reflects Caprae's philosophy of driving post-acquisition value by equipping sales and operations teams with intelligent, no-friction tools. It prioritizes:
- High-impact data for outreach
- Zero reliance on costly APIs
- User empathy through a no-code interface
- Fast turnaround with focused enrichment

---

##  Result

Within 5 hours, a fully functional tool was developed that:
- Takes raw domain data
- Enriches it with high-value insights
- Scores and filters for sales readiness
- Enables CSV export with minimal user effort

---

##  Demo

Loom Video Walkthrough: [Watch here](https://www.loom.com/share/048786f16dc44f0b978fb53229124d41?t=165)

---

##  Repository

GitHub Link: [LeadInsights_AI](https://github.com/imantasha/LeadInsights_AI)

