# Conversor de arquivo JSON para CSV com Python

É uma aplicacão extremamente simples, porém me ajudou MUITO em um trabalho.
Com poucas linhas de código você pode converter seu arquivo json em um arquivo csv usando Python.

## Passo a passo:

Crie o arquivo: **json_to_csv.py** (Ou com qualquer outro nome que desejar, o que importa é formato .py)

Copie o código abaixo e cole no arquivo.
```
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
```

Salve o arquivo e no terminal rode o seguinte comando:
```
python json_to_csv.py input.json output.csv
```

It's all folks