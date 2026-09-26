def check_password_strength(password):
    score=0
    has_upper=False
    has_lower=False
    has_digit=False
    has_symbol=False

    for char in password:
        if char.isupper():
            has_upper=True
        elif char.islower():
            has_lower=True
        elif char.isdigit():
            has_digit=True
        elif char in "!@#$%^&*()_-+=,./<>?;'":
            has_symbol=True

    if len(password)>=8:
        score+=1
    if has_upper:
        score+=1
    if has_lower:
        score+=1
    if has_digit:
        score+=1
    if has_symbol:
        score+=1
    return score

def get_password_score(score):
    if score<=1:
        return "Very weak"
    elif score==2:
        return "Weak"
    elif score==3:
        return "Moderate"
    elif score==4:
        return "Strong"
    else:
        return "Very Strong"
def risk_score_analyzer():
    habit_questions={
        "reuse": "Do you use the same password across multiple platforms? (yes/no)",
        "2fa": "Do you use two-factor authentication on your accounts? (yes/no)",
        "public_wifi": "Do you log in to your sensitive accounts over public wifi? (yes/no)",
        "overshare": "Do you post you personal details (example: your birthday, location, or your pet's name) on social media?(yes/no)",
        "update": "Do you update you apps and devices regularly? (yes/no)"
    }

    habit_risk_points={
        "reuse": 2,
        "2fa": 2,
       "public_wifi": 2,
        "overshare": 1,
        "update": 1
    }

    habit_safe_points={
        "reuse": "no",
        "2fa": "yes",
        "public_wifi": "no",
        "overshare": "no",
        "update": "yes"
    }

    risk_score=0
    for key in habit_questions:
        answer=input(habit_questions[key]).lower()
        if answer==habit_safe_points[key]:
            risk_score-=habit_risk_points[key]
        else:
            risk_score+=habit_risk_points[key]

    print(f"\nYour digital footprint risk score: {risk_score}")

    if risk_score<=0:
        print("Low risk")
    elif risk_score<=3:
        print("Moderate risk")
    else:
        print("High risk")