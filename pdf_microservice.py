"""
File Name: pdf_microservice.py
Description: Takes JSON object as input and returns link to generated PDF file
"""

from flask import Flask, request, jsonify, send_file
from fpdf import FPDF

app = Flask(__name__)

def validate_input(data):
    """Validates class schedule input is a dictionary"""
    if not isinstance(data, dict):
        return False
    return True

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    """Takes data from JSON object and writes to PDF"""
    # Get JSON object containing class schedule
    data = request.get_json()

    # Check data is in dictionary format
    if validate_input(data) is False:
        return jsonify({"message": "Invalid structure. Class schedule should be in dictionary format"})

    # Create PDF which will be saved in directory this code will be run
    pdf = FPDF()

    # Creates new page in PDF
    pdf.add_page()
    pdf.set_font("Courier", size=16)

    # Write class schedule to PDF
    for quarter, classes in data.items():
        # Add each quarter as a header
        pdf.cell(300, 10, txt=quarter, ln=True, align='L')
        # Add each class below quarter
        for class_id, class_name in classes.items():
            pdf.cell(300, 10, txt=f"{class_id} - {class_name}", ln=True, align='L')
        # Add space between each quarter
        pdf.cell(300, 20, txt = " ", ln=True, align='L')

    # Save pdf as class_schedule.pdf to current directory
    pdf.output("class_schedule.pdf")

    # Return link to PDF
    return jsonify({"message": "PDF generated successfully", "pdf": "http://127.0.0.1:5001/get_pdf"})

@app.route('/get_pdf', methods=['GET'])
def get_pdf():
    # get_pdf endpoint handles requests to download PDF
    return send_file("class_schedule.pdf", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5001)







