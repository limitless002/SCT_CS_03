import re

def assess_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    # Strength rating
    if score == 5:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def main():
    print("🔐 Password Strength Checker")
    password = input("Enter your password: ")
    strength, suggestions = assess_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if suggestions:
        print("Suggestions to improve your password:")
        for tip in suggestions:
            print(f" - {tip}")
    else:
        print("Your password is strong. Great job!")

if __name__ == "__main__":
    main()
