import sys
import os
import gdown
import zipfile

# Google Drive File ID (Update if needed)
GDRIVE_FILE_ID = "1kQPeECKHD4_x_1f9qKjzCSo0MKvxik_2"

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # src/
LOGS_DIR = os.path.join(BASE_DIR, "../logs")  # Outside src/
OUTPUT_DIR = os.path.join(BASE_DIR, "../output")
ZIP_FILE = os.path.join(BASE_DIR, "../logs.zip")
LOG_FILE = os.path.join(LOGS_DIR, "logs_2024.log")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)


def download_and_extract():
    """Downloads and extracts logs if they are not already present."""
    if os.path.exists(LOG_FILE):
        print(f"Log file already exists at {LOG_FILE}, skipping download.")
        return

    print("Downloading log file from Google Drive... (This may take time)")
    url = f"https://drive.google.com/uc?id={GDRIVE_FILE_ID}"
    gdown.download(url, ZIP_FILE, quiet=False)

    print("Extracting ZIP file...")
    with zipfile.ZipFile(ZIP_FILE, "r") as zip_ref:
        zip_ref.extractall(LOGS_DIR)

    print(f"Log file extracted to '{LOG_FILE}'.")
    os.remove(ZIP_FILE)  # Cleanup zip file


def extract_logs(target_date):
    """Extracts logs for the given date."""
    output_file = os.path.join(OUTPUT_DIR, f"output_{target_date}.txt")

    with open(LOG_FILE, "r", encoding="utf-8") as file, open(output_file, "w", encoding="utf-8") as outfile:
        for line in file:
            if line.startswith(target_date):
                outfile.write(line)

    print(f"Logs for {target_date} saved to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py <YYYY-MM-DD>")
        sys.exit(1)

    target_date = sys.argv[1]

    # Ensure log file exists
    download_and_extract()

    # Extract logs for given date
    extract_logs(target_date)
