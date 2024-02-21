import json
import csv

# Open the input file
with open('output10.json', 'r') as f:
    # Load the data from the JSON-like structure
    data = json.load(f)

    # Open the output CSV file
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # Define the CSV writer
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['Medicine Name', 'Symptom', 'Description'])

        # Iterate over each entry in the data
        for entry in data:
            # Extract medicine name
            medicine_name = entry.get('medicine_name', [''])[0]

            # Iterate over symptoms and descriptions
            for symptom, description in entry.items():
                if symptom != 'medicine_name':
                    # Write the data to the CSV file
                    writer.writerow([medicine_name, symptom, description[0]])

print("CSV file generated successfully.")
