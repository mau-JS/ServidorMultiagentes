from model import *
from agent import *
import numpy as np
import pandas as pd
def agent_portrayal(agent):
        portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": agent.color,
                 "r": 0.5}
        #Caso en el que sea semáforo
        return portrayal


#results_df = pd.DataFrame(results)
#print(results_df.keys())

grid = mesa.visualization.CanvasGrid(agent_portrayal, 50, 50, 500, 500)
chart = mesa.visualization.ChartModule([{"Label": "Tiempo total de coches en alto total",
                      "Color": "Black"}],
                    data_collector_name='datacollector')

server = mesa.visualization.ModularServer(
    CarModel, [grid,chart], "Car Model", {"N": 20, "width": 50, "height": 50}
)
server.port = 8521 # The default
server.launch()