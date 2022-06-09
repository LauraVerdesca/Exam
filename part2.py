"""PART 2"""
import pandas as pd
import collections
 
data1 = pd.read_csv('disease_evidences.tsv', delimiter="\t")
data2 = pd.read_csv('gene_evidences.tsv', delimiter="\t")

#class_1
# class Metadata:
#     def __init__(self, data1, data2):
#         self.__data1 = data1
#         self.__data2 = data2
#     
#     def get_rows_col(self):
#         metadata_1 = self.__data1.shape
#         metadata_2 = self.__data2.shape
#         return metadata_1, metadata_2

# 
# # """Trying the class"""
# # class1 = Metadata(data1, data2)
# # print(class1.get_rows_col())
# 
# class Semantics:
#     def __init__(self, data1, data2):
#         self.__data1 = data1
#         self.__data2 = data2
#     
#     def get_labels(self):
#         header1 = list(self.__data1.columns.values)
#         header2 = list(self.__data2.columns.values)
#         return header1, header2
# # 
# # """Trying the class"""
# # class2 = Semantics(data1, data2)
# # print(class2.get_labels())
# 
# 
# #class_3
# 
# # class Genes:
# #     """ The class Genes is about how many different genes are present in the second 
# #     DataFrame and how many times each gene is listed. """
# # 
# #     def __init__(self, data2):
# #         self.__data = data2
# #     
# #     def gene_num(self):
# #         for column in self.__data.columns[4:5]:
# #             gene_symbol = list(self.__data[column])# extracting fifth column
# #         
# #         
# #         occurrences = collections.Counter(gene_symbol)
# #         
# #         return occurrences
# #     
#     
# class Genes:
#     """ The class Genes is about how many different genes are present in the second 
#     DataFrame and how many times each gene is listed. """
# 
#     def __init__(self, data2):
#         self.__data = data2
    
#     def gene_num(self):
#         for column in self.__data.columns[4:5]:
#             gene_symbol = list(self.__data[column])# extracting fifth column
#         
#         
# #         #occurrences = collections.Counter(gene_symbol)
# #         
#         #return occurrences
#         genes = {}
#         for el in gene_symbol:
#             if el not in genes.keys():
#                 genes[el] = 1
#             else:                                      
#                 genes[el] += 1
# 
#         sort_genes = sorted(genes.items(), key=lambda item: item[1], reverse = True)
#         return sort_genes
#         
# # """Trying the class"""
# # class3 = Genes(data2)
# # print(class3.gene_num())
# 
# # class 4.0
# 
# class Pre4:
#   def __init__(self,data2):
#     self.__data = data2
# 
#   def list_gen(self):
#     gene = self.__data['gene_symbol']
#     list_gene = gene.drop_duplicates().tolist() 
#     return list_gene
# 
# 
# #class 4
# 
# class SentencesG:
#     def __init__(self, data2):
#         self.__data = data2
#         #self.__id = geneID
#         
#     def search_covid(self, gene_id):
#         sliced_data2 = self.__data.loc[self.__data['gene_symbol'] == gene_id]
#         covid_list = []
#         sentences_col = sliced_data2['sentence'].tolist()
#         for sentence in sentences_col:
#             if 'COVID19'or 'SARS-CoV2'or 'COVID-19' or 'covid' or 'coronavirus' in sentence:
#                 covid_list.append(sentence)
#         return covid_list
#     
# """Trying the class"""
# geneID = 12
# class4 = SentencesG(data2, geneID)
# print(class4.search_covid())



#Class 5

# class Diseases:
#     def __init__(self, data1):
#         self.__data = data1
#     
#     def diseases_num(self):
#         for column in self.__data.columns[4:5]:
#             disease_symbol = list(self.__data[column]) #extracting fifth column
            
#         occurrences = collections.Counter(disease_symbol)
#         
#         return occurrences
#         disease = {}
#         for el in disease_symbol:
#             if el not in disease.keys():
#                 disease[el] = 1
#             else:                                      
#                 disease[el] += 1
# 
#         sort_diseases = sorted(disease.items(), key=lambda item: item[1], reverse = True)
#         return sort_diseases

# """Trying the class"""
# class5 = Diseases(data1)
# print(class5.diseases_num())

#class pre 6
# class Pre6:
#   def __init__(self,data1):
#     self.__data = data1
# 
#   def list_dis(self):
#     dis = self.__data['diseaseid']
#     list_disease = dis.drop_duplicates().tolist() 
#     return list_disease



# class 6

# class SentencesD:
#     def __init__(self, data1):
#         self.__data = data1
#         
#         
#     def search_covid(self, disease_id):
#         sliced_data1 = self.__data.loc[self.__data['diseaseid'] == disease_id]
#         covid_list = []
#         sentences_col = sliced_data1['sentence'].tolist()
#         for sentence in sentences_col:
#             if 'COVID19'or 'SARS-CoV2'or 'COVID-19' or 'covid' or 'coronavirus' in sentence:
#                 covid_list.append(sentence)
#         
#         return covid_list
#     
# """Trying the class"""
# diseaseID = 'C0000727'
# class6 = SentencesD(data1, diseaseID)
# print(class6.search_covid())
    

# class 7

# class TopTen:
#     def __init__(self, data1, data2):
#         self.__data1 = data1
#         self.__data2 = data2
#         
#     def general_association(self):
#         id_disease = self.__data1['diseaseid']
#         list_disease_id = id_disease.drop_duplicates().tolist() # list of all the different diseases_id
#         dict_association = {}
#         
#         col2 = self.__data2['sentence'].tolist() # "sentence" column in data2
#         
#         for idd in list_disease_id:
#             for row in col2:
#                 if idd in row:
#                     index = col2.index(row)
#                     gene_symbol = self.__data2.loc[index]['gene_symbol'] # associated gene_symbol
#                     association = (gene_symbol, idd) # association (gene_id, disease_id )= key name
#                     
#                     if association not in dict_association.keys(): # new association
#                         dict_association[association] = 1
#                     else:                                       # association already present
#                         dict_association[association] += 1
#                         
#         sorted_dict = sorted(dict_association.items(), key=lambda kv: kv[1])
#         top10 = list(sorted_dict)[:-11:-1]
#         return top10

class TopTen:
    def __init__(self, data1, data2):
        self.__data1 = data1
        self.__data2 = data2
        
    def general_association(self):
        id_genes = self.__data2['gene_symbol']
        list_genes_id = id_genes.drop_duplicates().tolist() # list of all the different diseases_id
        
        
        dict_association = {}
        list_tr = []
        
        col2 = self.__data1['sentence'].tolist() # "sentence" column in data1
        
        for idd in list_genes_id:
            for row in col2:
                if idd in row:
                    index = col2.index(row)
                    disease_name = self.__data1.loc[index]['disease_name'] # associated gene_symbol
                    
                    association = (idd, disease_name) # association (gene_id, disease_id )= key name
                    list_tr.append(association)
                    print(list_tr)
        print(list_tr)
        for el in list_tr:            
            if el in dict_association.keys(): # new association
                dict_association[association] += 1
            else:                                       # association already present
                dict_association[association] = 1
                    
        sorted_dict = sorted(dict_association.items(), key=lambda kv: kv[1], reverse=True)
        print(sorted_dict)
        top10 = list(sorted_dict)[0:9]
        print(top10)


"""Trying the class"""
class7 = TopTen(data1, data2)
print(class7.general_association())


#class 8 pre




#class 8

# class AssociationDisease:
#     
#     def __init__(self, data1):
#         self.__data = data1
#         
#     
#     def search_genes(self, gene_symbol):
#         final_list = []
#         col_sentence = self.__data['sentence'].tolist()
#         for row in col_sentence:
#             if gene_symbol in row:
#                 index_row = col_sentence.index(row)
#                 disease_symbol = self.__data.loc[index_row]['disease_name']
#                 if disease_symbol not in final_list:
#                     final_list.append(disease_symbol)
#                 elif disease_symbol == "COVID19" or disease_symbol == "SARS-CoV2" or disease_symbol == "covid" or disease_symbol == "coronavirus" and disease_symbol in covid_list:
#                     pass
#             
#                 
#         return final_list

# """Trying the class"""
# gene_symbol = 'ACE2'
# class8 = AssociationDisease(data1)
# print(class8.search_genes(gene_symbol))


# class 9

# class AssociationGenes:
#     
#     def __init__(self, data2):
#         self.__data = data2
#         
#         
#     def search_diseases(self, disease_id):
#         final_list = []
#         col_sentence = self.__data['sentence'].tolist()
#         for row in col_sentence:
#             if disease_id in row:
#                 index_row = col_sentence.index(row)
#                 gene_symbol = self.__data.loc[index_row]['gene_symbol']
#                 if gene_symbol not in final_list:
#                     final_list.append(gene_symbol)
#                 
#         return final_list

# """Trying the class"""
# disease_name = 'Coronavirus Disease 2019'
# class9 = AssociationGenes(data2, disease_name)
# print(class9.search_diseases())
# 