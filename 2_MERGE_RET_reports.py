import os
import csv
from datetime import date, datetime

# Define the directory path
directory = os.path.expanduser("~/Documents/Data_Collection")

# Create a subdirectory based on the current date
current_date = date.today().strftime("%d-%m-%Y")
input_directory  = os.path.join(directory, "input", "ret")
output_directory = os.path.join(directory, current_date, "output", "ret")

def merge_csv_files(input_directory, output_directory, output_file):
    # Get all CSV files in the input directory
    csv_files = [file for file in os.listdir(input_directory) if file.endswith('.csv')]

    # Check if any CSV files are found
    if not csv_files:
        print("No CSV files found in the input directory.")
        return

    # Sort the CSV files alphabetically
    csv_files.sort()
    
    # Create the output directory path
    output_directory_path = os.path.expanduser(os.path.join(output_directory))
    os.makedirs(output_directory_path, exist_ok=True)

    # Set the output file path
    output_file_path = os.path.join(output_directory_path, output_file)

    # Initialize the output CSV file
    with open(output_file_path, 'w', newline='') as output:
        writer = csv.writer(output)

        # Process each CSV file
        for i, file in enumerate(csv_files):
            file_path = os.path.join(input_directory, file)

            with open(file_path, 'r') as input_file:
                reader = csv.reader(input_file)

                # Skip header for all files except the first one
                if i > 0:
                    next(reader)

                # Write the data from all files
                for row in reader:
                    writer.writerow(row)

    print(f"RET files merged successfully. Merged file saved at {output_file_path}")

# input and output 
# input_directory = os.path.expanduser(os.path.join(directory,"input", "ret"))
# output_directory = os.path.expanduser(os.path.join(directory, current_date, "output", "ret" ))
output_file = 'ret_merged' + datetime.now().strftime(("-%Y-%m-%d_T%H-%M-%S") + '.csv')

# # Create the directory if it doesn't exist
# os.makedirs(output_directory, exist_ok=True)

merge_csv_files(input_directory, output_directory, output_file)
