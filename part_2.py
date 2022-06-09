"""PART 2"""
import pandas as pd

#class_1
class Metadata:
    """ The class Metadata is involved in getting general info about the dataframes.
        The informations obtained are the number of rows and columns of each file. """

	def __init__(self, data1, data2):
		self.__data1 = data1
		self.__data2 = data2
		
	def get_rows_col(self):
		metadata_1 = self.__data1.shape
		metadata_2 = self.__data2.shape
		return metadata_1, metadata_2
    

#class_2
class Semantics:
    """ The class Semantics has been created to carry out the operation of getting
        the labels of the columns for each file. """

	def __init__(self, data1, data2):
		self.__data1 = data1
		self.__data2 = data2

	def get_labels(self):
		header1 = list(self.__data1.columns.values)
		header2 = list(self.__data2.columns.values)
		return header1, header2


#class_3    
class Genes:
    """ The class Genes is about how many different genes are present in the second 
    DataFrame and how many times each gene is listed. """

	def __init__(self, data2):
		self.__data = data2

	def gene_num(self):
		for column in self.__data.columns[4:5]:
			gene_symbol = list(self.__data[column])# extracting fifth column

		genes = {}
		for el in gene_symbol:
			if el not in genes.keys():
				genes[el] = 1
			else:                                      
				genes[el] += 1

		sort_genes = sorted(genes.items(), key=lambda item: item[1], reverse = True)
		return sort_genes


# class pre 4
class Pre4:
    """The class Pre4 lists all of the genes present in the file gene_evidences"""

	def __init__(self,data2):
		self.__data = data2

	def list_gen(self):
		gene = self.__data['gene_symbol']
		list_gene = gene.drop_duplicates().tolist() 
		return list_gene


#class 4
class SentencesG:
    """ The class SentencesG works with the gene file and exctracts all the sentences involved with Covid
        and associated to a specific gene. """
    
	def __init__(self, data2):
		self.__data = data2
		#self.__id = geneID

	def search_covid(self, gene_id):
		sliced_data2 = self.__data.loc[self.__data['gene_symbol'] == gene_id]
		covid_list = []
		sentences_col = sliced_data2['sentence'].tolist()
		for sentence in sentences_col:
			if 'COVID19'or 'SARS-CoV2'or 'COVID-19' or 'covid' or 'coronavirus' in sentence:
				covid_list.append(sentence)
		return covid_list


#Class 5
class Diseases:
    """ The class Diseases will report all the different diseases and how many times
        they have bene listed in the disease file. """

	def __init__(self, data1):
		self.__data = data1

	def diseases_num(self):
		for column in self.__data.columns[4:5]:
			disease_symbol = list(self.__data[column]) #extracting fifth column

		occurrences = collections.Counter(disease_symbol)
        
		return occurrences
		disease = {}
		for el in disease_symbol:
			if el not in disease.keys():
				disease[el] = 1
			else:                                      
				disease[el] += 1

		sort_diseases = sorted(disease.items(), key=lambda item: item[1], reverse = True)
		return sort_diseases


#class pre 6
class Pre6:
    """The class Pre6 lists all of the diseases present in the file disease_evidences"""

	def __init__(self,data1):
		self.__data = data1

	def list_dis(self):
		dis = self.__data['diseaseid']
		list_disease = dis.drop_duplicates().tolist()
		return list_disease


#class_6
class SentencesD:
     """ The class Sentences D gives the list of all sentences associated to Covid and 
    the specific given disease. """

	def __init__(self, data1):
		self.__data = data1


	def search_covid(self, disease_id):
		sliced_data1 = self.__data.loc[self.__data['diseaseid'] == disease_id]
		covid_list = []
		sentences_col = sliced_data1['sentence'].tolist()
		for sentence in sentences_col:
			if 'COVID19'or 'SARS-CoV2'or 'COVID-19' or 'covid' or 'coronavirus' in sentence:
				covid_list.append(sentence)

		return covid_list


#class 7
class TopTen:
    """ The class TopTen returns the 10 most abundant associations between genes and diseases."""
    
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


#class_8
class AssociationDisease:
     """ This class will return a list of diseases that are associated to the given gene by its symbol """

	def __init__(self, data1):
		self.__data = data1


	def search_genes(self, gene_symbol):
		final_list = []
		col_sentence = self.__data['sentence'].tolist()
		for row in col_sentence:
			if gene_symbol in row:
				index_row = col_sentence.index(row)
				disease_symbol = self.__data.loc[index_row]['disease_name']
				if disease_symbol not in final_list:
					final_list.append(disease_symbol)
				elif disease_symbol == "COVID19" or disease_symbol == "SARS-CoV2" or disease_symbol == "covid" or disease_symbol == "coronavirus" and disease_symbol in covid_list:
					pass


		return final_list



#class_9
class AssociationGenes:
    """ This class will return a list of the genes associated to the given disease by its name """

	def __init__(self, data2):
		self.__data = data2


	def search_diseases(self, disease_id):
		final_list = []
		col_sentence = self.__data['sentence'].tolist()
		for row in col_sentence:
			if disease_id in row:
				index_row = col_sentence.index(row)
				gene_symbol = self.__data.loc[index_row]['gene_symbol']
				if gene_symbol not in final_list:
					final_list.append(gene_symbol)

		return final_list