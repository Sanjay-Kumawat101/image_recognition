# AI Vision – Object Detection Web Application

🔗 **Live Application:** aivision-hmdvaafhbdhfawgc.eastus-01.azurewebsites.net

---

## Project Overview

**AI Vision** is a web-based application that uses **Azure Cognitive Services (Computer Vision API)** to analyze images and detect objects present in them. Users can upload an image through a simple web interface and the application returns AI-generated insights such as detected objects, tags and image description.

---

## Technologies Used

### Frontend

* HTML5
* CSS3
* Jinja2 (Flask Templates)

### Backend

* Python
* Flask Framework

### Cloud & AI Services

* Azure Cognitive Services – Computer Vision API
* Azure App Service (Web App)
* Azure Student Subscription

### DevOps

* GitHub
* GitHub Actions (CI/CD)

---

## Application Workflow

1. The user accesses the AI Vision web application.
2. An image is uploaded using the upload form.
3. The Flask backend reads the image as binary data.
4. The image is sent to the Azure Computer Vision API using a secure endpoint and subscription key.
5. Azure analyzes the image and returns detected objects, tags, and description.
6. The analysis result is displayed on the web interface.

---

## Azure Computer Vision API Details

**API Endpoint Used:**

```
POST /vision/v3.2/analyze
```

**Visual Features:**

* Description
* Tags
* Objects

---

## Security Configuration

* Azure **subscription key** and **endpoint** are not hardcoded.
* Sensitive values are stored securely using:

  * GitHub Secrets (for deployment)
  * Azure App Service Application Settings (runtime environment variables)


---

## Deployment

* The application is hosted on **Azure App Service**.
* Deployment is automated using **GitHub Actions**.

---

## Project Structure

```
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
|   └── script.js
├── requirements.txt
├── .github/workflows/
│   └── deploy.yml
└── README.md
```

---


