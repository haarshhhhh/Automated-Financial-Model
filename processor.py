# processor.py
import pandas as pd

def process_file(sheets: dict) -> dict:
    """Process raw Excel sheets into structured financial statements and ratios."""
    try:
        # Extract statements from sheets (adjust sheet names if needed)
        income_statement = sheets.get("Profit & Loss", pd.DataFrame())
        balance_sheet = sheets.get("Balance Sheet", pd.DataFrame())
        cash_flow_statement = sheets.get("Cash Flow", pd.DataFrame())

        # Example ratios (replace with actual logic)
        ratios = pd.DataFrame({
            "Metric": ["Net Profit Margin", "ROA", "Debt/Equity"],
            "Value": [0.15, 0.08, 1.2]
        }).set_index("Metric")

        return {
            "income_statement": income_statement,
            "balance_sheet": balance_sheet,
            "cash_flow_statement": cash_flow_statement,
            "ratios": ratios
        }
    except Exception as e:
        return {
            "income_statement": pd.DataFrame(),
            "balance_sheet": pd.DataFrame(),
            "cash_flow_statement": pd.DataFrame(),
            "ratios": pd.DataFrame({"Error": [str(e)]})
        }
