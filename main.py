import pandas as pd
from model import FraudDetector
from explanation_engine import explain_transaction, generate_risk_score
from chatbot_interface import chat_display

# Load dataset
df = pd.read_csv("dataset/sample_transactions.csv")

# Train and predict
fd = FraudDetector()
fd.train(df)
predictions, scores = fd.predict(df)

# Display flagged anomalies
for i, (pred, score) in enumerate(zip(predictions, scores)):
    if pred == -1:
        row = df.iloc[i]
        explanation = explain_transaction(row)
        risk_score = generate_risk_score()
        chat_display(row, explanation, risk_score)
