# Project
##### Advanced Programming 2021/2022
![Alt description of image](https://www.cloverdx.com/hubfs/david-clode-PsqJlaAlvXk-unsplash__1618841662_5.81.219.59.jpg) 

## Project specification
The project consists in a three *.py* files, each one containing a different parts:
1. ***part_1.py*** consists in a program able to: 
   * Read the files;
   * Provide a registry of analytical operations that can be performed on the dataset and the link to the classes created in the _part_2.py_;
   * Links to _part_3.py_. 
   
2. ***part_2.py*** consists in a program containing the classes and their associated methods for:
   * Recording the numerical metadata consisting of the number of rows and columns of each of the two files composing the data collection;
   * Recording the general semantics of the dataset, i.e. the labels of the columns of each of the two files composing the data collection;
   * Recording the number of different genes detected in literature. The list should be sorted in ascending order;
   * Given a gene symbol, provide the list of sentences that are an evidence in literature about the relation of this gene with COVID-19;
   * Recording the number of different disease detected in literature. The list should be sorted in ascending order;
   * Given a disease ID, provide the list of sentences that are an evidence in literature about the relation of this disease with COVID-19;
   * Recording the 10-top most frequent distinct association between genes and diseases;
   * Given a gene symbol, provide the list of diseases such a gene is associated with;
   * Given a disease name, provide the list of genes such a disease is associated with.
   
   This part of the project has been done by using *Pandas*, which is a fast, powerful, flexible open source data analysis and manipulation tool.
   Also in _part_1.py_ it has been used in order to open the two files; in this way they have been transformed in two **data frames**, manipulated with the functions of Pandas.
   
3. ***part_3.py*** consists in a program which implements the Web-based user interface (UI).

Moreover, a folder with several <ins>templates</ins> is present: it is used in order to implement the file ***part_3.py*** to create an HTML web page.

Finally, <ins>UML diagrams</ins> and <ins>CRC cards</ins> are provided, in order to better understand the classes structures.

## Data
The three parts will analyze the DisGeNET COVID-19 data collection. The *.tsv* files can be downloaded clicking onto the following links:
-   *[disease_evidences.tsv](https://github.com/anuzzolese/genomics-unibo/blob/master/2020-2021/project/dataset/disease_evidences.tsv.gz)*
-   *[gene_evidences.tsv](https://github.com/anuzzolese/genomics-unibo/blob/master/2020-2021/project/dataset/gene_evidences.tsv.gz)*

## Libraries
Several libraries have been used:
```python
import csv
import pandas as pd
from flask import Flask, render_template, request
```

In order to run the program, make sure to have them installed. If not, we have provided some tutorials to do so:
- Installing *[Flask](https://phoenixnap.com/kb/install-flask)*;
- Installing *[pandas](https://pandas.pydata.org/docs/getting_started/install.html)*;
- Installing *[csv](https://pypi.org/project/python-csv/)*.

## Classes specification
Each part has it's own classes, as stated before. In details:
- ***part_1.py*** is connected with *part_2.py* since it imports it. Furthermore, it contains only one class, called <ins>*Registry*</ins>, which aims to contain all the functions calling analytical operations defined in *part_2.py* file;
- ***part_2.py*** contains eleven classes:
  * <ins>Metadata</ins>:;
  * <ins>Semantics</ins>:;
  * <ins>Genes</ins>:;
  * <ins>Pre4</ins>:;
  * <ins>SentencesG</ins>:;
  * <ins>Diseases</ins>:;
  * <ins>Pre6</ins>:;
  * <ins>SentencesD</ins>:;
  * <ins>Top10</ins>:;
  * <ins>AssociationDisease</ins>:;
  * <ins>AssociationGenes</ins>:;

## HTML page
Once running the code, the homepage will be available at the following <ins>*[link](http://127.0.0.1:3000/main)*</ins>.

## Authors
***Corona** Gaia, **Storari** Samuele, **Verdesca** Laura Claudia.*
