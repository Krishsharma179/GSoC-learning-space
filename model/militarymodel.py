from mesa import Model
import networkx as nx
from agent import Soldier
from random import randint
from mesa import Agent
from mesa.experimental.meta_agents.meta_agent import (
    create_meta_agent
    
)

class Military_model(Model):
    """A Mesa model simulating a military hierarchy with agent-based leave approval and meta agent grouping."""
    def __init__(self):
        """Initialize the military model, create agents, and set up hierarchy."""
        super().__init__()
        agent1=Soldier(fitness=9,iq=9,edu_level=1,discipline=9,stress_handeling_level=9,rank="Commander",health=10)

        agent2=Soldier(fitness=randint(0,10),iq=randint(0,10),edu_level=2,discipline=8,stress_handeling_level=8,rank="Officer",health=3)

        agent3=Soldier(fitness=randint(0,10),iq=randint(0,10),edu_level=1,discipline=9,stress_handeling_level=9,rank="Soldier",health=8)
            

        agent1.subordinates = [agent2, agent3]
        agent2.supervisor = agent1
        agent2.subordinates = [agent3]
        agent3.supervisor = agent2
        
        self.agen=[agent1,agent2,agent3]

    def approval(subordinates:list):
        """Return a list of subordinates who do not meet approval criteria."""
        not_approved_agent=[]
        for i in subordinates:
            if i.fitness<5 or i.iq<5 or i.edu_level<3 or i.stress_handeling_level<5:
                not_approved_agent.append(i)
        return not_approved_agent       
            
    def approve_leave(self,agent):
        """This is the supervisor approve leave function"""
        return agent.health <5


    def process_leave_requests(self, agent):
        """Check if an agent's leave request is approved by supervisor and agent's own request_exit logic."""
        approved = False
        if hasattr(agent, 'request_exit') and agent.request_exit() and self.approve_leave(agent):
            approved = True
        return approved

    def create_meta_agents(self):
        """Create a meta agent (group) for the current agents with group-level attributes."""
        agent1=self.agen[0]
        agent2=self.agen[1]
        agent3=self.agen[2]
        self.meta= create_meta_agent(
            self,
            new_agent_class="Metaagent",
            agents=[agent1, agent2,agent3],
            mesa_agent_type=Agent,
            meta_attributes={
                "group_name": "Alpha Squad",
                "group_rank": "Squad",
                "group_strength": sum(agent.fitness for agent in self.agen),
                "leader": agent1,
                "member_count": 3
            },
        )

    def step(self):
        """Run one step of the simulation: process leave requests and update meta agent membership."""
        for agent in self.agen:
            if self.process_leave_requests(agent):
                self.meta.remove_constituting_agents({agent})
                print(f"{agent} left ")

model=Military_model()
model.create_meta_agents()
model.step()

