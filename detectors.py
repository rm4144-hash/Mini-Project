import pandas as pd
from datetime import datetime

class Detectors:

    def detect_nulls(self, df):
        """Return all rows containing NULL or missing values."""
        return df[df.isnull().any(axis=1)]

    def detect_duplicates(self, df, key):
        """Detect duplicate rows based on a given key/column."""
        return df[df.duplicated(key, keep=False)]

    def detect_invalid_emails(self, df, col="email"):
        """Detect email values that are not in valid format."""
        return df[~df[col].str.contains(r".+@.+\..+", na=True)]

    def detect_future_dobs(self, df, col="dob"):
        """Detect date-of-birth values in the future (invalid)."""
        today = datetime.now().date()
        return df[pd.to_datetime(df[col], errors='coerce').dt.date > today]
