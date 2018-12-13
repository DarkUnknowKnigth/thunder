from flask import Flask
from flask import Flask,render_template,Blueprint
app = Flask(__name__)

@app.route('/x', methods=['GET'] )
def xmine():
    return render_template('x.html')
app.run(app)


