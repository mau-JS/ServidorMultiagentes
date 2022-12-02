# TC2008B. Sistemas Multiagentes y Gráficas Computacionales
# Python flask server to interact with Unity. Based on the code provided by Sergio Ruiz.
# Octavio Navarro. November 2022

from flask import Flask, request, jsonify
from boids.boid import Boid
import numpy as np
import os
import mesa
import random
import pandas as pd
from agent import *

with open('posicion.json', 'r') as archivo:
  posicionInicial = json.load(archivo)

conteoSteps = 0
conteoAgente = -1
def updatePositions(flock):
    global conteoSteps
    global conteoAgente
    conteoSteps = conteoSteps + 1
    positions = []
    for boid in flock:
        conteoAgente = conteoAgente + 1
        boid.apply_behaviour(flock)
        boid.update(conteoSteps,conteoAgente)
        boid.edges()
        positions.append((boid.id, boid.position))
    conteoAgente = -1
    return positions

def positionsToJSON(positions):
    posDICT = []
    for id, p in positions:
        pos = {
            "boidId" : str(id),
            "x" : float(p.x),
            "y" : float(p.z),
            "z" : float(p.y)
        }
        posDICT.append(pos)
    return jsonify({'positions':posDICT})

# Size of the board:
width = 50
height = 50

# Set the number of agents here:
flock = []

app = Flask("Boids example", static_url_path='')
port=int(os.getenv('PORT',8000))

@app.route('/', methods=['POST', 'GET'])
def boidsPosition():
    if request.method == 'GET':
        positions = updatePositions(flock)
        return positionsToJSON(positions)
    elif request.method == 'POST':
        return "Post request from Boids example\n"

@app.route('/init', methods=['POST', 'GET'])
def boidsInit():
    global flock
    if request.method == 'GET':
        # Set the number of agents here:
        flock = [Boid(*posicionInicial[id], width, height, id) for id in range(20)]

        return jsonify({"num_agents":20, "w": 50, "h": 50})
    elif request.method == 'POST':
        return "Post request from init\n"

if __name__=='__main__':
    app.run(host="0.0.0.0", port=port, debug=True)