"""PART 1"""
import pandas as pd
import csv
from part 2 import *


class Registry():
    def __init__(self):
        self.__data1 = pd.read_csv('disease_evidences.tsv', delimiter="\t")
        self.__data2 = pd.read_csv('gene_evidences.tsv', delimiter="\t")
        self.__operations = ["Get the numerical metadata of the two files: number of rows and columns",
                           "Record the general semantics, hence the labels of the columns",
                           "Get the number of different genes from the first file",
                            #"Get the list of all the genes",
                           "Get the number of different diseases from the second file",
                           "Given a gene symbol, give the list of associations with Covid19",
                           "Given a disease name, give the list of associations with Covid19",
                           "Record the top 10 associations between genes and diseases",
                           "Given a gene symbol, detect the associated diseases",
                           "Given a disease name, detect the associated genes"]
        self.__links = ["MD", "Sem", "G", "P4", "SenG", "D", "P6", "SenD", "T10", "AD", "AG"]
        
    def registry(self):
        return self.__operations
    
    def links(self):
        return self.__links
    
    def link_metadata(self): # class 1
        return Metadata(self.__data1, self.__data2).get_rows_col()

    def link_semantics(self): # class 2
        return Semantics(self.__data1, self.__data2).get_labels()

    def link_geneNum(self): # class 3
        return Genes(self.__data2).gene_num()
    
    def link_prefour(self):
        return Pre4(self.__data2).list_gen()

    def link_geneSent(self): # class 4 # INPUT!!!!
        return SentencesG(self.__data2)

    def link_diseaseNum(self): # class 5
        return Diseases(self.__data1).diseases_num()
    
    def link_presixth(self):
        return Pre6(self.__data1).list_dis()

    def link_disSent(self) : # class 6 #INPUT!!!!
      return SentencesD(self.__data1)

    def link_top10(self): # class 7
        return TopTen(self.__data1, self.__data2).general_association()

    def link_get_geneDisease(self): # class 8 #INPUT!!!
        return AssociationDisease(self.__data1)

    def link_get_DiseaseGene(self): # class 9 #INPUT!!!
        return AssociationGenes(self.__data2)

# per gli input, possiamo creare delle variabili da mettere nel registry tipo a = "gene_choice.html"
# e poi nella funzione richiamare quel valore
