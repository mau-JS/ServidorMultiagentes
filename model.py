import numpy as np
import mesa
import random

from agent import *

vec = []
posicionAgent = []
posicionStep = []
choices = (CarAgent1,CarAgent2,CarAgent3,CarAgent4)
selecciones = []

def compute_gini(model):
    acumulado = 0
    for i in model.schedule.agents:
        if (isinstance(i,CarAgent1) or isinstance(i,CarAgent2) or isinstance(i,CarAgent3) or isinstance(i,CarAgent4)):
            acumulado += i.conteo
    return acumulado


#Cambiar esta linea
for i in range (20):
    #CarAgentType1
    eleccion = random.choice(choices)

    if eleccion == CarAgent1:
        m = random.randrange(0,10)
        n = random.choice([25,26,28,29,30])
        a = [m,n]
        vec.append(a)
        selecciones.append(eleccion)

    if eleccion == CarAgent2:
        m = random.randrange(40,50)
        n = random.choice([20,21,23,24])
        a = [m,n]
        vec.append(a)
        selecciones.append(eleccion)

    if eleccion == CarAgent3:
        m = random.choice([20,21,23,24])
        n = random.randrange(0,10)
        a = [m,n]
        vec.append(a)
        selecciones.append(eleccion)

    if eleccion == CarAgent4:
        m = random.choice([26,28,29])
        n = random.randrange(40,50)
        a = [m,n]
        vec.append(a)
        selecciones.append(eleccion)

posicionJSON = json.dumps(vec)


with open("posicion.json", "w") as outfile:
    outfile.write(posicionJSON)

class CarModel(mesa.Model):
    def __init__(self,N,width,height):
        global vec
        self.numAgentsCar = N
        conteo = 0

        self.grid = mesa.space.MultiGrid(width,height,True)
        self.schedule = mesa.time.BaseScheduler(self)
        self.running = True
        self.clases = (CarAgent1,CarAgent2,CarAgent3,CarAgent4)
        

        for i in range(10,20):
            for j in range(10,20):
                c = entornoAgent("E" + str(conteo), self)
                self.schedule.add(c)
                x = i
                y = j
                self.grid.place_agent(c,(x,y))
                conteo += 1

        for i in range(10,20):
            for j in range(30,40):
                c = entornoAgent("E" + str(conteo), self)
                self.schedule.add(c)
                x = i
                y = j
                self.grid.place_agent(c,(x,y))
                conteo += 1

        for i in range(30,40):
            for j in range(10,20):
                c = entornoAgent("E" + str(conteo), self)
                self.schedule.add(c)
                x = i
                y = j
                self.grid.place_agent(c,(x,y))
                conteo += 1

        for i in range(30,40):
            for j in range(30,40):
                c = entornoAgent("E" + str(conteo), self)
                self.schedule.add(c)
                x = i
                y = j
                self.grid.place_agent(c,(x,y))
                conteo += 1

        for i in range(self.numAgentsCar):
            #a = random.choice(self.clases)("C" + str(i),self)
            a = selecciones[i]("C" + str(i),self)
            self.schedule.add(a)
            x,y = vec[i]
            self.grid.place_agent(a,(x,y))





        s1 = SemaforoAgent1("S" + str(1),self)
        self.schedule.add(s1)
        x1 = 19
        y1 = 27
        self.grid.place_agent(s1,(x1,y1))

        s2 = SemaforoAgent2("S_2" + str(2),self)
        self.schedule.add(s2)
        x1 = 30
        y1 = 22
        self.grid.place_agent(s2,(x1,y1))

        s3 = SemaforoAgent3("S_3" + str(3),self)
        self.schedule.add(s3)
        x1 = 22
        y1 = 19
        self.grid.place_agent(s3,(x1,y1))

        s4 = SemaforoAgent4("S_4" + str(3),self)
        self.schedule.add(s4)
        x1 = 27
        y1 = 30
        self.grid.place_agent(s4,(x1,y1))

        s5 = SemaforoAgent3("S_5" + str(3),self)
        self.schedule.add(s5)
        x1 = 22
        y1 = 39
        self.grid.place_agent(s5,(x1,y1))

        s6 = SemaforoAgent4("S_6" + str(4),self)
        self.schedule.add(s6)
        x1 = 27
        y1 = 10
        self.grid.place_agent(s6,(x1,y1))

        self.datacollector = mesa.DataCollector(
            model_reporters={"Tiempo total de coches en alto total": compute_gini}
        )

    def step(self):
        posicionStep = []
        self.datacollector.collect(self)
        self.schedule.step()
        for i in self.schedule.agents:
            if(isinstance(i,CarAgent1) or isinstance(i,CarAgent2) or isinstance(i,CarAgent3) or isinstance(i,CarAgent4)):
                posicionStep.append(i.velocidadAgente)

        posicionAgent.append(posicionStep)

        json_object = json.dumps(posicionAgent, indent = 4)

        with open("sample.json", "w") as outfile:
            outfile.write(json_object)