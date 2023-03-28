from pickle import TRUE
from mesa import Agent

# from mesa import Model
# from mesa.time import RandomActivation
# from mesa.space import MultiGrid
# from mesa.datacollection import DataCollector



class MoneyAgent(Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1
        

    def step(self) -> None:
        self.move()
        if self.wealth > 0:
            self.give_money()
    
    def give_money(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = self.random.choice(cellmates)
            other.wealth += 1
            self.wealth -= 1
    
    def move(self) -> None:
        
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore = TRUE, include_center = False, radius = 1)       # defines motion
        # x = possible_steps
        # new_position = x
        new_position = self.random.choice(possible_steps)                                                       # defines new pos to move to
        self.model.grid.move_agent(self, new_position)


