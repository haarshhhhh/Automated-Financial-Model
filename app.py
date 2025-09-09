# app.py
import streamlit as st
import pandas as pd
from processor import process_file
from geminiresponse import get_gemini_response

# GitHub repo details
GITHUB_USER = "haarshhhhh"
REPO_NAME = "Automated-Financial-Model"
BRANCH = "main"
DATA_FOLDER = ""  # if your xlsx are at repo root, leave empty

COMPANY_FILES = {
    "Infosys": "Infosys.xlsx",
    "Reliance Industries": "RelianceIndustr.xlsx",
    "Nestle India": "NestleIndia.xlsx",
    "ITC": "ITC.xlsx",
    "Tata Consumer": "TataConsumer.xlsx",
    "Tata Motors": "TataMotors.xlsx",
    "Tata Power": "TataPower.xlsx",
    "Tata Steel": "TataSteel.xlsx"
}

@st.cache_data
def load_company_excel(file_name: str) -> dict:
    url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/{BRANCH}/{DATA_FOLDER}{file_name}"
    df = pd.read_excel(url, sheet_name="Data Sheet")
    return df

st.set_page_config(page_title="Automated Financial Model", layout="wide")
st.title("📊 Automated Financial Modeling Demo")

company = st.selectbox("🏢 Select a Company", list(COMPANY_FILES.keys()))

if st.button("📂 Load Company Data"):
    file_name = COMPANY_FILES[company]
    try:
        sheets = load_company_excel(file_name)
        st.success(f"✅ Loaded {company} successfully!")

        results = process_file(sheets)

        option = st.sidebar.radio(
            "Choose View:",
            ("Income Statement", "Balance Sheet", "Cash Flow Statement", "Ratio Analysis")
        )

        if option == "Income Statement":
            st.subheader("📑 Income Statement")
            st.dataframe(results["income_statement"])

        elif option == "Balance Sheet":
            st.subheader("📊 Balance Sheet")
            st.dataframe(results["balance_sheet"])

        elif option == "Cash Flow Statement":
            st.subheader("💵 Cash Flow Statement")
            st.dataframe(results["cash_flow_statement"])

        elif option == "Ratio Analysis":
            st.subheader("📈 Ratio Analysis")
            st.dataframe(results["ratios"])
            st.line_chart(results["ratios"].T)

            if st.button("🔮 Get Gemini’s Interpretation"):
                with st.spinner("Asking Gemini..."):
                    response = get_gemini_response(results["ratios"])
                st.success("✅ Gemini’s Response")
                st.write(response)

    except Exception as e:
        st.error(f"❌ Could not process {file_name}. Error: {e}")
