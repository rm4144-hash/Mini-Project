class Correctors:

    def fill_nulls(self, df, defaults):
        """
        Fill NULL or missing values in the DataFrame
        using the default values provided as a dictionary.
        Example: defaults = {"email": "N/A"}
        """
        return df.fillna(defaults)

    def lower_case_email(self, df, col="email"):
        """
        Convert all email values to lowercase
        to maintain data consistency.
        """
        df[col] = df[col].astype(str).str.lower()
        return df
