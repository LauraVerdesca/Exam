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
- ***part_3*** is connected with *part_1.py* since it imports it. Furthermore, it contains several *@app_route* decorators which intend to map the URLs to a specific function that will handle the logic for that URL. It will create fourteen pages:
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
- ***templates*** folder contains fourteen *.html* files

## Project specification GAIA

- ***part_1.py*** is connected with *part_2.py* since it imports it. 

It contains only one class, called <ins>*Registry*</ins>, which aims to contain all the functions calling analytical operations defined in *part_2.py* file.

The two files are opened through **Pandas**: in thsi way they are transformed in two dataframes, easily manipulated through the functions of the previously mentioned library. 

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
- ***part_3*** is connected with *part_1.py* since it imports it. Furthermore, it contains several *@app_route* decorators which intend to map the URLs to a specific function that will handle the logic for that URL. It will create fourteen pages:
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
- ***templates*** folder contains fourteen *.html* files
