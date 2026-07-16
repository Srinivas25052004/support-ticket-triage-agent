import os
import csv
from datetime import datetime

FILE_NAME = "data/results.csv"


def save_ticket(subject, body, result):

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Timestamp",
                "Subject",
                "Description",
                "Category",
                "Urgency",
                "Team",
                "Confidence",
                "Reason"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            subject,
            body,
            result["category"],
            result["urgency"],
            result["team"],
            result["confidence"],
            result["reason"]
        ])