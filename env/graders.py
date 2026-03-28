def grade_response(response: str, expected_keywords: list):
    response = response.lower()
    
    score = 0

    for word in expected_keywords:
        if word in response:
            score += 1

    # reward shaping (important for judges)
    if "sorry" in response:
        score += 0.2
    if "thank" in response:
        score += 0.2

    return min(score / len(expected_keywords), 1.0)