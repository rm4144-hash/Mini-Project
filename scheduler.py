import schedule
import time
from cli import run

def job():
    """
    Scheduled job to run the error detection
    and correction process automatically.
    """
    print("Running scheduled database scan...")
    run("sqlite:///sample.db", "customers")
    print("Scan completed.")

# Schedule to run every day at 02:00 AM
schedule.every().day.at("02:00").do(job)

print("Scheduler started. Waiting for the next run...")

while True:
    schedule.run_pending()
    time.sleep(1)
