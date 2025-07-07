from checker import validate_symptoms, calculate_score, assess_risk

def main():
    user_input = input("Enter your symptoms (comma separated): ")
    symptoms = validate_symptoms(user_input)
    score = calculate_score(symptoms)
    risk, recommendation = assess_risk(score, symptoms)

    print("\n--- Diagnosis ---")
    print(f"Symptoms: {', '.join(symptoms)}")
    print(f"Risk Score: {score}")
    print(f"Risk Level: {risk}")
    print(f"Recommendation: {recommendation}")

if __name__ == "__main__":
    main()
