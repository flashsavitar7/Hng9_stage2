
import csv
import hashlib
import json

#removing blank lines from csv file if any
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

    # Open a csv reader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(BlankLineSkipper(csvf))
        #header = next(csvReader)


        #print(header)
        # Convert each row into a dictionary
        # and add it to data

        for rows in csvReader:
            Team = ""
            team = rows ['TEAM NAMES']
            if team.lower().startswith("team"):
                Team = team
                print(Team)


            # append the json to data
            data.append({'format': "CHIP-0007",
                'Name':rows['Filename'],
                'description':rows['Description'],
                'minting-too':Team,
                'series_number':rows['Series Number'],
                'series_total':420,
                'attributes': [{'trait_type':"gender",'value':rows['Gender']}, 
                    {'trait_type':rows['Attributes'],}

                ],
                'collection':{'name':"Zuri NFT Tickets for Free Lunch", 'id':"b774f676-c1d5-422e-beed-00ef5510c64d",
                'attributes': [{'trait_type':"description",'value':"Rewards for accomplishments during HNGi9"}]}

                })
            
    #Open a json writer, and use the json.dumps()
    # function to dump data        
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))        
            
    #convert json created to hash=sha256
    with open (jsonFilePath) as i:
        val = json.load(i)
        for v in val:
            dat = f"{v}"
            json_hash = hashlib.sha256(dat.encode()).hexdigest()
            v.update({"Hash":json_hash})
        val.append({"Hash":json_hash})
        
        
        
    with open(jsonFilePath, "w") as i:
        json.dump(val, i, indent=4)
        
    with open(jsonFilePath, "r") as openJson:
        datar = json.load(openJson)
    #xonvert json to csv   
    with open('HNGi9-CSV-FILE.output.csv', "w", encoding='utf-8') as newCsv:
        headers = datar[0].keys()
        copy =  csv.DictWriter(newCsv, fieldnames=headers) 
        copy.writeheader()
        for dat in datar:
            copy.writerow(dat) 
                 
# Driver Code
# Decide the two file paths according to your
# computer system
csvFilePath = r'HNGi9-CSV-FILE.csv'
jsonFilePath = r'Names_NFT.json'
# Call the make_json function
make_json(csvFilePath, jsonFilePath)
