import route
import controller
import model
from flask import Flask,render_template,Blueprint
app = Flask(__name__)

@app.route('/')
def view():
    navigation={
        '1':{
            'href':'#index',
            'caption':'INDEX'
        },
        '2':{
            'href':'#ABOUT',
            'caption':'ABOUT'
        }
    }
    return render_template('view.html',nav=navigation.values())
app.run()

@app.route('/route')
def hello_world():
    return 'Hello, World!'