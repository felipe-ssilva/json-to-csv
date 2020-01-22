# -*- coding: utf-8 -*-

import csv, json, sys

if sys.argv[1] is not None and sys.argv[2] is not None:

    fileInput = sys.argv[1]
    fileOutput = sys.argv[2]

    inputFile = open(fileInput) #open json file
    outputFile = open(fileOutput, 'w') #load csv file

    data = json.load(inputFile) #load json content
    inputFile.close() #close the input file

    output = csv.writer(outputFile) #create a csv
    output.writerow(data[0].keys())  #header row

    for row in data:
        output.writerow(row.values()) #values row