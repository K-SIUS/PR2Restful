import requests
#3 agentes deben legar a un acuerdo con la elección de 
#un número aleatorio usando Flask.
'''
La lógica será la siguiente.
Necesito que se generen números aleatorios de 3 en 3. (en llamadas independientes, uno cada "agente").
Si hay 2 o más iguales --> hay consenso
Sino, bucle. Print de cada tirada. 
Hasta ahí todo bien, pero como lo hacemos?
método de flask para /generar_aleatorio.
guardamos el aleatorio en memoria (variable (agent1,agent2,agent3) o array, habrá que ver).
método flask que /compare el valor de los valores y retorne true o false.

'''
generar_Aleatorios = "http://127.0.0.1:5000/random"
AñadirAgente = "http://127.0.0.1:5000/addAgent"
comprobarConsenso = "http://127.0.0.1:5000/compare"
AgentList = "http://127.0.0.1:5000/Agents"


acuerdo = False
#Por lo tanto el programa consistirá en un bucle hasta haber acuerdo
iteraciones= 0
while not acuerdo:
    iteraciones= iteraciones + 1 
    #generamos los agentes con los números aleatorios
    requests.post(AñadirAgente, json = {'random' : 'r'})
    #pedimos los agentes generados aleatorios
    lista= requests.get(AgentList).json()
    #comprobamos si hay consenso
    comprobante = requests.get(comprobarConsenso).json()
    print(lista, comprobante)
    #si hay consenso sale del bucle, sino no
    if comprobante == False:
        acuerdo = False
    elif comprobante == True:
        print("Hay acuerdo")
        acuerdo = True
        #guardamos registro de los intentos.
        print("número de intentos: %i"%iteraciones)

