
def choose_transport(distance_km, urgency, budget):
    explanation = []

    if urgency == "urgent":
        explanation.append("Urgent travel → fastest option selected (Flight)")
        return "Flight", explanation

    if distance_km <= 300:
        explanation.append("Distance ≤ 300 km → Train selected")
        return "Train", explanation

    if distance_km > 300 and budget >= 5000:
        explanation.append("Distance > 300 km and sufficient budget → Flight selected")
        return "Flight", explanation

    explanation.append("Low budget or long distance → Bus selected")
    return "Bus", explanation


def choose_hotel(role):
    explanation = []

    if role == "intern":
        explanation.append("Intern policy → Max 3-star hotel")
        return "3-star", explanation

    if role == "staff":
        explanation.append("Staff policy → 3-star hotel")
        return "3-star", explanation

    explanation.append("Manager policy → 4-star hotel allowed")
    return "4-star", explanation


# AI appended note: prompt => change the theme keep all same just theme color and   a littlt ui
