import PyPDF2
import csv
import os
from dotenv import load_dotenv

load_dotenv()
reader = PyPDF2.PdfReader(os.getenv('FILE_PATH'))

pageData = []
p=0
pageCount = len(reader.pages)
for page in reader.pages:
    print(str(p)+"/"+str(pageCount))
    pageDataLinesRaw = page.extract_text().split("\n")
    pageDataLines = pageDataLinesRaw[12:len(pageDataLinesRaw)]
    pageDataItem = {"date":"","description":"","value":"","balance":"","withdrawableBalance":""}
    p = p + 1

    i = 0
    for pdl in pageDataLines:
        if(i % 2 == 0):
            pageDataItem["date"] = pdl
        else:
            splitValues = pdl[8:len(pdl)].split("R$")
            splitValues[0] = splitValues[0][0:len(splitValues[0])-1]
            splitValues[1] = splitValues[1][1:len(splitValues[1])]
            if(splitValues[0][len(splitValues[0])-1] == "-"):
                splitValues[0] = splitValues[0].replace(" -","")
                splitValues[1] = "-"+splitValues[1]
            if(splitValues[2][len(splitValues[2])-1] == "-"):
                splitValues[2] = splitValues[2].replace(" -","")
                splitValues[1] = splitValues[1].replace(" ","")
            splitValues[2] = splitValues[2].replace(" ","")
            if(len(splitValues) > 3):
                splitValues[3] = splitValues[3].replace(" ","")
                pageDataItem["withdrawableBalance"] = splitValues[3]

            pageDataItem["description"] = splitValues[0]
            pageDataItem["value"] = splitValues[1]
            pageDataItem["balance"] = splitValues[2]
            pageData.append(pageDataItem)
            pageDataItem = {"date":"","description":"","value":"","balance":"","withdrawableBalance":""}
        i = i + 1
keys = pageData[0].keys()
with open('picpay_data.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(pageData)
print(pageData)