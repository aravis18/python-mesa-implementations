from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

from model import MoneyModel
from mesa.visualization.modules import CanvasGrid

from mesa.visualization.UserParam import UserSettableParameter

NUMBER_OF_CELLS = 20
SIZE_OF_CANVAS_IN_PIXEL_X = 800
SIZE_OF_CANVAS_IN_PIXEL_Y = 800
simulation_params = {
    "number_of_agents": UserSettableParameter("slider", "Number of agents", 1, 1, 200, 1, description = "choose number of agents"),
    "width": NUMBER_OF_CELLS,
    "height": NUMBER_OF_CELLS,
}

def agent_potrayal(agent):
    potrayal = {"Shape": "circle", "Filled": "true", "r": (agent.wealth/2) + 0.1}

    if agent.wealth > 4:
        potrayal["Color"] = "green"
        potrayal["Layer"] = 0

    elif agent.wealth > 3:
        potrayal["Color"] = "blue"
        potrayal["Layer"] = 1

    elif agent.wealth > 2:
        potrayal["Color"] = "yellow"
        potrayal["Layer"] = 2

    elif agent.wealth > 1:
        potrayal["Color"] = "orange"
        potrayal["Layer"] = 3

    else:
        potrayal["Color"] = "red"
        potrayal["Layer"] = 4
    return potrayal


grid = CanvasGrid(agent_potrayal, NUMBER_OF_CELLS, NUMBER_OF_CELLS, SIZE_OF_CANVAS_IN_PIXEL_X, SIZE_OF_CANVAS_IN_PIXEL_Y)

chart = ChartModule([{
    'Label': 'Gini',
    'Color': 'Black'}],
    data_collector_name = 'datacollector')

# syntax -> ModularServer(original model, [grid, chart, etc..], name, dictionary with arguments for the model)

server = ModularServer(MoneyModel, [grid, chart], "Money Model", simulation_params)        
server.port = 8521
server.launch()