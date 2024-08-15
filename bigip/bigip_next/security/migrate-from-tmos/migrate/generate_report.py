import csv
import json
import sys

def generate_csv_report(output_file, deploy_tree, ip_map):
    headers = ['deploy_tree_key', 'deploy_tree_value', 'ip_map_key', 'ip_map_value']
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

        for deploy_key, deploy_values in deploy_tree.items():
            for deploy_value in deploy_values:
                for ip_key, ip_value in ip_map.items():
                    row = {
                        'deploy_tree_key': deploy_key,
                        'deploy_tree_value': deploy_value['bigip_next'],
                        'ip_map_key': ip_key,
                        'ip_map_value': ip_value
                    }
                    writer.writerow(row)

# def save_cm_apps_json(cm_apps, output_json_file):
#     with open(output_json_file, 'w') as json_file:
#         json.dump(cm_apps, json_file, indent=4)

if __name__ == "__main__":
    output_file = sys.argv[1]
    deploy_tree = json.loads(sys.argv[2])
    ip_map = json.loads(sys.argv[3])
    # cm_apps = json.loads(sys.argv[4]) 
    # output_json_file = sys.argv[5]

    generate_csv_report(output_file, deploy_tree, ip_map)
    # save_cm_apps_json(cm_apps, output_json_file)
