from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from Agent import MoneyAgent

def compute_gini(model):
    # return 0
    agent_wealth = [agent.wealth for agent in model.schedule.agents]
    x = sorted(agent_wealth)
    N = model.num_agents
    B = sum(xi * (N - i) for i,xi in enumerate(x)) / (N * sum(x))
    return (1 + (1/N) - 2 * B)



class MoneyModel(Model):

    def __init__(self, number_of_agents, width, height):
        self.num_agents = number_of_agents
        self.grid = MultiGrid(width, height, False)
        self.schedule = RandomActivation(self)
        self.running = True     #to be able to run simulation in server and potentially add condition to stop the simulation

        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)

            # Add agent to random grid in the cell
            x = self.random.randrange(self.grid.width)             # self.random helps record the 'randomness' => can repeat the random steps again if needed
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x,y))
        
        self.datacollector = DataCollector(model_reporters={"Gini": compute_gini} )
    
    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()            # Advance the model by one step
        
