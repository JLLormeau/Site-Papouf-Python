from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/moumout/')
def moumout ():
    return render_template('moumout.html')

@app.route('/babykiki/')
def babykiki ():
    return render_template('babykiki.html')

if __name__ == '__main__':
  # Run the app server on localhost:5000
  # app.run()
   app.run()