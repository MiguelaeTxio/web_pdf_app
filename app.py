from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import os

app = Flask(__name__)

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Informacion de la Persona', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']
    dni = request.form['dni']
    localidad = request.form['localidad']

    pdf = PDF()
    pdf.add_page()
    pdf.chapter_title('Datos Personales')
    pdf.chapter_body(f'Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nDNI: {dni}\nLocalidad: {localidad}')

    #pdf_output = 'informacion_persona.pdf'
    #pdf.output(pdf_output)

    pdf_output = os.path.join(os.getcwd(), 'informacion_persona.pdf')
    pdf.output(pdf_output)


    return send_file(pdf_output, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)


