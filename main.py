import json
import os

def main():
    filename = input("Please provide the name of the JSON file to be validated: ")
    process_json_file(filename)

def check_record_length(record, i):

    limit_size = 32767
    error_found = False

    for key, value in record.items():
        if isinstance(value, str) and len(value) > limit_size:
            error_found = True
            print(f"\nRecord {i} with more than {limit_size} characters found in key '{key}'\n")
            print("-----------------------")
            # exit()
        else:
            print(f"Register: {i} validate!")

    return error_found
            

def process_json_file(filename):

    errors = 0

    if os.path.isfile(filename):

        with open(filename) as f:
            content = f.read()

        data = json.loads(content)

        i = 1
        for record in data.values():
             
             error_found = check_record_length(record, i)

             if(error_found == True):
                 errors = errors + 1

             i = i+1

        print(f"Total errors: {errors}")

    else:
        print("File not found.")

main()