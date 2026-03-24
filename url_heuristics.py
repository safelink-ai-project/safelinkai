def url_heuristics(url):

    score = 0
    flags = []

    if len(url) > 75:
        score += 10
        flags.append("URL is unusually long")

    if url.count(".") > 4:
        score += 10
        flags.append("Too many subdomains")

    suspicious_keywords = ["login", "verify", "secure", "update", "account"]

    for word in suspicious_keywords:
        if word in url.lower():
            score += 10
            flags.append(f"Suspicious keyword detected: {word}")

    if "@" in url:
        score += 10
        flags.append("URL contains @ symbol")

    return score, flags