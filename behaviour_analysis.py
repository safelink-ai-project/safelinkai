def behaviour_analysis(scan):

    threats = []

    if scan.get("password_fields", 0) > 0:
        threats.append("Login form detected")

    if scan.get("scripts", 0) > 20:
        threats.append("High number of scripts")

    if scan.get("external_links", 0) > 30:
        threats.append("Too many external links")

    if scan.get("forms", 0) > 2:
        threats.append("Multiple forms detected")

    return threats
