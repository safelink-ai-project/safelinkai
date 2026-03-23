def behaviour_analysis(scan):

    threats = []

    if scan.get("password_fields", 0) > 0:
        threats.append("Login form detected")

    if scan.get("scripts", 0) > 15:
        threats.append("High number of scripts")

    if scan.get("forms", 0) > 2:
        threats.append("Multiple forms detected")

    return threats