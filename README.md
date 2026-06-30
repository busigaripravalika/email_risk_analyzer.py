# Email Risk Analyzer

## Description

Email Risk Analyzer is a Python application that scans email content for suspicious patterns and identifies potential phishing or scam emails. It detects urgent phrases, requests for sensitive information, and suspicious links, then assigns a risk score and classifies the email as Low, Medium, or High risk.

## Features

* Detects urgent or suspicious phrases.
* Identifies requests for sensitive information (e.g., passwords, OTPs, credit card details).
* Detects URLs and links in email content.
* Calculates a risk score based on detected threats.
* Classifies emails into Low, Medium, or High risk levels.
* Displays detailed warnings for suspicious content.

## Technologies Used

* Python 3
* Regular Expressions (`re` module)

## Requirements

* Python 3.x

No additional libraries are required.

## How to Run

1. Save the program as `email_risk_analyzer.py`.
2. Open a terminal in the project folder.
3. Run the program:

   ```
   python email_risk_analyzer.py
   ```
4. Paste the email content when prompted and press **Enter**.
5. View the generated risk analysis report.

## Example

### Input

```
URGENT! Verify now using https://fakebank.com and send your password and OTP immediately.
```

### Output

```
===== Email Risk Analysis Report =====
Risk Level: HIGH
Risk Score: 8

Warnings:
- Urgent phrase detected: urgent
- Urgent phrase detected: immediately
- Urgent phrase detected: verify now
- Sensitive information request detected: password
- Sensitive information request detected: otp
- Link(s) detected: https://fakebank.com
```

## Project Structure

```
email_risk_analyzer.py
README.md
```

## Future Enhancements

* Detect suspicious email addresses and domains.
* Analyze email attachments.
* Integrate machine learning for advanced phishing detection.
* Build a graphical user interface (GUI).
* Generate detailed security reports.

## Author

**Pravalika**
