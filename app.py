import streamlit as st
import pandas as pd
from enrich import enrich_domain_data
from utils import score_leads

st.set_page_config(page_title="LeadSight AI", layout="wide")
st.title("🚀 LeadSight AI - Smart Lead Enrichment")

# Upload CSV file
uploaded_file = st.file_uploader("Upload CSV with domain column", type=["csv"])

# Initialize session state
if "leads_df" not in st.session_state:
    st.session_state["leads_df"] = None

# Handle file upload
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if "domain" not in df.columns:
        st.error("❌ CSV must contain a 'domain' column.")
    else:
        if st.button("🔍 Enrich Leads"):
            enriched = enrich_domain_data(df["domain"].tolist())
            scored = score_leads(enriched)
            st.session_state["leads_df"] = pd.DataFrame(scored)
            st.success("✅ Leads enriched and scored!")

# Always show results if available
if st.session_state["leads_df"] is not None:
    df = st.session_state["leads_df"]
    st.subheader("📊 Enriched and Scored Leads")
    st.dataframe(df)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download All Leads",
        data=csv,
        file_name="enriched_leads.csv",
        mime="text/csv"
    )
