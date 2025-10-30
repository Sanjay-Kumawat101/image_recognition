from flask import Flask, render_template, request
import requests, os

app = Flask(__name__)

# Replace with your Azure endpoint and key
endpoint = "https://cclproject.cognitiveservices.azure.com/"
subscription_key = "Evz2GeuMxF8jHY0GOuf2Z0A4ftI084C1W7V9rZlt6Du3DjJvYsdHJQQJ99BJACYeBjFXJ3w3AAAFACOGG6es"

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
        result = response.json()

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
