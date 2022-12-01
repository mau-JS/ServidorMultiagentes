import numpy as np
import mesa
import random
import pandas as pd
import json


#Coche carril superior a la derecha
class CarAgent1(mesa.Agent):
    global vectorPosiciones

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "purple"
        self.moverStatus = None
        self.seleccion = ""
        self.conteo = 0
        self.stopsSemaforo = None
    def moveAbajo(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x, y - 1)):
            self.newPos = (x , y - 1)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()


    def moveIzquierda(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x - 1, y)):
            self.newPos = (x - 1 , y)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()

    def moveArriba(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x, y + 1)):
            self.newPos = (x , y + 1)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()
#Seleccion2 izquierda
    def seleccionaDireccion(self):
        random1 = random.choice([20,21]) #Carril abajo derecha
        #random2 = random.randint(25,30)#Carril Arriba derecha

        #Cuadrícula izquierda

        if (self.pos[0] == random1 and (self.pos[1] == 29 or self.pos[1] == 28)) :

            tempSeleccion = random.choice(("arriba","derecha"))
            self.seleccion = tempSeleccion

            if self.seleccion == "arriba":
                self.moveArriba()

            elif self.seleccion == "derecha":
                self.verificaSemaforo()
        
        elif((self.pos[0] == 20 or self.pos[0] == 21 or self.pos[0] == 22) and (self.pos[1] == 41)):
            self.seleccion = "izquierda"
            self.moveIzquierda()
            

        elif(self.pos[0] == 9 and self.pos[1] >= 30):
            self.seleccion = "abajo"
            self.moveAbajo()    
        elif(self.pos[0] == 9 and self.pos[1] == 28):
            self.seleccion = "derecha"
            self.verificaSemaforo()

        #Cuadrícula derecha
        elif(self.pos[0] == 41 and self.pos[1] < 40 ):
            self.seleccion = "arriba"
            self.moveArriba()

        elif(self.pos[0] == 41 and self.pos[1] >= 40 ):
            self.seleccion = "izquierda"
            self.moveIzquierda()


        
        #Movimiento General
        elif self.seleccion == "derecha":
            self.verificaSemaforo()

        elif self.seleccion == "izquierda":
            self.moveIzquierda()

        elif self.seleccion == "arriba":
            self.moveArriba()

        elif self.seleccion == "abajo":
            self.moveAbajo()

        #Tercera Intersección CarAgent1

        else:
            self.verificaSemaforo()
        





    def stop(self):
        x,y = self.pos
        self.conteo += 1
        self.newPos = (x , y)
        self.model.grid.move_agent(self,self.newPos)
        self.velocidadAgente = {
            "x": str(self.newPos[0] - x),
            "y": str(self.newPos[1] - y)
            }

    def verificaSemaforo(self):
        celdasAlrededor = self.model.grid.get_neighbors(self.pos, moore = True, include_center = False, radius = 2)
        for i in celdasAlrededor:
            if (isinstance(i, SemaforoAgent1) or isinstance(i,SemaforoAgent3)):
                if(i.color == "red" or i.color == "yellow"):
                    self.stopsSemaforo = True
                    self.moverStatus = False
                    break
                elif(i.color == "green"):
                    self.stopsSemaforo = False
                    self.moverStatus = True
                    break
            else: 
                self.moverStatus = True
        if self.moverStatus == True:
            self.move()
            self.moverStatus = None
        elif self.moverStatus == False:
            self.stop()
            self.moverStatus = None
        else:
            self.move()
            self.moverStatus = None
#Coche carril inferior a la izquierda
    def move(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x + 1, y)):
            self.newPos = (x + 1 , y)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()
    def stop(self):
        x,y = self.pos
        self.newPos = (x , y)
        self.model.grid.move_agent(self,self.newPos)
        self.velocidadAgente = {
            "x": str(self.newPos[0] - x),
            "y": str(self.newPos[1] - y)
            }

    def step(self):
        self.seleccionaDireccion()
        if(self.stopsSemaforo == True):
            self.conteo += 1
        self.stopsSemaforo = None
        #for i in self.celdasAlrededor:
        #    print(str(self.unique_id) +" "+ str(self.celdasAlrededor))
        #self.move()

#Coche se dirige izquierda
class CarAgent2(mesa.Agent):
    global vectorPosiciones
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "orange"
        self.moverStatus = None
        self.seleccion = ""
        self.conteo = 0
        self.stopsSemaforo = None
    def moveAbajo(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x, y - 1)):
            self.newPos = (x , y - 1)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()


    def moveDerecha(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x + 1, y)):
            self.newPos = (x + 1 , y)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()

    def moveArriba(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x, y + 1)):
            self.newPos = (x , y + 1)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()

    def seleccionaDireccion(self):
        random1 = random.randint(28,29) #Carril abajo derecha
        #random2 = random.randint(25,30)#Carril Arriba derecha

        #Cuadrícula abajo derecha

        if (self.pos[0] == random1 and (self.pos[1] == 20 or self.pos[1] == 21)) :

            tempSeleccion = random.choice(("abajo","izquierda"))
            self.seleccion = tempSeleccion
            if self.seleccion == "abajo":
                self.moveAbajo()
            elif self.seleccion == "izquierda":
                self.verificaSemaforo()
        elif ((self.pos[0] == 27 or self.pos[0] == 28 or self.pos[0] == 29) and self.pos[1] == 8):
            self.seleccion = "derecha"
            self.moveDerecha()

        elif(self.pos[0] == 41 and self.pos[1] <= 19):
            self.seleccion = "arriba"
            self.moveArriba()

        elif(self.pos[0] == 41 and self.pos[1] == 20):
            self.seleccion = "izquierda"
            self.verificaSemaforo()

        #Cuadrícula abajo izquierda
        elif(self.pos[0] == 8 and self.pos[1] > 19 ):
            self.seleccion = "abajo"
            self.moveAbajo()

        elif(self.pos[0] == 8 and self.pos[1] < 9 ):
            self.seleccion = "derecha"
            self.moveDerecha()


        #Movimiento General
        elif self.seleccion == "derecha":
            self.moveDerecha()

        elif self.seleccion == "izquierda":
            self.verificaSemaforo()

        elif self.seleccion == "arriba":
            self.moveArriba()

        elif self.seleccion == "abajo":
            self.moveAbajo()

        #Tercera Intersección CarAgent1

        else:
            self.verificaSemaforo()

    def verificaSemaforo(self):
        celdasAlrededor = self.model.grid.get_neighbors(self.pos, moore = True, include_center = False, radius = 2)
        for i in celdasAlrededor:
            if (isinstance(i, SemaforoAgent2) or isinstance(i,SemaforoAgent4)):
                if(i.color == "red" or i.color == "yellow"):
                    self.stopsSemaforo = True
                    self.moverStatus = False
                    break
                elif(i.color == "green"):
                    self.stopsSemaforo = False
                    self.moverStatus = True
                    break
            else: 
                self.moverStatus = True

        if self.moverStatus == True:
            self.move()
            self.moverStatus = None
        elif self.moverStatus == False:
            self.stop()
            self.moverStatus = None
        else:
            self.move()
            self.moverStatus = None

    def stop(self):
        x,y = self.pos
        self.conteo += 1
        self.newPos = (x , y)
        self.model.grid.move_agent(self,self.newPos)
        self.velocidadAgente = {
            "x": str(self.newPos[0] - x),
            "y": str(self.newPos[1] - y)
            }

    def move(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x - 1, y)):
            self.newPos = (x - 1 , y)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()

    def step(self):
        self.seleccionaDireccion()
        if self.stopsSemaforo == True:
            self.conteo += 1


#Coche se dirige arriba
class CarAgent3(mesa.Agent):
    global vectorPosiciones
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "blue"
        self.moverStatus = None
        self.seleccion = ""
        self.conteo = 0
    def moveAbajo(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x, y - 1)):
            self.newPos = (x , y - 1)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()


    def moveDerecha(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x + 1, y)):
            self.newPos = (x + 1 , y)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()

    def moveIzquierda(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x - 1, y)):
            self.newPos = (x - 1 , y)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()
            
    def seleccionaDireccion(self):
         #Carril abajo derecha
        #random2 = random.randint(25,30)#Carril Arriba derecha

        #Cuadrícula izquierda

        if (self.pos[1] == 41 and self.pos[0] > 19):
            self.seleccion = "izquierda"
            self.moveIzquierda()

        elif (self.pos[0] == 5 and self.pos[1] == 41):
            self.seleccion = "abajo"
            self.moveAbajo()
        elif(self.pos[0] == 5 and self.pos[1] == 5):
            self.seleccion = "derecha"
            self.moveDerecha()
        elif(self.pos[0] == 21 and self.pos[1] == 5):
            self.seleccion = "arriba"
            self.verificaSemaforo()
        #Movimiento General

        elif self.seleccion == "derecha":
            self.moveDerecha()

        elif self.seleccion == "izquierda":
            self.moveIzquierda()

        elif self.seleccion == "arriba":
            self.verificaSemaforo()

        elif self.seleccion == "abajo":
            self.moveAbajo()

        #Tercera Intersección CarAgent1
        else:
            self.verificaSemaforo()
            

    def verificaSemaforo(self):
        celdasAlrededor = self.model.grid.get_neighbors(self.pos, moore = True, include_center = False, radius = 2)
        for i in celdasAlrededor:
            if (isinstance(i, SemaforoAgent3) or isinstance(i,SemaforoAgent2)):
                if(i.color == "red" or i.color == "yellow"):
                    self.moverStatus = False
                    break
                elif(i.color == "green"):
                    self.moverStatus = True
                    break
            else: 
                self.moverStatus = True

        if self.moverStatus == True:
            self.move()
            self.moverStatus = None
        elif self.moverStatus == False:
            self.stop()
            self.moverStatus = None
        else:
            self.move()
            self.moverStatus = None
            
    def stop(self):
        x,y = self.pos
        self.conteo += 1
        self.newPos = (x , y)
        self.model.grid.move_agent(self,self.newPos)
        self.velocidadAgente = {
            "x": str(self.newPos[0] - x),
            "y": str(self.newPos[1] - y)
            }

    def move(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x, y + 1)):
            self.newPos = (x , y + 1)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()
    def step(self):
        self.seleccionaDireccion()

#Se dirige abajo carril derecho
class CarAgent4(mesa.Agent):
    global vectorPosiciones
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "black"
        self.moverStatus = None
        self.seleccion = ""
        self.conteo = 0
    def moveArriba(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x, y + 1)):
            self.newPos = (x , y + 1)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()


    def moveDerecha(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x + 1, y)):
            self.newPos = (x + 1 , y)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()

    def moveIzquierda(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x - 1, y)):
            self.newPos = (x - 1 , y)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()
            
    def seleccionaDireccion(self):
         #Carril abajo derecha
        #random2 = random.randint(25,30)#Carril Arriba derecha

        #Cuadrícula izquierda

        if (self.pos[1] == 7 and self.pos[0] <= 29):
            self.seleccion = "derecha"
            self.moveDerecha()
        elif (self.pos[0] == 41 and self.pos[1] == 7):
            self.seleccion = "arriba"
            self.moveArriba()

        elif(self.pos[0] == 41 and self.pos[1] == 41):
            self.seleccion = "izquierda"
            self.moveIzquierda()
        elif(self.pos[0] <= 29 and self.pos[1] == 41):
            self.seleccion = "abajo"
            self.verificaSemaforo()
           # self.seleccion = "abajo"
           # self.moveAbajo()
        #elif(self.pos[0] == 5 and self.pos[1] == 5):
         #   self.seleccion = "derecha"
         #   self.moveDerecha()
      #  elif(self.pos[0] == 21 and self.pos[1] == 5):
         #   self.seleccion = "arriba"
        #    self.verificaSemaforo()
        #Movimiento General

        elif self.seleccion == "derecha":
            self.moveDerecha()

        elif self.seleccion == "izquierda":
            self.moveIzquierda()

        elif self.seleccion == "arriba":
            self.moveArriba()

        elif self.seleccion == "abajo":
            self.verificaSemaforo()

        #Tercera Intersección CarAgent1
        else:
            self.verificaSemaforo()
    def verificaSemaforo(self):
        celdasAlrededor = self.model.grid.get_neighbors(self.pos, moore = True, include_center = False, radius = 2)
        for i in celdasAlrededor:
            if (isinstance(i, SemaforoAgent4)):
                if(i.color == "red" or i.color == "yellow"):
                    self.moverStatus = False
                    break
                elif(i.color == "green"):
                    self.moverStatus = True
                    break
            else: 
                self.moverStatus = True

        if self.moverStatus == True:
            self.move()
            self.moverStatus = None
        elif self.moverStatus == False:
            self.stop()
            self.moverStatus = None
        else:
            self.move()
            self.moverStatus = None
    def stop(self):
        x,y = self.pos
        self.conteo += 1
        self.newPos = (x , y)
        self.model.grid.move_agent(self,self.newPos)
        self.velocidadAgente = {
            "x": str(self.newPos[0] - x),
            "y": str(self.newPos[1] - y)
            }
    def move(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x, y - 1)):
            self.newPos = (x , y - 1)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()
    def step(self):
        self.seleccionaDireccion()

class SemaforoAgent1(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "green"
        self.tiempo = 13
    def change(self):
        self.tiempo -= 1
        if (self.tiempo == 3 and self.color == "green"):
            self.color = "yellow"
        elif(self.tiempo == 0 and self.color == "yellow"):
            self.color = "red"
            self.tiempo = 10
        elif(self.tiempo == 0 and self.color == "red"):
            self.color = "green"
            self.tiempo = 10
    def step(self):
        self.change()

class SemaforoAgent2(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "green"
        self.tiempo = 13
    def change(self):
        self.tiempo -= 1
        if (self.tiempo == 3 and self.color == "green"):
            self.color = "yellow"
        elif(self.tiempo == 0 and self.color == "yellow"):
            self.color = "red"
            self.tiempo = 10
        elif(self.tiempo == 0 and self.color == "red"):
            self.color = "green"
            self.tiempo = 10
    def step(self):
        self.change()

class SemaforoAgent3(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "red"
        self.tiempo = 13
    def change(self):
        self.tiempo -= 1
        if (self.tiempo == 3 and self.color == "green"):
            self.color = "yellow"
        elif(self.tiempo == 0 and self.color == "red"):
            self.color = "green"
            self.tiempo = 10
        elif(self.tiempo == 0 and self.color == "yellow"):
            self.color = "red"
            self.tiempo = 10
    def step(self):
        self.change()

class SemaforoAgent4(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "red"
        self.tiempo = 13
    def change(self):
        self.tiempo -= 1
        if (self.tiempo == 3 and self.color == "green"):
            self.color = "yellow"
        elif(self.tiempo == 0 and self.color == "red"):
            self.color = "green"
            self.tiempo = 10
        elif(self.tiempo == 0 and self.color == "yellow"):
            self.color = "red"
            self.tiempo = 10
    def step(self):
        self.change()

class entornoAgent(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "black"
    def step(self):
        pass