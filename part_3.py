# part 3
from flask import Flask
from flask import render_template, request
from part_1 import Registry

app = Flask(__name__)

@app.route('/')
def index_page():
	r = Registry().registry()  # guides the program to the correct output
	l = Registry().links()
	return render_template('0_homepage.html', registry = r, links = l, length = 9)

@app.route('/MD') #metadata 
def first_page():
	output = Registry().link_metadata() # link from part 1
	return render_template('1_metadata.html', result = output) # html template

@app.route('/Sem') #general semantics
def second_page():
	output = Registry().link_semantics() 
	return render_template('2_general_semantics.html', result = output) 

@app.route('/G') #genes
def third_page():
	output = Registry().link_geneNum()
	return render_template('3_genes.html', result = output)

@app.route('/P4') # input for classes 4 
def fourthuser_page():
	output = Registry().link_prefour()
	return render_template('user_genesentences.html', result = output) 


@app.route('/SenG') #sentences genes
def fourth_page():
	output = Registry().link_geneSent().search_covid(request.args.get('gene'))
	return render_template('4_sentences_g.html', result = output)
 
@app.route('/D') #disease
def fifth_page():
	output = Registry().link_diseaseNum()
	return render_template('5_diseases.html', result = output)

@app.route('/P6') # input for class 6 
def sixthuser_page():
	output=Registry().link_presixth()
	return render_template('user_diseasesentences.html', result = output)

@app.route('/SenD') #sentences 
def sixth_page():
	output = Registry().link_disSent().search_covid(request.args.get('disease'))
	return render_template('6_sentences_d.html', result = output)

@app.route('/T10') #top ten
def seventh_page():
	output = Registry().link_top10()
	return render_template('7_top_ten.html', result = output)


@app.route('/P8') # input for class 8
def eighthuser_page():
	output=Registry().link_prefour() 
	return render_template('user_eight.html', result = output)


@app.route('/AD') #association disease
def eight_page():
	output = Registry().link_get_geneDisease().search_genes(request.args.get('gene'))
	return render_template('8_association_d.html', result = output)


@app.route('/P9') # input for class 9
def ninthuser_page():
	output=Registry().link_presixth()
	return render_template('user_nine.html', result = output)

@app.route('/AG') #association genes
def ninth_page():
	output = Registry().link_get_DiseaseGene().search_diseases(request.args.get('disease'))
	return render_template('9_association_g.html', result = output)


if __name__ == '__main__':
    app.run(port = 3000)
