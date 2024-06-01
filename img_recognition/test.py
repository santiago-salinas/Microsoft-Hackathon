import re

import cv2
import simplelpr

plateRegex = r'[A-Za-z]{3}\s+[\d]{4}'


def list_countries(eng):
    print('List of available countries:')
    for i in range(0, eng.numSupportedCountries):
        print(eng.get_countryCode(i))


# Configuración del motor de simplelpr
setupP = simplelpr.EngineSetupParms()
eng = simplelpr.SimpleLPR(setupP)

proc = eng.createProcessor()
proc.plateRegionDetectionEnabled = True
proc.cropToPlateRegionEnabled = True


# Función para procesar cada cuadro de video
def process_frame(frame):
    # Convertir la imagen de OpenCV (BGR) a formato compatible con simplelpr (RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cds = proc.analyze(rgb_frame)

    # Imprimir las matrículas detectadas
    for cd in cds:
        for m in cd.matches:
            if re.match(plateRegex, m.text):
                display_frame = rgb_frame.copy()

                cv2.putText(display_frame, f"Plate: {m.text}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
                cv2.imshow("Cropped Plate", display_frame)
                cv2.waitKey(1)
        # if cd.chars & cd.confidence:
        #     print(f"Plate: {cd.chars}, Confidence: {cd.confidence}")


# Capturar video desde la cámara de la notebook
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Procesar el cuadro de video
    process_frame(frame)

    # Mostrar el cuadro de video
    cv2.imshow('Video', frame)

    # Salir del bucle al presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura de video y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
