'''from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("dd.html")

@app.route('/login', methods=['GET', 'POST'])
def login2():
    if request.method == "POST":
        car_brand = request.form.get("cars", None)
        if car_brand!=None:
            return render_template("web_scraper.html", car_brand = car_brand)
    return render_template("web_scraper.html")

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
#from flask import render_template
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def build_plot():

    img = io.BytesIO()

    y = [1,2,3,4,5]
    x = [0,2,1,3,4]
    plt.plot(x,y)
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()

    return '<img src="data:image/png;base64,{}">'.format(plot_url)

if __name__ == '__main__':
    app.debug = True
    app.run()'''

from flask import Flask, render_template, request, url_for, redirect
import json, pandas as pd

app = Flask(__name__)

@app.route("/login")
def GetData():
    df = pd.read_csv("datasets/results.csv")
    temp = df.to_dict('records')
    columnNames = df.columns.values
    return render_template('record.html', records=temp, colnames=columnNames)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/web_scraper', methods=['GET', 'POST'])
def scraper_page():
    if request.method == "POST":
        product = request.form.get("dataset", None)
        if product == 'Shoes':
            df = pd.read_json("datasets/Shoes.json")
            temp = df.to_dict('records')
            columnNames = df.columns.values
            return render_template('record.html', records=temp, colnames=columnNames, product = product)
        elif product == 'Pants':
            df = pd.read_json("datasets/Pants.json")
            temp = df.to_dict('records')
            columnNames = df.columns.values
            return render_template('record.html', records=temp, colnames=columnNames, product = product)
        elif product == 'Shirts':
            df = pd.read_json("datasets/Shirts.json")
            temp = df.to_dict('records')
            columnNames = df.columns.values
            return render_template('record.html', records=temp, colnames=columnNames, product = product)
        elif product == 'Hats':
            df = pd.read_json("datasets/Hats.json")
            temp = df.to_dict('records')
            columnNames = df.columns.values
            return render_template('record.html', records=temp, colnames=columnNames, product = product)
    return render_template('record.html')

@app.route('/machine_learning')
def ml_page():
    return render_template('machine_learning.html')

@app.route('/product')
def product_page():
    if request.method == "POST":
        product = request.form.get("dataset1", None)
        if product == 'Choice 2':
            df = pd.read_json("datasets/Shoes.json")
            temp = df.to_dict('records')
            columnNames = df.columns.values
            return render_template('product.html', records=temp, colnames=columnNames, product = product)
    return render_template('product.html')

if __name__ == "__main__":
    app.run(debug=True)