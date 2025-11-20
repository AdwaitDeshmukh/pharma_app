from flask import Flask
from utils.db import init_db

app = Flask(__name__)

# initialize DB tables on app start
init_db()

@app.route("/")
def home():
    return "Pharma App Running Successfully!"

if __name__ == "__main__":
    app.run(debug=True)
