import cv2
import matplotlib.pyplot as plt

def task3_facial_recognition(modelo_cara_path, imagen_path, output_filename):
    modelo_cara = cv2.CascadeClassifier(modelo_cara_path)
    imagen = cv2.imread(imagen_path)
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    caras = modelo_cara.detectMultiScale(imagen_gris)

    for (x, y, w, h) in caras:
        cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)

    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    plt.imsave(output_filename, imagen_rgb)

    return f"Face detection done successfully! Output saved as {output_filename}"
