import json
from datetime import datetime

class Reporter:

    def save_report(self, report_data, filename="report.json"):
        """
        Saves a summary report of detected and corrected issues
        into a JSON file with a timestamp.
        """

        report_data["generated_at"] = str(datetime.now())

        with open(filename, "w") as f:
            json.dump(report_data, f, indent=4)

        print(f"Report saved to: {filename}")
