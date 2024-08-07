import os
import csv
from datetime import date
import time

def generate_report(folder_path: str, report_file: str) -> None:
    """
    Generate a report of the number of files in each folder in the specified path.
        folder_path (str): The path to the folder to generate the report for.
        report_file (str): The name of the report file to generate.
    """
    
    # Check if the folder path exists
    if not os.path.exists(folder_path):
        print(f"Error: The specified folder path '{folder_path}' does not exist.")
        return
    
    # Check if the folder path is a directory
    if not os.path.isdir(folder_path):
        print(f"Error: The specified folder path '{folder_path}' is not a directory.")
        return
    
    # Define the report header
    report_header = ['Folder Name', 'Number of Files']
    
    # Create a list to store the report data
    report_data = []
    
    # Iterate through each folder in the specified path
    for folder in os.listdir(folder_path):
        # Get the full path of the folder
        folder_full_path = os.path.join(folder_path, folder)
        
        # Check if the folder is a directory
        if os.path.isdir(folder_full_path):
            # Count the number of files in the folder
            file_count = len(os.listdir(folder_full_path))
            
            # Append the report data to the list
            report_data.append([folder, file_count])
    
    # Create the report file
    with open(report_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(report_header)
        writer.writerows(report_data)
    
    # Print a success message
    print(f"Report generated successfully: {report_file} at {time.strftime('%H:%M:%S')}")

# Define the folder path and report file name
folder_path = 'C:\\Users\\MIRUDULAA\\Desktop\\Cognifyz\\level 3'
report_file = f'C:\\Users\\MIRUDULAA\\Desktop\\Cognifyz\\Level 3\\employees_{date.today().strftime("%y-%m-%d")}.csv'

# Generate the report
generate_report(folder_path, report_file)

# Output :-
#     Daily report generated successfully: C:\Users\MIRUDULAA\Desktop\Cognifyz\Level 3\employees_24-08-07.csv at 19:07:14 