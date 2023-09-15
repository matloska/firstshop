from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

regions = {"WASHINGTON","NY"}

PRODUCTS_SERVICE_IP = "localhost"
PRODUCTS_SERVICE_PORT = 9876
PRODUCTS_SERVICE_URL = "http://"+PRODUCTS_SERVICE_IP+":"+str(PRODUCTS_SERVICE_PORT)+"/api"
print(PRODUCTS_SERVICE_URL)

@app.route("/", methods=['GET'])
def homepage():
    return render_template("main.html")

@app.route("/news/")
@app.route("/news/<string:region>")
def news(region=None):
    if region:
        if str.upper(region) not in regions:
            region = None
    return render_template("news.html", region=region)

@app.route("/products/")

def products():
    req = requests.get(PRODUCTS_SERVICE_URL+"/products")
    product_list = req.json()
    for p in product_list:
        print(p)
    return render_template("products.html", product_list=product_list)

if __name__ == "__main__":
    app.run(debug=True)

