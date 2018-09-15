from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def papouf():
    return render_template('papouf.html')

@app.route('/waddels/')
def waddels():
    return render_template('waddels.html')

@app.route('/moumout/')
def moumout ():
    return render_template('moumout.html')

@app.route('/babykiki/')
def babykiki ():
    return render_template('babykiki.html')

@app.route('/blitz/')
def blitz ():
    return render_template('blitz.html')

@app.route('/doudou_rose/')
def doudou_rose ():
    return render_template('doudou_rose.html')

if __name__ == '__main__':
  # Run the app server on localhost:5000
  # app.run()
   app.run()