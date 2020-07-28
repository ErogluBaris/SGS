from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("/html/main.html")

@app.route("/iletisim")
def contact():
    return render_template("/html/contact.html")

@app.route("/urunler")
def products():
    return render_template("/html/products.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)