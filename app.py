from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, Raju Garu"

if __name__ == "__main__":
    # This block is executed when the script is run directly
    app.run(host="0.0.0.0", port=5000, debug=True)
