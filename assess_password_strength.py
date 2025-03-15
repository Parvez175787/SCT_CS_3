import re

def assess_password_strength(password):
    # Criteria for a strong password
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "numbers": bool(re.search(r'[0-9]', password)),
        "special_characters": bool(re.search(r'[\W_]', password)),
    }

    # Calculate the strength score
    strength_score = sum(criteria.values())

    # Determine the password strength based on the score
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Return the assessment result
    result = {
        "password": password,
        "strength": strength,
        "criteria": criteria
    }
    
    return result

# Example usage
password = "P@ssw0rd123"
assessment = assess_password_strength(password)
print(assessment)
