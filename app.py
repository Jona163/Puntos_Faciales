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
