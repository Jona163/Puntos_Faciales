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
       'left_eye_outer_corner_x': [None], 'left_eye_outer_corner_y': [None],
        'right_eye_inner_corner_x': [None], 'right_eye_inner_corner_y': [None],
        'right_eye_outer_corner_x': [None], 'right_eye_outer_corner_y': [None],
        'left_eyebrow_inner_end_x': [None], 'left_eyebrow_inner_end_y': [None],
        'left_eyebrow_outer_end_x': [None], 'left_eyebrow_outer_end_y': [None],
        'right_eyebrow_inner_end_x': [None], 'right_eyebrow_inner_end_y': [None],
        'right_eyebrow_outer_end_x': [None], 'right_eyebrow_outer_end_y': [None],
        'nose_tip_x': [None], 'nose_tip_y': [None],
        'mouth_left_corner_x': [None], 'mouth_left_corner_y': [None],
        'mouth_right_corner_x': [None], 'mouth_right_corner_y': [None],
        'mouth_center_top_lip_x': [None], 'mouth_center_top_lip_y': [None],
        'mouth_center_bottom_lip_x': [None], 'mouth_center_bottom_lip_y': [None],
        'Image': [image_path]
    }

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            landmarks_mapping = {
                33: 'left_eye_center', 263: 'right_eye_center',
                133: 'left_eye_inner_corner', 362: 'right_eye_inner_corner',
