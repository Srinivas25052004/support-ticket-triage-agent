import os
import pandas as pd

from agent import classify_ticket
from utils import save_ticket

RESULT_FILE = "data/results.csv"


def process_single_ticket(subject, body):
    """
    Process one ticket using the AI agent
    and save the result.
    """

    result = classify_ticket(subject, body)

    save_ticket(subject, body, result)

    return result


def process_csv(file):

    df = pd.read_csv(file)

    processed = []

    for _, row in df.iterrows():

        subject = str(row["Subject"])
        body = str(row["Description"])

        result = classify_ticket(subject, body)

        save_ticket(subject, body, result)

        processed.append({
            "Subject": subject,
            "Description": body,
            "Category": result.get("category", ""),
            "Urgency": result.get("urgency", ""),
            "Team": result.get("team", ""),
            "Confidence": result.get("confidence", 0),
            "Sentiment": result.get("sentiment", ""),
            "Summary": result.get("summary", ""),
            "Reason": result.get("reason", ""),
            "Human Review": result.get("needs_human_review", False)
        })

    output = pd.DataFrame(processed)

    output.to_csv(RESULT_FILE, index=False)

    return len(output)


def download_results():

    if os.path.exists(RESULT_FILE):
        return RESULT_FILE

    return None