import csv
import json

class BlankLineSkipper(object):
    def __init__(self, file):
        self.file = file
    def __iter__(self):
        return (line for line in self.file if line.strip())
    def read(self):
        return ''.join(self)


# Function to convert a CSV to JSON
# Takes the file paths as arguments

def make_json(csvFilePath, jsonFilePath):
    # create a dictionary

    data = []
    datas = ""
    atrr = []
    values = []

    # Open a csv reader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(BlankLineSkipper(csvf))
        header = next(csvReader, 0)


        #print(header)
        # Convert each row into a dictionary
        # and add it to data

        for rows in csvReader:

            Team = rows['TEAM NAMES']
            if Team.lower().startswith("team"):
                datas = Team
                print(datas)



            attributes = rows['Attributes']
            atrr = attributes.split(";")
            for i in atrr:
                value = i.split(":")
                trait_type = value[0]
                values = value[1]
                print(values)

            # Assuming a column named 'No' to
            # be the primary key
            data.append({'format': "CHIP-0007",
                'Name':rows['Filename'],
                'description':rows['Description'],
                'minting-too':datas,
                'series_number':rows['Series Number'],
                'series_total':420,
                'attributes': [{'trait_type':"gender",'value':rows['Gender']}, 
                    {'trait_type':trait_type,'value':values}

                ],
                'collection':{'name':"Zuri NFT Tickets for Free Lunch", 'id':"b774f676-c1d5-422e-beed-00ef5510c64d",
                'attributes': [{'trait_type':"description",'value':"Rewards for accomplishments during HNGi9"}]}

                })
    


    #Open a json writer, and use the json.dumps()
    # function to dump data
            count = 0
            with open(jsonFilePath +str(count), 'w', encoding='utf-8') as jsonf:
                 jsonf.write(json.dumps(data, indent=4))
# Driver Code
# Decide the two file paths according to your
# computer system
csvFilePath = r'HNGi9-CSV-FILE.csv'
jsonFilePath = r'Names.json'
# Call the make_json function
make_json(csvFilePath, jsonFilePath)
