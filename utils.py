def score_leads(leads):
    for lead in leads:
        score = 0
        if lead.get("email"): score += 40
        if lead.get("organization"): score += 30
        if lead.get("linkedin"): score += 30
        lead["score"] = score
    return leads