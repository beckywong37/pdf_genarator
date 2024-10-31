# pdf_generator
Generates PDF from JSON

## How to Request Data from PDF_Generator
Make a POST request to the microservice endpoint (/generate_pdf) and pass in the JSON formatted data. The Flask application is run locally and listens for incoming request.

Data should be in JSON format, structured as a dictionary of dictionaries. Below is an example of how the class schedule should be structured.

`data = {
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
}`

**Example Call:**

`response = requests.post('http://127.0.0.1:5001/generate_pdf', json=data)
`

## How to Receive Data from PDF Generator
1. Once POST request has been made to the /generate_pdf endpoint, the generate_pdf() will run
2. The JSON data will be validated to ensure it is the validate structure. If the data is not a valid dictionary, a JSON response with an error message is sent to the caller.
  `  if validate_input(data) is False:
        return jsonify({"message": "Invalid structure. Class schedule should be in dictionary format"})
`
3. If PDF generation was successful, the PDF will be saved to the current directory the code is run on:
`pdf.output("class_schedule.pdf")
`
4. The JSON response will include a confirmation message indicating that the PDF was successfully generated and a link to download the PDF.
`  return jsonify({"message": "PDF generated successfully", "pdf": "http://127.0.0.1:5001/get_pdf"})
`
5. To receive the JSON response on the client side:
`print(response.json())`
6. Users have two ways to access the PDF file. The PDF file will be stored on their local drive in the current directory the code is run in. Alternatively, users can click on the PDF link to initiate a GET request to the /get_pdf endpoint to download the PDF.

## UML Diagram
![image](https://github.com/user-attachments/assets/5be40096-695a-4d88-b008-3c8e6b8852e3)
