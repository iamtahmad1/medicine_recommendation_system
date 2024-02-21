import json
import csv

# Open the input file
with open('output10.json', 'r') as f:
    # Load the data from the JSON-like structure
    data = json.load(f)

    # Extract all unique symptom categories
    symptom_categories = set()
    for entry in data:
        for category in entry.keys():
            if category != 'medicine_name' and category != 'Dose' and category != 'Relationship':
                symptom_categories.add(category)

    # Convert set to list and sort for consistent column order
    symptom_categories = sorted(list(symptom_categories))

    # Open the output CSV file
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # Define the CSV writer
        writer = csv.writer(csvfile)

        # Write the header row
        header_row = ['Medicine Name'] + symptom_categories
        writer.writerow(header_row)

        # Iterate over each entry in the data
        for entry in data:
            # Extract medicine name
            medicine_name = entry.get('medicine_name', [''])[0]

            # Initialize dictionary for symptoms of each category
            category_symptoms = {category: [] for category in symptom_categories}

            # Iterate over each symptom category and its associated symptoms
            for category, symptoms in entry.items():
                if category != 'medicine_name' and category != 'Dose' and category != 'Relationship':
                    category_symptoms[category] = symptoms

            # Write the data to the CSV file
            row_data = [medicine_name] + [", ".join(category_symptoms[category]) for category in symptom_categories]
            writer.writerow(row_data)

print("CSV file generated successfully.")
