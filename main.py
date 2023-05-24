import json
import os

def main():

    filename = input("Please provide the name of the JSON file to be validated: ")
    process_json_file(filename)

def check_record_length(record):

    limit_size = 32767

    for key, value in record.items():
        if isinstance(value, str) and len(value) > limit_size:
            print(f"\nRecord with more than {limit_size} characters found in key '{key}'\n")
            print("-----------------------")
            exit()

def process_json_file(filename):

    if os.path.isfile(filename):

        with open(filename) as f:
            content = f.read()

        data = json.loads(content)

        for record in data.values():
             check_record_length(record)

    else:
        print("File not found.")

main()