## Project specification
Each part has it's own classes, as stated before. In details:
- ***part_1.py*** is connected with *part_2.py* since it imports it. Furthermore, it contains only one class, called <ins>*Registry*</ins>, which aims to contain all the functions calling analytical operations defined in *part_2.py* file;
- ***part_2.py*** contains eleven classes:
  * <ins>*Metadata*</ins>:;
  * <ins>*Semantics*</ins>:;
  * <ins>*Genes*</ins>:;
  * <ins>*Pre4*</ins>:;
  * <ins>*SentencesG*</ins>:;
  * <ins>*Diseases*</ins>:;
  * <ins>*Pre6*</ins>:;
  * <ins>*SentencesD*</ins>:;
  * <ins>*Top10*</ins>:;
  * <ins>*AssociationDisease*</ins>:;
  * <ins>*AssociationGenes*</ins>:;
- ***part_3*** is connected with *part_1.py* since it imports it. Furthermore, it contains several *@app_route* decorators which intend to map the URLs to a specific function that will handle the logic for that URL. It will create fourteen pages:
  * */main*:;
  * */MD*:;
  * */Sem*:;
  * */G*:;
  * */P4*:;
  * */SenG*:;
  * */D*:;
  * */P6*:;
  * */SenD*:;
  * */T10*:;
  * */P8*:;
  * */AD*:;
  * */P9*:;
  * */AG*:;
- ***templates*** folder contains fourteen *.html* files
