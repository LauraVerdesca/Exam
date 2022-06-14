# part 3
from flask import Flask
from flask import render_template, request
from part_1 import Registry

app = Flask(__name__)

@app.route('/main')
def index_page():
	r = Registry().registry()  # guides the program to the correct output
	l = Registry().links()
	return render_template('homepage.html', registry = r, links = l, length = 9)

@app.route('/MD') #metadata 
def first_page():
	output = Registry().link_metadata() # link from part 1
	return render_template('metadata.html', result = output) # html template

@app.route('/Sem') #general semantics
def second_page():
	output = Registry().link_semantics() 
	return render_template('general_semantics.html', result = output) 

@app.route('/G') #genes
def third_page():
	output = Registry().link_geneNum()
	return render_template('genes.html', result = output)

@app.route('/P4') # input for classes 4 
def fourthuser_page():
	output = Registry().link_prefour()
	return render_template('user_genesentences.html', result = output) 


@app.route('/SenG') #sentences genes
def fourth_page():
	output = Registry().link_geneSent().search_covid(request.args.get('gene'))
	return render_template('sentences_g.html', result = output)
 
@app.route('/D') #disease
def fifth_page():
	output = Registry().link_diseaseNum()
	return render_template('diseases.html', result = output)

@app.route('/P6') # input for class 6 
def sixthuser_page():
	output=Registry().link_presixth()
	return render_template('user_diseasesentences.html', result = output)

@app.route('/SenD') #sentences 
def sixth_page():
	output = Registry().link_disSent().search_covid(request.args.get('disease'))
	return render_template('sentences_d.html', result = output)

@app.route('/T10') #top ten
def seventh_page():
	output = Registry().link_top10()
	return render_template('top_ten.html', result = output)


@app.route('/P8') # input for class 8
def eighthuser_page():
	output=Registry().link_prefour() 
	return render_template('user_usereight.html', result = output)


@app.route('/AD') #association disease
def eight_page():
	output = Registry().link_get_geneDisease().search_genes(request.args.get('gene'))
	return render_template('association_d.html', result = output)


@app.route('/P9') # input for class 9
def ninthuser_page():
	output=Registry().link_presixth()
	return render_template('user_nine.html', result = output)

@app.route('/AG') #association genes
def ninth_page():
	output = Registry().link_get_DiseaseGene().search_diseases(request.args.get('disease'))
	return render_template('association_g.html', result = output)


if __name__ == '__main__':
    app.run(port = 3000)
