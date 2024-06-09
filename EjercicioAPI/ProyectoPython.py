import requests
from tabulate import tabulate
from fpdf import FPDF

def get_request(url):
    response = requests.get(url)
    return response.json()

def format_response(response):
    data = [list(item.values()) for item in response]
    return data

def print_table(data):
    print(tabulate(data, tablefmt="grid"))

def export_to_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Encabezado de la tabla
    headers = ["UserID", "ID", "Title", "Body"]

    # Agregar encabezados a la tabla
    for header in headers:
        pdf.cell(40, 10, header, border=1)
    
    pdf.ln()

    # Agregar filas de datos a la tabla
    for row in data:
        for item in row:
            pdf.cell(40, 10, str(item), border=1)
        pdf.ln()

    pdf.output("table.pdf")

if __name__ == "__main__":
    # Defino la URL del endpoint de la API
    get_url = "https://jsonplaceholder.typicode.com/posts"

    # Realizo la solicitud GET utilizando la API, y devuelve un JSON
    get_response = get_request(get_url)

    # Formatea las respuestas en tablas
    get_data = format_response(get_response)

    # Imprime las respuestas en forma de tablas por consola
    print("GET Response:")
    print_table(get_data)

    # Exportar a PDF
    export_to_pdf(get_data)