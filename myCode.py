from flask import Flask
from flask import render_template
from flask import request
import requests

app = Flask(__name__)


@app.route('/',  methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        # get url that the user has entered
        try:
            url = request.form['title']
            print(url)
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
