## Project specification

***part_1.py*** is connected with *part_2.py* since it imports it. 

It has only one class, called <ins>*Registry*</ins>, which aims to contain all the functions calling analytical operations defined in the *part_2.py* file.

The files are opened through **Pandas**: in this way they are transformed in two dataframes, easily manipulated through the functions of the previously mentioned library. 

  * In lines <ins>10-18</ins> there is the list of all the operations that have to be carried out.
  * Line <ins>19</ins> lists all the acronyms associated to the classes of _part_2.py_. They will be needed for _part_3.py_ and for this reason they are returned in lines <ins>24-25</ins>.
  * Each function from line <ins>27</ins> to <ins>58</ins> is associated to a specififc operation, in fact each one returns the result of its corresponding class from _part_2.py_.
 
***part_2.py*** 

It has 11 classes:

  * <ins>*Metadata*</ins>: <br/>
It is involved in getting the number of rows and columns of each file.
A specific Pandas function is used: **.shape** returns a tuple(n. rows, n. cols);

  * <ins>*Semantics*</ins>: <br/>
With this class the labels of the columns for each file are obtained. Also in this case a Pandas function is used, always because the two files are opened as two dataframes. The function is: **.columns.values** and the result is transformed into a list;

  * <ins>*Genes*</ins>: <br/>
_Genes_ class is involved in finding all the different genes in the _gene_evidences.tsv_ file and how many times each one is present.
A _gene_symbol_ list is created by exctraction of the corresponding column from the file. The dictionary is the final output where, after iteration on the list, the key is the gene and the value is the counter (hence how many time the specific gene was counted inside the list, so how many times is present in the file);

  * <ins>*Pre4*</ins>: <br/>
It is involved in listing all of the genes present in the file _gene_evidences.tsv_, in fact is very similar to the previous one and the difference is in the absence of the counter.
After the exctraction of the "gene_symbol" column as dataframe, the Pandas function **drop_duplicates().tolist()** is used to remove repetitions.
The aim of this function is to display the different genes of the file on the screen, in fact it is connected to the _part_3.py_;

  * <ins>*SentencesG*</ins>: <br/>
The class is involved in working with the gene file and exctracting all the sentences involved with Covid and associated to a specific gene requested by the user from _part_3.py_.
In line <ins>80</ins> the **loc[self.__data['gene_symbol'] == gene_symbol]** function is used in order to exctract the portion of the matrix related to the gene and then, through iteration, _covid_list_ is created;
 
  * <ins>*Diseases*</ins>: <br/>
The class is involved in finding all the different diseases in the _disease_evidences.tsv_ file and how many times each one is present.
A _disease_symbol_ list is created by exctraction of the "disease name" column from the file. The dictionary is the final output where, after iteration on the list, the key is the disease and the value is its counter;

  * <ins>*Pre6*</ins>: <br/>
It is involved in listing all of the diseases present in the file _disease_evidences.tsv_; it is very similar to the _Disease_ class and the difference is in the absence of the counter.
After the exctraction of the "diseaseid" column as dataframe, the Pandas function **drop_duplicates().tolist()** is used to remove repetitions.
The aim of this function is to display the different diseases of the file on the screen, in fact it is connected to the _part_3.py_;

  * <ins>*SentencesD*</ins>: <br/>
The class is involved in giving the list of all sentences associated to Covid and the specific disease, given by input from the user in _part_3.py_.
In line <ins>136</ins> the **loc[self.__data['diseaseid'] == disease_id]** function is used in order to exctract the portion of the matrix related to the disease and then, through iteration, _covid_list_ is created;

  * <ins>*Top10*</ins>: <br/>
It is involved in returning the 10 most abundant associations between genes and diseases. <br/>
The idea behind the algorithm  is to search in the domain of the solution (hence all the possible combinations between diseases and genes, which is indeed the search space) in order to get at the end the top10 most abundant associations.
All the genes have been exctracted from the file _gene_evidences.tsv_ as a list without duplicates through the Pandas function **drop_duplicates().tolist()**. <br/>
To save all the associations, a dictionary is used: _dict_association_. The keys are the associations and the values are the counters.<br/>
The reasoning is: while doing a double for loop to analyse every gene in the _list_genes_ and the column of the _sentences_ in the _disease_eviences.tsv_ file, <ins>if<</ins> the gene is present in the sentence, then the disease associated to the sentence is taken and the key of the dictionary is created. 
Every time a key is already present, the counter increases, otherwise it is created. <br/>
After obtaining the dictionary, it is sorted to put everything in discending order with **sorted(dict_association.items(), key=lambda kv: kv[1], reverse=True)** and the first ten elements are sliced and given as result. <br/>
Due to the high time complexity, the iteration is commented and the output (**top10**) is already stored.
 
  * <ins>*AssociationDisease*</ins>: <br/>
It is involved in returning a list of diseases that are associated to a gene specified by the user thanks to the link with _part_3.py_.
By searching the gene in the sentences of the _disease_evidences.tsv_ file, when it is present then the disease name is exctracted by using the Pandas function: **loc[index_row]['disease_name']**. All the diseases are appended to the _final_list_;

  * <ins>*AssociationGenes*</ins>: <br/>
The class is involved in returning a list of the genes associated to the given disease by its name (asked by the user).
It is the same reasoning of before: by searching the disease in the sentences of the _gene_evidences.tsv_ file, when it is present then the gene name is exctracted by using the Pandas function: **loc[index_row]['gene_symbol']**. All the genes, without repetitions, are appended to the _final_list_.

**Efficiency**
<br/>
All the classes, except for the seventh one, have a low time complexity and they run in few seconds. 
<br/>
The _Top10_ problem has been resolved with an _exhaustive search_ approach, meanining that we explored both the datasets in order to find the best solution. In this way we prioritized the optimality of the solution in spite of the time effeciency. For this reason we already saved the output and assigned it to a variable. So when the user clicks on the seventh class of the Web UI, what will appear on the screen is the saved output and not the actual class running. Still the class works but the running time is about 14 hours.

***part_3*** is connected with *part_1.py* since it imports it. 
<br/>
Furthermore, it contains several *@app_route* decorators which intend to map the URLs to a specific function that will handle the logic for that URL. 
It will create fourteen pages:

  * */main*: <br/>
It shows the nine possible choices the user can select;

  * */MD*: <br/>
It shows the output of *Metadata* class. This is done by returning the link from _part_1.py_ and using **render template** to connect with the correspective HTML templates. This is valid for all the pages;

  * */Sem*: <br/> 
It shows the output of *Semantics* class;

  * */G*: <br/>
It shows the output of *Genes* class;

  * */P4*: <br/>
It displays on the fourth page the list of genes from which the user has to choose;

  * */SenG*: <br/>
After taking as input the result from the previous page, the gene is authomatically sent to _SenG_, which shows the output of the class _SentencesG_;

  * */D*: <br/>
It shows the output of *Diseases* class;

  * */P6*: <br/>
It displays on the sixth page the list of diseases ID from which the user has to choose;

  * */SenD*: <br/>
After taking as input the result from the previous page, the disease is authomatically sent to _SenD_, which shows the output of the class _SentencesD_;

  * */T10*: <br/>
It shows the output of *Top10* class, so the top 10 distinct associations between genes an diseases;

  * */P8*: <br/>
It displays on the eighth page the list of genes from which the user has to choose;

  * */AD*: <br/>
After taking as input the result from the previous page, the gene is authomatically sent to _AD_, which shows the output of the class _AssociationD_;

  * */P9*: <br/>
It displays on the ninth page the list of diseases ID from which the user has to choose;

  * */AG*: <br/>
After taking as input the result from the previous page, the disease is authomatically sent to _AG_, which shows the output of the class _AssociationG_.

!!! In all the cases in which the input is needed, the function used to connect everything is: **request.args.get('')** placed inside the returned function of the class from _part_2.py_.

<br/>

***templates*** folder contains fourteen *.html* files that display the outputs:
- <ins>*homepage.html*</ins> contains: 
  * *Text-decoration shorthand CSS properties*: set the appearance of decorative lines on text (*head* part);
  * *Headings*: some centered, some not (*body* part);
  * *Buttons*: each one connects the command with a secondary page with the output or a *form* (*body* part);   
  * *Footer* with the names of the authors.
- <ins>*metadata.html*</ins>, <ins>*general_semantics.html*</ins>, <ins>*genes.html*</ins>, <ins>*diseases.html*</ins> and <ins>*top_ten.html*</ins> contain: 
  * *Text-decoration shorthand CSS properties*: set the appearance of decorative lines on text (*head* part);
  * *Headings*: some centered, some not (*body* part);
  * *Buttons*: each one connects the secondary page with the */main* (*body* part);
  * *Footer* with the names of the authors.
- <ins>*user_diseasesentences.html*</ins>, <ins>*user_genesentences.html*</ins>, <ins>*user_nine.html*</ins> and <ins>*user_usereight.html*</ins> contain: 
  * *Text-decoration shorthand CSS properties*: set the appearance of decorative lines on text (*head* part);
  * *Headings*: some centered, some not (*body* part);
  * *Forms*: used to store the user input and pass it to the third page (*body* part);
  * *Buttons*: each one connects the secondary page with the */main* (*body* part)
  * *Footer* with the names of the authors.
- <ins>*association_d.html*</ins>, <ins>*association_g.html*</ins>, <ins>*sentences_d.html*</ins> and <ins>*sentences_g.html*</ins> contain: 
  * *Text-decoration shorthand CSS properties*: set the appearance of decorative lines on text (*head* part);
  * *Headings*: some centered, some not (*body* part);
  * *Buttons*: some connect the third page with the */main*, others go back to the secondary page (*body* part);
  * *Footer* with the names of the authors.



