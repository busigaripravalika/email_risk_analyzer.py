import re

def analyze_email(email_text):
    risk_score = 0
    warnings = []

    urgent_words = [
        "urgent", "immediately", "asap", "act now",
        "limited time", "verify now", "suspended"
    ]

    sensitive_words = [
        "password", "bank account", "credit card",
        "otp", "ssn", "pin", "login details"
    ]

    links = re.findall(r'https?://\S+|www\.\S+', email_text)

    for word in urgent_words:
        if word.lower() in email_text.lower():
            risk_score += 1
            warnings.append(f"Urgent phrase detected: {word}")

    for word in sensitive_words:
        if word.lower() in email_text.lower():
            risk_score += 2
            warnings.append(f"Sensitive information request detected: {word}")

    if links:
        risk_score += len(links)
        warnings.append(f"Link(s) detected: {', '.join(links)}")

    print("\n===== Email Risk Analysis Report =====")

    if risk_score == 0:
        print("Risk Level: LOW")
    elif risk_score <= 3:
        print("Risk Level: MEDIUM")
    else:
        print("Risk Level: HIGH")

    print(f"Risk Score: {risk_score}")

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print("-", warning)
    else:
        print("No suspicious content detected.")

email_content = input("Paste the email content:\n")
analyze_email(email_content)