from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('loign.html')

@app.route('/home')
def index():
    return render_template('index.html')

if __name__ == "__main__":
	app.run()