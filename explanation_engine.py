def explain_transaction(row):
    explanation = []

    if row['amount'] > 3000:
        explanation.append("💰 Unusually high transaction amount.")

    if row['location'] not in ['Chennai', 'Bangalore']:
        explanation.append(f"📍 Unusual transaction location: {row['location']}.")

    if row['time'] < 6 or row['time'] > 21:
        explanation.append("⏰ Transaction occurred at an odd time.")

    if not explanation:
        explanation.append("⚠️ Pattern doesn't match your usual behavior.")

    return " ".join(explanation)

def generate_risk_score():
    import random
    return round(random.uniform(0.7, 0.99), 2)
