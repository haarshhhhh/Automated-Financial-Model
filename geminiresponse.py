# geminiresponse.py
import os
import google.generativeai as genai

def get_gemini_response(ratios_df):
    """Send ratios DataFrame to Gemini and return interpretation text."""
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            return "⚠️ Gemini API key not found. Please set GEMINI_API_KEY in environment."

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"Interpret the following financial ratios for an investor:\n\n{ratios_df.to_string()}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating Gemini response: {e}"
