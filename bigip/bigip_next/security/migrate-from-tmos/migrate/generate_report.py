import csv
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

if __name__ == "__main__":
    import json

    output_file = sys.argv[1]
    deploy_tree = json.loads(sys.argv[2])
    ip_map = json.loads(sys.argv[3])

    generate_csv_report(output_file, deploy_tree, ip_map)
