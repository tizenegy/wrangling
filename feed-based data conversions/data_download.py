import requests

XMLfilename = "BBC_RSS.xml"
xml_output_file = open(XMLfilename, "w")
xml_data = requests.get('http://feeds.bbci.co.uk/news/science_and_environment/rss.xml')
xml_output_file.write(xml_data.text)
xml_output_file.close()

JSONfilename = "citibikenyc_station_status.json"
json_output_file = open(JSONfilename, "w")
json_data = requests.get('https://gbfs.citibikenyc.com/gbfs/en/station_status.json')
json_output_file.write(json_data.text)
json_output_file.close()