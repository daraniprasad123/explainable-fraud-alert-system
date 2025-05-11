import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

class FraudDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.2, random_state=42)
        self.le_location = LabelEncoder()
        self.le_category = LabelEncoder()

    def preprocess(self, df):
        df['location_enc'] = self.le_location.fit_transform(df['location'])
        df['category_enc'] = self.le_category.fit_transform(df['merchant_category'])
        return df[['time', 'amount', 'location_enc', 'category_enc']]

    def train(self, df):
        X = self.preprocess(df)
        self.model.fit(X)

    def predict(self, df):
        X = self.preprocess(df)
        return self.model.predict(X), self.model.decision_function(X)
