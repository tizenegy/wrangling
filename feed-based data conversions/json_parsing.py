import json
import csv

filename = "U6_FRED_data"
json_source_file = open(filename+".json","r")
json_data = json.load(json_source_file)
output_file = open("json"+filename+".csv","w")
output_writer = csv.writer(output_file)

output_writer.writerow(list(json_data["observations"][0].keys()))

for obj in json_data["observations"]:
    obj_values = []
    for key, value in obj.items():
        print(key,value)
        obj_values.append(value)
    output_writer.writerow(obj_values)
output_file.close()