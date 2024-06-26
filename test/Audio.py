import speech_recognition as sr

# Crear un objeto de reconocimiento de voz
recognizer = sr.Recognizer()
# Utilizar el micrófono como fuente de audio
with sr.Microphone() as source:
    print("Esperando el comando 'matrícula' para comenzar a grabar...")
    # Ajusta automáticamente la sensibilidad del ruido de fondo durante 1 segundo
    # recognizer.adjust_for_ambient_noise(source)

    # Escuchar el audio del micrófono
    audio_data = recognizer.listen(source, timeout=5)

    try:
        # Reconocer el texto del audio
        text = recognizer.recognize_google(audio_data, language="es-ES")
        print(text)
        # Si el usuario dice "matrícula", comenzar a grabar
        if 'matrícula' in text.lower():
            print("Comenzando a grabar...")
            # Escuchar hasta que el usuario termine de hablar
            audio_data = recognizer.listen(source)
            print("Fin de la grabación.")

            # Reconocer el texto de la grabación
            recorded_text = recognizer.recognize_google(audio_data, language="es-ES")
            print("Texto grabado:", recorded_text)
        else:
            print("No se detectó la palabra 'matrícula'.")

    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print("Error al solicitar el reconocimiento de voz; {0}".format(e))
