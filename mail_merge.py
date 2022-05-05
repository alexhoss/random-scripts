# automate mail merging from ebay's sales record

import csv
from mailmerge import MailMerge
from datetime import date
import os

orders = []
i = 0

for file in os.listdir(os.getcwd()):
    if file.startswith('eBay'):
        csv_file = file

with open(csv_file, 'r') as inp:
    for row in csv.reader(inp):
        if row[3] != "":
            ship_to_addr = {
                "Ship_To_Name": row[3],
                "Ship_To_Address_1": row[6],
                "Ship_To_Address_2": None,
                "Ship_To_City": row[8],
                "Ship_To_Province": row[9],
                "Ship_To_Postal_Code": row[10]
            }
            if row[7] != "": ship_to_addr.update({'Ship_To_Address_2': row[7] })
            
            orders.append(ship_to_addr)
            
orders.pop(0)   # first row is always empty 

template = "label-template.docx"
document = MailMerge(template)

document.merge_pages(orders)
document.write("to_print.docx")