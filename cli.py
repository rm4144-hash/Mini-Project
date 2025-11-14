import pandas as pd
from db_connector import DatabaseConnector
from detectors import Detectors
from correctors import Correctors
from reporter import Reporter
from preprocessor import Preprocessor

def run(db_url, table):
    """
    Main function to execute detection, correction,
    and reporting workflow.
    """

    # Connect to database and load table
    db = DatabaseConnector(db_url)
    df = db.read_table(table)

    # Initialize modules
    pre = Preprocessor()
    det = Detectors()
    corr = Correctors()
    rep = Reporter()

    # Step 1: Preprocess data
    df = pre.clean(df)

    # Step 2: Detect anomalies
    nulls = det.detect_nulls(df)
    duplicates = det.detect_duplicates(df, df.columns[0])
    invalid_emails = det.detect_invalid_emails(df)

    # Step 3: Apply corrections
    df = corr.fill_nulls(df, {"email": "N/A"})
    df = corr.lower_case_email(df)

    # Step 4: Save corrected data back into table
    db.write_table(df, table)

    # Step 5: Generate report
    rep.save_report({
        "null_record_count": len(nulls),
        "duplicate_record_count": len(duplicates),
        "invalid_email_count": len(invalid_emails)
    })

if __name__ == "__main__":
    run("sqlite:///sample.db", "customers")
