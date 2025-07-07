# Techsophy-Symptom-Checker-2210030200
# 🩺 Medical Symptom Checker & Triage System

This is an AI-powered Medical Symptom Checker built using a rule-based logic system. It allows users to input symptoms and receive a **preliminary risk score** and **care recommendation**. The system is accessible via both **command-line interface** and a **user-friendly web interface** built with Streamlit.

---

## 📊 Project Overview

- **Core Logic**: Implemented in Python using a rule-based classifier (`checker.py`)
- **Terminal Interface**: CLI-based symptom input and diagnosis (`main.py`)
- **Web UI**: Built with Streamlit for checkbox-based interaction (`streamlit_app.py`)
- **Scoring Model**: Symptoms are assigned severity values and assessed accordingly
- **Design**: Clean and simple UX for both technical and non-technical users

---

## ✅ Features

- Rule-based AI system using symptom severity scores
- Critical symptom override for urgent cases (e.g., chest pain → High risk)
- Handles:
  - Multiple symptoms
  - Duplicates
  - Unknown or invalid entries
- Dual input modes: terminal or web-based UI
- Modular and testable code structure

---

## 🧪 How to Use

### 🔹 Option 1: Run in Terminal

1. Open terminal in your project folder  
2. Run the following command: python main.py
3. Enter symptoms when prompted (comma-separated):

  Enter your symptoms (comma separated): fever, chest pain

4. You'll receive output like:
--- Diagnosis ---
Symptoms: fever, chest pain
Risk Score: 6
Risk Level: High
Recommendation: Seek emergency care


---

### 🔹 Option 2: Run Web UI (Streamlit)

1. Install Streamlit: pip install streamlit
2. Launch the web app: streamlit run streamlit_app.py

3. In the browser:
   - Select your symptoms via checkboxes
   - Click "Assess Risk"
   - Instantly see the risk level and care recommendation

---

## 📁 Project Structure
📦 symptom-checker/
├── checker.py # Core logic (risk scoring, validation, recommendation)
├── main.py # Terminal interface for symptom input
├── requirements.txt # Required Python packages
├── streamlit_app.py # Streamlit UI app
├── test_cases.py # Sample test case script 


---

## 📈 Sample Outputs

| Symptoms                  | Score | Risk   | Recommendation            |
|---------------------------|-------|--------|----------------------------|
| fever, cough              | 3     | Medium | Visit a doctor soon        |
| chest pain                | 4     | High   | Seek emergency care        |
| headache, fatigue         | 2     | Low    | Self-care at home          |
| vomiting, diarrhea, fever | 6     | High   | Seek emergency care        |

---

## 🧠 Skills Demonstrated

- AI/ML logic via rule-based decision scoring
- Critical thinking to differentiate between urgent and mild symptoms
- Problem-solving for handling ambiguous inputs and edge cases
- Modular Python programming with reusable components
- Web app design with interactive UI using Streamlit

---

## 🔄 Future Enhancements

- Add patient details: age, gender, etc.
- Export diagnosis as PDF
- Integrate live medical data or APIs (e.g., WHO/CDC symptom lists)
- Deploy online via Streamlit Cloud

---

## 🏷️ Submission Info

**Project**: Techsophy AI Assessment  
**Submitted by**: Narra Khanishk  
**Roll Number**: 2210030200







