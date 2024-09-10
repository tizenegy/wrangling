import csv

filename = "ghcnd-stations"
source_file = open(filename+".txt", "r")

stations_list = source_file.readlines()
output_file = open(filename+".csv", "w")
output_writer = csv.writer(output_file)

headers = ["ID","LATITUDE","LONGITUDE","ELEVATION","STATE","NAME","GSN_FLAG","HCNCRN_FLAG","WMO_ID"]

output_writer.writerow(headers)

for line in stations_list:
    new_row = []
    new_row.append(line[0:11])
    new_row.append(line[12:20])
    new_row.append(line[21:30])
    new_row.append(line[31:37])
    new_row.append(line[38:40])
    new_row.append(line[41:71])
    new_row.append(line[72:75])
    new_row.append(line[76:79])
    new_row.append(line[80:85])
    output_writer.writerow(new_row)

output_file.close()

"""
ID            1-11   Character
LATITUDE     13-20   Real
LONGITUDE    22-30   Real
ELEVATION    32-37   Real
STATE        39-40   Character
NAME         42-71   Character
GSN FLAG     73-75   Character
HCN/CRN FLAG 77-79   Character
WMO ID       81-85   Character
"""