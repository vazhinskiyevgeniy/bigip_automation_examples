import csv
import sys

# Function to generate a CSV report
def generate_csv_report(output_file, data):
    headers = ['hostname', 'ip_address']  # Update headers to match the keys in the data
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

if __name__ == "__main__":
    # Assuming that data is passed as a JSON-encoded string in the first argument
    # Ansible can pass data to this script in JSON format
    import json

    data = json.loads(sys.argv[1])
    output_file = sys.argv[2]

    generate_csv_report(output_file, data)
