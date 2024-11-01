import requests

# URL for the pdf microservice
url = 'http://127.0.0.1:5001/generate_pdf'

# Example data to pass through to microservice
data = {
    "Winter 2024": {
        "CS290": "Web Development",
        "CS261": "Data Structures"
    },
    "Spring 2025": {
        "CS271": "Computer Architecture",
    },
    "Summer 2025": {
        "CS325": "Analysis of Algorithms"
    }
}

# Request includes url and data
response = requests.post(url, json=data)

# Print contents of JSON response
print(response.json())