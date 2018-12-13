from flask import Flask
from flask import Flask,render_template,Blueprint
app = Flask(__name__)

navigation={
        '1':{
            'href':'#index',
            'caption':'INDEX'
        },
        '2':{
            'href':'#ABOUT',
            'caption':'ABOUT'
        },
        '3':{
            'href':'#op1',
            'caption':'OP1'
        },
        '4':{
            'href':'#op2',
            'caption':'OP2'
        },
    }
cards=[1,2]

@app.route( '/escandon', methods=['GET'])
def escandon():
	return render_template('layout.html',nav=navigation.values(),card=cards)

@app.route('/')
def view():
    
    return render_template('view.html',nav=navigation.values(),card=cards)

@app.route( '/y', methods=['GET'] )
def y():
	return render_template('y.html')

@app.route( '/houston', methods=['GET'] )
def houston():
	return render_template('houston.html')

@app.route( '/card', methods=['GET'] )
def card():
	return render_template('card')

@app.route( '/card', methods=['GET'] )
def card():
	return render_template('card')

@app.route( '/card', methods=['GET'] )
def card():
	return render_template('card')

@app.route( '/card', methods=['GET'] )
def card():
	return render_template('card')

@app.route( '/ass', methods=['GET'] )
def ass():
	return render_template('ass')

@app.route( '/ass', methods=['GET'] )
def ass():
	return render_template('ass')

@app.route( '/card', methods=['GET'] )
def card():
	return render_template('card')

@app.route( '/card', methods=['GET'] )
def card():
	return render_template('card')

@app.route( '/card', methods=['GET'] )
def card():
	return render_template('card')

@app.route( '/card', methods=['GET'] )
def card():
	return render_template('card')

@app.route( '/card', methods=['GET'] )
def card():
	return render_template('card')

@app.route( '/card', methods=['GET'] )
def card():
	return render_template('card')

@app.route( '/card', methods=['GET'] )
def card():
	return render_template('card')

@app.route( '/card', methods=['GET'] )
def card():
	return render_template('card')

@app.route( '/card', methods=['GET'] )
def card():
	return render_template('card')

@app.route( '/card', methods=['GET'] )
def card():
	return render_template('card')