import logging
import csv
from datetime import datetime

# Configure the logger to log to a CSV file
log_file = "distance_measurements_nxp.csv"

# Open the CSV file for logging
with open(log_file, "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Timestamp", "Responder", "Distance (cm)"])  # Header row

    # Custom logger configuration
    logger = logging.getLogger("distance_logger")
    logger.setLevel(logging.INFO)

    # Create a handler that writes log messages to the CSV file
    class CsvHandler(logging.Handler):
        def emit(self, record):
            log_entry = self.format(record)
            timestamp, responder, distance = log_entry.split(",")
            csv_writer.writerow([timestamp, responder, float(distance)])

    # Add the custom handler to the logger
    csv_handler = CsvHandler()
    csv_formatter = logging.Formatter('%(asctime)s,%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    csv_handler.setFormatter(csv_formatter)
    logger.addHandler(csv_handler)

    # Example function to simulate logging distances
    def log_distance(responder_index, distance_cm):
        logger.info(f"{responder_index},{distance_cm}")

    # Simulate your NXP distance calculations
    try:
        for i in range(5):  # Replace with actual loop from your main code
            responder_index = i  # Example responder index
            distance_cm = 100 + i * 5  # Example distance calculation
            log_distance(responder_index, distance_cm)
    except KeyboardInterrupt:
        print("Logging stopped.")
