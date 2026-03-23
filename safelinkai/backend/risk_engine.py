def calculate_risk(ai_result, heuristic_score, threats):

    score = heuristic_score

    if ai_result == 1:
        score += 50

    score += len(threats) * 10

    if score > 100:
        score = 100

    if score <= 30:
        status = "SAFE"

    elif score <= 60:
        status = "SUSPICIOUS"

    else:
        status = "DANGEROUS"

    return score, status