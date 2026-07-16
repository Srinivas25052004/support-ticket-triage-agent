import os
import pandas as pd

RESULT_FILE = "data/results.csv"


def get_dashboard_stats():

    stats = {
        "total": 0,
        "high": 0,
        "medium": 0,
        "low": 0,
        "authentication": 0,
        "billing": 0,
        "technical": 0,
        "general": 0,
        "average_confidence": 0
    }

    if not os.path.exists(RESULT_FILE):
        return stats

    try:

        df = pd.read_csv(RESULT_FILE)

        if df.empty:
            return stats

        # Convert all column names to lowercase
        df.columns = df.columns.str.strip().str.lower()

        stats["total"] = len(df)

        if "urgency" in df.columns:
            stats["high"] = len(df[df["urgency"] == "High"])
            stats["medium"] = len(df[df["urgency"] == "Medium"])
            stats["low"] = len(df[df["urgency"] == "Low"])

        if "category" in df.columns:
            stats["authentication"] = len(df[df["category"] == "Authentication"])
            stats["billing"] = len(df[df["category"] == "Billing"])
            stats["technical"] = len(df[df["category"] == "Technical"])
            stats["general"] = len(df[df["category"] == "General"])

        if "confidence" in df.columns:
            stats["average_confidence"] = round(df["confidence"].mean(), 1)

    except Exception as e:
        print("Analytics Error:", e)

    return stats


def get_recent_tickets(limit=10):

    if not os.path.exists(RESULT_FILE):
        return []

    try:

        df = pd.read_csv(RESULT_FILE)

        if df.empty:
            return []

        return df.tail(limit).to_dict(orient="records")

    except Exception:
        return []