SYMPTOM_SEVERITY = {
    "fever": 2,
    "cough": 1,
    "chest pain": 4,
    "shortness of breath": 3,
    "fatigue": 1,
    "headache": 1,
    "vomiting": 2,
    "sore throat": 1,
    "diarrhea": 2
}

CRITICAL_SYMPTOMS = {"chest pain", "shortness of breath"}

def validate_symptoms(user_input):
    user_symptoms = [sym.strip().lower() for sym in user_input.split(",")]
    known, unknown = [], []

    for sym in user_symptoms:
        if sym in SYMPTOM_SEVERITY:
            known.append(sym)
        else:
            unknown.append(sym)

    if unknown:
        print(f"⚠️ Unknown symptoms ignored: {', '.join(unknown)}")

    # Remove duplicates
    known = list(set(known))

    return known



def calculate_score(symptoms):
    score = 0
    for s in symptoms:
        score += SYMPTOM_SEVERITY.get(s, 0)
    return score

def assess_risk(score, symptoms):
    if any(sym in CRITICAL_SYMPTOMS for sym in symptoms):
        return "High", "Seek emergency care"
    elif score <= 2:
        return "Low", "Self-care at home"
    elif score <= 4:
        return "Medium", "Visit a doctor soon"
    else:
        return "High", "Seek emergency care"
