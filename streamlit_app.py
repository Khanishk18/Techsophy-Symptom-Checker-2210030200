import streamlit as st
from checker import SYMPTOM_SEVERITY, CRITICAL_SYMPTOMS, calculate_score, assess_risk

st.set_page_config(page_title="🩺 Medical Symptom Checker", layout="centered")

# --- Header ---
st.markdown("""
            <h1 style="text-align: center; color: #4B9CD3; font-size: 38px; font-weight: bold;">
    🩺 Symptom Checker &nbsp;&amp;&nbsp; Triage System
</h1>
    <p style="text-align: center; font-size: 16px;">Select symptoms you're experiencing to receive a preliminary risk assessment and care recommendation.</p>
    <hr>
""", unsafe_allow_html=True)

# --- Symptom Groups (categorized) ---
symptom_groups = {
    "🧍 General Symptoms": ["fever", "cough", "fatigue", "headache", "sore throat"],
    "❤️ Severe Symptoms": ["chest pain", "shortness of breath"],
    "🤢 Gastrointestinal": ["vomiting", "diarrhea"]
}

selected_symptoms = []

# --- Display Checkboxes ---
st.subheader("🔘 Select Your Symptoms")
for group, symptoms in symptom_groups.items():
    with st.expander(group, expanded=True):
        for symptom in symptoms:
            if st.checkbox(symptom.title()):
                selected_symptoms.append(symptom)

# --- Assess Button ---
if st.button("🩺 Assess Risk"):
    if not selected_symptoms:
        st.warning("⚠️ Please select at least one symptom.")
    else:
        score = calculate_score(selected_symptoms)
        risk, recommendation = assess_risk(score, selected_symptoms)

        # --- Risk Color Styling ---
        risk_colors = {
            "Low": "#D4EDDA",
            "Medium": "#FFF3CD",
            "High": "#F8D7DA"
        }

        st.markdown(f"""
        <div style="background-color:{risk_colors[risk]}; padding:20px; border-radius:10px;">
            <h3>📝 Summary</h3>
            <p><strong>Symptoms:</strong> {', '.join([s.title() for s in selected_symptoms])}</p>
            <p><strong>Risk Score:</strong> {score}</p>
            <p><strong>Risk Level:</strong> <span style="color: black;">{risk}</span></p>
            <p><strong>Recommendation:</strong> {recommendation}</p>
        </div>
        """, unsafe_allow_html=True)
