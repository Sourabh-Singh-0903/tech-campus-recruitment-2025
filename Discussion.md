Approach Used:
 ->The script reads the log file line-by-line instead of loading it all at once.
 ->If a line starts with the target date, it is saved to an output file.
 ->The script downloads and extracts the log file automatically if it is missing.


Steps to run the program:
Make sure Python 3+ is installed. Then, run:
 ->pip install gdown
 ->Navigate to the src/ Directory
 ->Run the Script to extract logs for a specific date (e.g., 2024-12-01), run: python extract_logs.py 2024-12-01
 ->Output Location: Logs for the specified date will be saved in /output/output_YYYY-MM-DD.txt. For example: /output/output_2024-12-01.txt.

