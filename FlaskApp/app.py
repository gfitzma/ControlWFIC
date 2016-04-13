# I'll let you guys take a look at this, 
# this is all new to me so I might be doing
# it in a dumb way

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route('/showTraffic')
def showTraffic():
	## TODO - get objects from sflow collector
    return render_template('showTraffic.html')

@app.route('/showErrors')
def showErrors():
	return render_template('showErrors.html')

@app.route('/showPOE')
def showPOE():
    return render_template('showPOE.html')

@app.route('/showAbout')
def showAbout():
    return render_template('about.html')


if __name__ == "__main__":
	app.run()
