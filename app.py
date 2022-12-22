import json
from flask import Flask, request, jsonify
import random
#Based on: https://realpython.com/api-integration-in-python/
seed= 2022
random.seed(seed)
app = Flask(__name__)
#inicializo los agentes con numeros diferentes no sea cosa que
#el compare me devuelva true en la primera iteración
agente1= 0
agente2= 1
agente3= 2

agentes = [agente1,agente2,agente3]

#método que comparará el valor de los agentes y devolverá true o false
#según si ve que hay un valor igual o no
@app.get("/compare")
def compareAgentes():
    if((agentes[0] == agentes[1])|(agentes[0]== agentes[2])): 
        return jsonify(True)
    if(agentes[1] == agentes[2]):
        return jsonify(True)
    
    return jsonify(False)


@app.get("/random")
def get_random_number():
    return jsonify(random.randint(0,9))


@app.get("/Agents")
def get_things():
    return jsonify(agentes)

#metodo que genera 3 numeros aleatorios y actualiza los valores
#de la lista de agentes con esos nuevos numeros.
#devuelve la peticion de request
@app.post("/addAgent")
def add_Agente():
    if request.is_json:
        Nuevoagente = request.get_json()
        for i in range(3):
            agentes[i] = random.randint(0,9)
        return Nuevoagente, 201
    return {"error": "Request must be JSON"}, 415
