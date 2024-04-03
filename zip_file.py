import datetime
import pandas as pd
import zipfile
import os
import csv

# Specify the path to your zip file in the local system
zip_file_path = '/home/nineleaps/Downloads/20240305124003123456_Extract.zip'

# Open the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Extract all contents to a specified directory "extracted_contents"
    zip_ref.extractall('extracted_contents')

# After this, the contents of the zip file will be extracted to the specified directory

# Function to extract load timestamp from zip file name
def extract_load_timestamp(zip_file_name):
    
    timestamp_str = zip_file_name[:14]
    
    load_timestamp = datetime.datetime.strptime(timestamp_str, '%Y%m%d%H%M%S')
    return load_timestamp
    

# Load your sample files into pandas dataframes
df1 = pd.read_csv("/home/nineleaps/Desktop/Day 2/extracted_contents/20240305124003123456_Extract.zip/sample.csv")
df2 = pd.read_csv("/home/nineleaps/Desktop/Day 2/extracted_contents/20240305124003123456_Extract.zip/sample2.csv")




#getting the name of the file using file_path using os module
file_name  = os.path.basename(zip_file_path)

#getting the timestamp from the zip file name
load_timestamp = extract_load_timestamp(file_name)

# Update CSV files with load timestamp
csv_files = ["sample.csv", "sample2.csv"]
for csv_file in csv_files:
    csv_file_path = os.path.join('/home/nineleaps/Desktop/Day 2/extracted_contents/20240305124003123456_Extract.zip', csv_file)
    updated_rows = []

    # Read CSV file
    with open(csv_file_path, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Skip the header row
        header.append("Load Timestamp")

        # Append load timestamp to each row
        for row in reader:
            row.append(load_timestamp.strftime('%Y-%m-%d %H:%M:%S'))  # Assuming you want the timestamp in this format
            updated_rows.append(row)

    # Write updated rows back to CSV file
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)  # Write the header row back
        writer.writerows(updated_rows)

print("Timestamp added to CSV files successfully.")