def chat_display(row, explanation, risk_score):
    print("\n🚨 Fraud Alert 🚨")
    print(f"Time: {row['time']}h | ₹{int(row['amount'])} | {row['location']} | {row['merchant_category']}")
    print("💬 Explanation:", explanation)
    print("🔒 Risk Score:", risk_score)
