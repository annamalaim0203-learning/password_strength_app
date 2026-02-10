def predict_strength(length, upper, lower, digit, special, entropy):
    score = 0

    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1

    score += upper
    score += lower
    score += digit
    score += special

    if entropy >= 60:
        score += 2
    elif entropy >= 40:
        score += 1

    if score >= 8:
        return "Strong"
    elif score >= 5:
        return "Medium"
    else:
        return "Weak"
