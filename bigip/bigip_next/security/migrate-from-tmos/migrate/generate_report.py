import csv
import sys
import json

def generate_csv_report(output_file, migrate_apps, migrate_app_prefix):
    headers = ['Old_App_Name', 'New_App_Name', 'Status', 'Old_IP_Address']
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

        for app in migrate_apps['applications']:
            for vs in app['virtual_servers']:
                app_name = vs['name']
                row = {
                    'Old_App_Name': app_name.replace(migrate_app_prefix, '', 1),
                    'New_App_Name': app_name,
                    'Status': vs['status'],
                    'Old_IP_Address': vs['ip_addresses'][0] if vs['ip_addresses'] else ''
                }
                writer.writerow(row)

if __name__ == "__main__":
    output_file = sys.argv[1]
    json_file = sys.argv[2]
    migrate_app_prefix = sys.argv[3]

    with open(json_file, 'r') as file:
        migrate_apps = json.load(file)

    generate_csv_report(output_file, migrate_apps, migrate_app_prefix)