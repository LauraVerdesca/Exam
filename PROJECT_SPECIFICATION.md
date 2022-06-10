## Project specification
Each part has it's own classes, as stated before. In details:
- ***part_1.py*** is connected with *part_2.py* since it imports it. Furthermore, it contains only one class, called <ins>*Registry*</ins>, which aims to contain all the functions calling analytical operations defined in *part_2.py* file;
- ***part_2.py*** contains eleven classes:
  * <ins>*Metadata*</ins>: it is involved in getting general info about the dataframes, which are the number of rows and columns of each file;
  * <ins>*Semantics*</ins>: it is involved in carrying out the operation of getting the labels of the columns for each file;
  * <ins>*Genes*</ins>: it is involved in finding how many different genes are present in the second DataFrame and how many times each gene is listed;
  * <ins>*Pre4*</ins>: it is involved in listing all of the genes present in the file *gene_evidences.tsv*;
  * <ins>*SentencesG*</ins>: it is involved in working with the gene file and exctracting all the sentences involved with Covid and associated to a specific gene;
  * <ins>*Diseases*</ins>: it is involved in reporting all the different diseases and how many times they have been listed in the disease file;
  * <ins>*Pre6*</ins>: it is involved in listing all of the diseases present in the file *disease_evidences.tsv*;
  * <ins>*SentencesD*</ins>: it is involved in giving the list of all sentences associated to Covid and the specific given disease;
  * <ins>*Top10*</ins>: it is involved in returning the 10 most abundant associations between genes and diseases;
  * <ins>*AssociationDisease*</ins>: it is involved in returning a list of diseases that are associated to the given gene by its symbol;
  * <ins>*AssociationGenes*</ins>: it is involved in returning a list of the genes associated to the given disease by its name.
- ***part_3.py*** is connected with *part_1.py* since it imports it. Furthermore, it contains several *@app_route* decorators which intend to map the URLs to a specific function that will handle the logic for that URL. It will create fourteen pages:
  * */main*: shows the nine possible choices the user can select;
  * */MD*: shows the output of *Metadata* class;
  * */Sem*: shows the output of *Semantics* class;
  * */G*: shows the output of *Genes* class;
  * */P4*: shows ;
  * */SenG*: shows ;
  * */D*: shows the output of *Diseases* class;
  * */P6*: shows;
  * */SenD*: shows;
  * */T10*: shows the output of *Top10* class;
  * */P8*: shows;
  * */AD*: shows;
  * */P9*: shows;
  * */AG*: shows.
- ***templates*** folder contains fourteen *.html* files that display the outputs:
  * <ins>*homepage.html*</ins> contains: 
    * *Text-decoration shorthand CSS properties*: set the appearance of decorative lines on text (*head* part);
    * *Headings*: some centered, some not (*body* part);
    * *Buttons*: each one connects the command with a secondary page with the output or a *form* (*body* part);
    * *Footer* with the names of the authors.
  * <ins>*metadata.html*</ins>, <ins>*general_semantics.html*</ins>, <ins>*genes.html*</ins>, <ins>*diseases.html*</ins> and <ins>*top_ten.html*</ins> contain: 
    * *Text-decoration shorthand CSS properties*: set the appearance of decorative lines on text (*head* part);
    * *Headings*: some centered, some not (*body* part);
    * *Buttons*: each one connects the secondary page with the */main* (*body* part);
    * *Footer* with the names of the authors.
  * <ins>*user_diseasesentences.html*</ins>, <ins>*user_genesentences.html*</ins>, <ins>*user_nine.html*</ins> and <ins>*user_usereight.html*</ins> contain: 
    * *Text-decoration shorthand CSS properties*: set the appearance of decorative lines on text (*head* part);
    * *Headings*: some centered, some not (*body* part);
    * *Forms*: used to store the user input and pass it to the third page (*body* part);
    * *Buttons*: each one connects the secondary page with the */main* (*body* part);
    * *Footer* with the names of the authors.
  * <ins>*association_d.html*</ins>, <ins>*association_g.html*</ins>, <ins>*sentences_d.html*</ins> and <ins>*sentences_g.html*</ins> contain: 
    * *Text-decoration shorthand CSS properties*: set the appearance of decorative lines on text (*head* part);
    * *Headings*: some centered, some not (*body* part);
    * *Buttons*: some connect the third page with the */main*, others go back to the secondary page (*body* part);
    * *Footer* with the names of the authors.


## Project specification GAIA

***part_1.py*** is connected with *part_2.py* since it imports it. 

It has only one class, called <ins>*Registry*</ins>, which aims to contain all the functions calling analytical operations defined in *part_2.py* file.

The files are opened through **Pandas**: in this way they are transformed in two dataframes, easily manipulated through the functions of the previously mentioned library. 

  * In lines <ins>10-18</ins> there is the listing of all the operations that have to be carried out.
  * Line <ins>19</ins> lists all the acronyms associated to the classes of _part_2.py_. They will be needed for _part_3.py_ and for this reason they are returned in lines <ins>24-25</ins>.
  * Each function from line <ins>27</ins> to <ins>58</ins> is associated to a specififc operation, in fact each one returns the result of the its correspective class from _part_2.py_.
 
***part_2.py*** 

It has 11 classes:

  * <ins>*Metadata*</ins>:
It is involved in getting the number of rows and columns of each file.
A specific Pandas function is used: **.shape** returns a tuple(n. rows, n. cols);

  * <ins>*Semantics*</ins>: 
With this class the labels of the columns for each file are obtained. Also in this case a Pandas function is used, always because the two files are opened as two dataframes. The function is: **.columns.values** and the result is transformed into a list;

  * <ins>*Genes*</ins>: 
_Genes_ class is involved in finding all the different genes in the _gene_evidences.tsv_ file and how many times each one is present.
A _gene_symbol_ list is created by exctraction of the corresponding column from the file. The dictionary is the final output where, after iteration on the list, the key is the gene and the value is the counter (hence how many time the specific gene was counted inside the list, so how many times is present in the file);

  * <ins>*Pre4*</ins>: 
It is involved in listing all of the genes present in the file _gene_evidences.tsv_, in fact is very similar to the previous one and the difference is in the absence of the counter.
After the exctraction of the "gene_symbol" column as dataframe, the Pandas function **drop_duplicates().tolist()** is used to remove repetitions.
The aim of this function is to display the different genes of the file on the screen, in fact it is connected to the _part_3.py_;

  * <ins>*SentencesG*</ins>: 
The class is involved in working with the gene file and exctracting all the sentences involved with Covid and associated to a specific gene requested by the used from _part_3.py_.
In line <ins>80</ins> the **loc[self.__data['gene_symbol'] == gene_symbol]** function is used in order to exctract the portion of the matrix related to the gene and then, through iteration, _covid_list_ is created;
 
  * <ins>*Diseases*</ins>: 
The class is involved in finding all the different diseases in the _disease_evidences.tsv_ file and how many times each one is present.
A _disease_symbol_ list is created by exctraction of the "disease name" column from the file. The dictionary is the final output where, after iteration on the list, the key is the disease and the value is its counter;

  * <ins>*Pre6*</ins>: 
It is involved in listing all of the diseases present in the file _disease_evidences.tsv_; it is very similar to the _Disease_ class and the difference is in the absence of the counter.
After the exctraction of the "diseaseid" column as dataframe, the Pandas function **drop_duplicates().tolist()** is used to remove repetitions.
The aim of this function is to display the different diseases of the file on the screen, in fact it is connected to the _part_3.py_;

  * <ins>*SentencesD*</ins>: it is involved in giving the list of all sentences associated to Covid and the specific given disease
The class is involved in giving the list of all sentences associated to Covid and the specific disease, given by input from the user in _part_3.py_.
In line <ins>136</ins> the **loc[self.__data['diseaseid'] == disease_id]** function is used in order to exctract the portion of the matrix related to the disease and then, through iteration, _covid_list_ is created;

  * <ins>*Top10*</ins>: it is involved in returning the 10 most abundant associations between genes and diseases;
 
  * <ins>*AssociationDisease*</ins>: it is involved in returning a list of diseases that are associated to the given gene by its symbol;
  * <ins>*AssociationGenes*</ins>: it is involved in returning a list of the genes associated to the given disease by its name.


***part_3*** is connected with *part_1.py* since it imports it. Furthermore, it contains several *@app_route* decorators which intend to map the URLs to a specific function that will handle the logic for that URL. It will create fourteen pages:
  * */main*: shows the nine possible choices the user can select;
  * */MD*: shows the output of *Metadata* class;
  * */Sem*: shows the output of *Semantics* class;
  * */G*: shows the output of *Genes* class;
  * */P4*: shows ;
  * */SenG*: shows ;
  * */D*: shows the output of *Diseases* class;
  * */P6*: shows;
  * */SenD*: shows;
  * */T10*: shows the output of *Top10* class;
  * */P8*: shows;
  * */AD*: shows;
  * */P9*: shows;
  * */AG*: shows.
***templates*** folder contains fourteen *.html* files
