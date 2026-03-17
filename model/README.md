# Military Hierarchy Simulation with Mesa

This project simulates a military hierarchy using agent-based modeling with Mesa. It demonstrates how agents (soldiers) interact in a structured chain of command, request leave, and are managed by supervisors and meta agents (groups).

## Features
- **Agent Hierarchy:** Soldiers are organized with supervisor and subordinate relationships (Commander, Officer, Soldier).
- **Leave Request Workflow:** Agents can request to leave; requests are approved or denied by their supervisor.
- **Meta Agents:** Groups of agents (e.g., squads) are managed collectively, with group-level attributes.
- **Approval Logic:** Supervisors evaluate leave requests based on agent health and other criteria.
- **Simulation Steps:** Each step processes leave requests and updates group membership.

## Structure
- `Agent.py`: Defines the Soldier class, including attributes, leave request logic, and supervisor/subordinate relationships.
- `militarymodel.py`: Implements the Mesa model, agent creation, hierarchy setup, leave processing, meta agent creation, and simulation steps.

## How It Works
1. Agents are created and assigned ranks, health, and relationships.
2. Each agent can request leave (if health is low).
3. Supervisors approve or deny leave requests.
4. Approved agents are removed from their group (meta agent).
5. The simulation can be expanded with more agents, groups, and custom logic.

## Usage
- Run `militarymodel.py` to start the simulation.
- Customize agent attributes, approval criteria, and group structure as needed.


## Example Output
- Agents requesting leave and being approved or denied by their supervisor.
- Agents leaving their group and being removed from the meta agent.

## Extending the Model
- Add more ranks, agents, or groups.
- Implement promotions, transfers, or additional approval criteria.
- Visualize the hierarchy and group structure using networkx or Mesa's visualization tools.

---

This project is a foundation for exploring organizational dynamics, decision-making, and group management in agent-based simulations.
