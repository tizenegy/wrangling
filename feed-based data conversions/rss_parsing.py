from lxml import etree
import csv

filename = "BBC News - Science & Environment XML Feed"
xml_source_file = open(filename+".xml", "rb")
xml_doc = etree.parse(xml_source_file)
document_root = xml_doc.getroot()

if etree.iselement(document_root):
    output_file = open("rss_"+filename+".csv","w")
    output_writer = csv.writer(output_file)
    
    main_channel = document_root[0]
    article_example = main_channel.find('item')
    tag_list = []
    for child in article_example.iterdescendants():
        tag_list.append(child.tag)
        if child.attrib:
            for attribute_name in child.attrib.keys():
                tag_list.append(attribute_name)
    output_writer.writerow(tag_list)
    for item in main_channel.findall('item'):
        new_row = []
        for tag in tag_list:
            if item.findtext(tag):
                new_row.append(item.findtext(tag))
            elif tag == "isPermaLink":
                new_row.append(item.find('guid').get("isPermaLink"))
        output_writer.writerow(new_row)
    output_file.close()
