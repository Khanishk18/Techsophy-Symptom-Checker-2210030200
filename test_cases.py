from checker import validate_symptoms, calculate_score, assess_risk

cases = [
    "fever, cough",
    "chest pain",
    "fatigue, headache",
    "fever, vomiting, diarrhea"
]

for case in cases:
    print(f"\nTest Case: {case}")
    symptoms = validate_symptoms(case)
    score = calculate_score(symptoms)
    risk, recommendation = assess_risk(score, symptoms)
    print(f"Score: {score} | Risk: {risk} | Recommendation: {recommendation}")
