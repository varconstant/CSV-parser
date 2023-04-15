import csv
import argparse
import os
import re

def saveCsv(file_path,modified_rows):
    # Save the modified CSV file at the same path
    filename, file_extension = os.path.splitext(file_path)
    modified_csv_path = f"{filename}_modified{file_extension}"
    # print(modified_rows)
    with open(modified_csv_path, 'w', newline='') as modified_csv_file:
        # writer = csv.writer(modified_csv_file)
        modified_csv_file.writelines(modified_rows)

    print(f"Modified CSV file saved at {modified_csv_path}")

def replace_suffix(csv_path, suffix, replacement):
    # Open the CSV file for reading
    with open(csv_path, 'r') as csv_file:
        reader = csv.reader(csv_file)

        # Read each row of the CSV file and replace the suffix with the replacement value
        modified_rows = []
        for row in reader:
            # print(row)
            modified_row = re.sub(r',[a-zA-Z0-9]*$','',row[0])
            # print(modified_row)
            # print(replacement)
            modified_row = modified_row + replacement +'\n'
            # print(modified_row)
            modified_rows.append(modified_row)
        # print(modified_rows)

    saveCsv(csv_path,modified_rows)


if __name__ == '__main__':
    # Parse the command-line arguments
    parser = argparse.ArgumentParser(description='Replace a suffix in a CSV file')
    parser.add_argument('csv_path', type=str, help='the path to the CSV file')
    parser.add_argument('suffix', type=str, help='the suffix to replace')
    parser.add_argument('replacement', type=str, help='the replacement value')

    args = parser.parse_args()

    # Replace the suffix in the CSV file and save the modified file
    replace_suffix(args.csv_path, args.suffix, args.replacement)