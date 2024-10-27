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
