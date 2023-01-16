from flask import Flask

app = Flask(__name__)      

@app.route("/")
def home():
    return "Welcome 🏡"

@app.route("/add")
def add():
    return {
        "name":"manu",
        "status":"record added successfully"
    }

@app.route("/display")
def display():
    return {
        "name":"Manu",
        "age":23,
        "housename":"Pothiyil"
    }
    
if __name__ == "__main__":
    app.run("0.0.0.0")
