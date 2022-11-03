import csv
import json
# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
    # create a dictionary
    data = []
    # Open a csv reader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.reader(csvf)
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            # Assuming a column named 'No' to
            # be the primary key
            data.append({'format': "CHIP-0007",
                'Name':rows[1],
                'description':rows[2],
                'minting-tool':""
                'series_number':rows[0],
                'series_total':500,
                'attributes': [{'trait-type':"gender"}, 
                            {'value':rows[0]}]

                })
        
    #Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
# Driver Code
# Decide the two file paths according to your
# computer system
csvFilePath = r'NFT_Naming_csv.csv'
jsonFilePath = r'Names.json'
# Call the make_json function
make_json(csvFilePath, jsonFilePath)
