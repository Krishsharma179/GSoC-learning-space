from mesa import Agent


class Soldier(Agent):
    """A military agent with attributes for hierarchy, health, and leave request logic."""

    def __init__(self, fitness:int, iq:int, edu_level:int, discipline:int, stress_handeling_level:int, rank:str, health, supervisor=None, subordinates=None):
        """
        Initialize a Soldier agent.
        Args:
            fitness: Physical fitness level of the soldier.
            iq: Intelligence level of the soldier.
            edu_level: Education level of the soldier.
            discipline: Discipline level of the soldier.
            stress_handeling_level: Stress handling capability.
            rank: Rank of the soldier (e.g., 'Commander', 'Officer', 'Soldier').
            health: Health value of the soldier.
            supervisor: Reference to the supervisor agent (default None).
            subordinates: List of subordinate agents (default None).
        """
        self.fitness = fitness
        self.iq = iq
        self.edu_level = edu_level
        self.discipline = discipline
        self.stress_handeling_level = stress_handeling_level
        self.rank = rank
        self.supervisor = supervisor
        self.health = health
        if subordinates is None:
            self.subordinates = []
        else:
            self.subordinates = subordinates
        self.want_to_leave = False  # Track intent to leave

    def request_exit(self):
        """
        Determine if the agent wants to leave based on health.
        Returns:
            bool: True if the agent wants to leave, False otherwise.
        """
        self.want_to_leave = False
        if self.health < 5:
            self.want_to_leave = True
        return self.want_to_leave




