import re
from pypdf import PdfReader
from model import create_tables, VehicleEventRecord

# Crear las tablas en la base de datos
create_tables()

# Leer el documento PDF
reader = PdfReader("documentos.pdf")

# Expresión regular para capturar los datos necesarios
pattern = r"(\w+)\s+(\d{2}/\d{2}/\d{4})\s+(\d{2}:\d{2})\s+.*?:\s+(.*?)\s+(\d+)"

# Iterar sobre las páginas del documento
for page in reader.pages:
    lines = page.extract_text().splitlines()

    # Iterar sobre cada línea de la página
    for line in lines:
        # Buscar la información en la línea usando la expresión regular
        match = re.search(pattern, line)
        if match:
            plate_code = match.group(1)
            date = match.group(2)
            time = match.group(3)
            description = match.group(4).strip()
            amount = match.group(5)

            # Crear el registro de evento del vehículo
            event = VehicleEventRecord(
                plateCode=plate_code,
                date=date,
                description=description,
                dangerLevel=int(amount)
            )
            event.save()

# Ejemplo de cómo imprimir los resultados para verificar
for page in reader.pages:
    lines = page.extract_text().splitlines()
    for line in lines:
        match = re.search(pattern, line)
        if match:
            plate_code = match.group(1)
            date = match.group(2)
            description = match.group(4).strip()
            amount = match.group(5)
            print(f"{plate_code}, {date}, {description}, {amount}")
