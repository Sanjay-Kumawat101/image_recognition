from flask import Flask, render_template, request
import requests, os

app = Flask(__name__)

# Replace with your Azure endpoint and key
endpoint = os.getenv("endpoint")
subscription_key = os.getenv("subscription_key")

print("KEY FOUND:", bool(key))
print("ENDPOINT FOUND:", bool(endpoint))

analyze_url = endpoint + "/vision/v3.2/analyze"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        image = request.files["image"]
        image_data = image.read()

        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Content-Type': 'application/octet-stream'
        }
        params = {'visualFeatures': 'Description,Tags,Objects'}

        response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
        
        if response.status_code != 200:
            print("Azure API Error:", response.text)

        result = response.json()

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
