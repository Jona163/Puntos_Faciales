# Autor: Jonathan Hernández
# Fecha: 27 octubre 2024
# Descripción: Graficacion puntos faciales.
# GitHub: https://github.com/Jona163

#Importaciones requeridas
import os
import re
from flask import Flask, request, render_template, redirect
import cv2
import mediapipe as mp
import pandas as pd

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Inicializar MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5)

def sanitize_filename(filename):
    return re.sub(r'[^a-zA-Z0-9_.-]', '_', filename)

def draw_cross(image, center, size=5, color=(0, 0, 255)):
    """Dibuja una cruz en la imagen en la posición especificada."""
   x, y = center
    cv2.line(image, (x - size, y - size), (x + size, y + size), color, 2)
    cv2.line(image, (x + size, y - size), (x - size, y + size), color, 2)

def process_image(image_path):
    image = cv2.imread(image_path)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_image)

    facial_points_dict = {
        'left_eye_center_x': [None], 'left_eye_center_y': [None],
        'right_eye_center_x': [None], 'right_eye_center_y': [None],
        'left_eye_inner_corner_x': [None], 'left_eye_inner_corner_y': [None],
