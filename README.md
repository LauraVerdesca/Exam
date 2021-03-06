# Project
##### Advanced Programming 2021/2022
<img width="1014" alt="Schermata 2022-06-15 alle 21 20 15" src="https://user-images.githubusercontent.com/106587485/173909765-9e8e83e9-b1e8-45c4-92ad-32ccb31c4ec0.png">

## Specification
The project consists in a three *.py* files, each one containing a different part:
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
   
3. ***part_3.py*** consists in a program which implements the Web-based user interface (UI).


## CRC Cards
We have provided a folder with CRC cards explaining each class built in _part_2.py_, each CRC card has been created with **Visual Paradigm**.

## UML diagrams
We have provided a folder with an UML diagram explaining the connections between the classes built in _part_2.py_:
- _DiagramProject.jpg_ is an image representing the UML diagram created with **Visual Paradigm**.
- _UMLproject_final.vpp_ is the equivalent of _DiagramProject.jpg_ but in format _.vpp_.

## Templates 
It is a folder with several <ins>templates</ins> used in order to implement the file ***part_3.py*** to create an HTML web page.

## Data
The three parts will analyze the DisGeNET COVID-19 data collection. The *.tsv* files can be downloaded clicking onto the following links:
-   *[disease_evidences.tsv](https://github.com/anuzzolese/genomics-unibo/blob/master/2020-2021/project/dataset/disease_evidences.tsv.gz)*
-   *[gene_evidences.tsv](https://github.com/anuzzolese/genomics-unibo/blob/master/2020-2021/project/dataset/gene_evidences.tsv.gz)*

## Libraries
Several libraries have been used:
```python
import pandas as pd
from flask import Flask, render_template, request
```

In order to run the program, make sure to have them installed. If not, we have provided some tutorials to do so:
- Installing *[Flask](https://phoenixnap.com/kb/install-flask)*;
- Installing *[pandas](https://pandas.pydata.org/docs/getting_started/install.html)*.

## HTML page
Once running the *part_3.py*, the homepage will be available at the following <ins>*[link](http://127.0.0.1:3000/)*</ins>.

## Authors
***Corona** Gaia, **Storari** Samuele, **Verdesca** Laura Claudia.*
