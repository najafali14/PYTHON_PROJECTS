from flask import Flask, request, render_template, send_file
import fitz  # PyMuPDF
from io import BytesIO
import os
from datetime import datetime
# nextjs app

@app.route("/nextjs")
def NextJs():
    return render_template("nextjs.html")

# Nextjs certificate

@app.route('/certificateeab-6c040f234bc6-00-3f0oyrwkpua7q')
def index():
    return render_template('certificate.html')

@app.route('/generate-certificate', methods=['POST'])
def generate_certificate():
    try:
        name = request.form['name']
        email = request.form['email']
        CertificateData = {"name": name, "email": email}

        # Save data from CertificateData
        with open('CertificateDetails.txt', 'a') as file:
            file.write(str(CertificateData) + '\n')

        # Get the current date
        today_date = datetime.now().strftime("%B %d, %Y")  # Format: August 17, 2024


        # Path to the certificate template
        pdf_path = os.path.join(app.root_path, 'static', 'Certificate.pdf')

        if not os.path.exists(pdf_path):
            return "Certificate template not found", 404  # Return a 404 Not Found error

        # Open the existing PDF certificate template
        with fitz.open(pdf_path) as pdf_document:
            # Select the first page (assuming the certificate is on the first page)
            page = pdf_document[0]

            # Define the position and style for the name, date, and result
            name_position = (300, 275)  # Coordinates to place the name
            date_position = (330, 370)  # Coordinates to place the date


            name_font_size = 40  # Font size for the name
            date_font_size = 20  # Font size for the date


            # Add the user's name to the PDF
            page.insert_text(name_position, name, fontsize=name_font_size, fontname="helv", color=(0, 0, 0))
            # Add the current date to the PDF
            page.insert_text(date_position, today_date, fontsize=date_font_size, fontname="helv", color=(0, 0, 0))
            # Add the result to the PDF


            # Save the updated PDF to a BytesIO object
            buffer = BytesIO()
            pdf_document.save(buffer)
            buffer.seek(0)

        return send_file(buffer, as_attachment=True, download_name=f"certificate_{name}.pdf", mimetype='application/pdf')

    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return f"An error occurred: {e}", 500  # Return a 500 Internal Server Error with the error message




if __name__ == "__main__":
    app.run(debug=False)
