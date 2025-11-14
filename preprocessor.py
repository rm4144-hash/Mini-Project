import pandas as pd

class Preprocessor:
    def clean(self, df):
        """
        Perform basic preprocessing such as trimming whitespace
        and standardizing text values.
        """
        # Strip extra spaces in string columns
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].astype(str).str.strip()

        return df
