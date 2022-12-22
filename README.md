# PR2Restful
Práctica 2 de arquitecturas avanzadas consistente en el uso de Flask y de Rest para implementar un consenso entre agentes.
Practica 2 Restful usando Flask. Arquitecturas Avanzadas
Ander Sarrión Martín

La lógica implementada entre app y programa es la siguiente.
El programa solicita a la aplicación que genere 3 numeros aleatorios.
Existen 3 agentes en la aplicación, a los que acopla esos nuevos valores.
El programa solicita esos 3 agentes con los nuevos valores aleatorios, para imprimirlos por pantalla.
Además, este solicita que compruebe si hay algún valor repetido y que este devuelva True o False según se dé.
El programa únicamente imprime por pantalla lo que le llega y guarda un conteo del número de iteraciones necesarias.

El esqueleto ha sido sacado del código facilitado en clase de  U2-RPC, y se ha basado en el mismo funcionamiento.
Además, se ha tenido en consideración la página marcada https://realpython.com/api-integration-in-python/ para entender
como funciona el import de requests
Atendiendo al enunciado de la práctica, no considero que haya algún tipo de comunicación entre agentes, pues estos están todos en una lista y únicamente comparan valores. (no es como si fueran dos conexiones de socket distintas).
Quizás ese no era el ejercicio y este consistía en ejecutar 3 terminales diferentes 3 agentes, pero como lo he leído en el enunciado, y dado el planteamiento de bucles, me parece que la forma como se ha programado es mejor.

A pesar de todo, y por lo tanto, no creo que este método sirva para establecer un grupo de comunicacionesde manera más optima que los sockets, pese a que sea mucho más liviano y desde luego, más manejable que estos.
