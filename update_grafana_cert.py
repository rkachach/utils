import json
import sys
import os

def update_json(entry_type, json_file, host_name, cert):
    # Load existing data or create a new dictionary
    if os.path.exists(json_file):
        with open(json_file, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}

    # Add or update the entry for the given host_name
    # and save the updated data back to the file
    data[host_name] = {
        entry_type: cert,
        "user_made": True
    }
    with open(json_file, 'w') as f:
        f.write(json.dumps(data))
    print(f"Updated JSON saved to {json_file}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python update_ceph_json.py <cert|key> <hostname> <certificate_file> <output_json_file>")
        sys.exit(1)

    entry_type = sys.argv[1]
    hostname = sys.argv[2]
    cert_file = sys.argv[3]
    json_file = sys.argv[4]
    # Read the certificate content
    with open(cert_file, 'r') as f:
        certificate = f.read()
    # Update the JSON
    update_json(entry_type, json_file, hostname, certificate)
