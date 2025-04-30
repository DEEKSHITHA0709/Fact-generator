from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Function to fetch a random fact
def generate_random_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    try:
        response = requests.get(url)
        response.raise_for_status()
        fact_data = response.json()
        return fact_data.get("text", "No fact found.")
    except requests.exceptions.RequestException as e:
        return f"Error fetching fact: {e}"

# API route to serve random fact
@app.route("/random-fact", methods=["GET"])
def get_fact():
    fact = generate_random_fact()
    return jsonify({"fact": fact})

# Route to serve the HTML page
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
