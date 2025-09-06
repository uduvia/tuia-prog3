from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GoRight:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Go Right

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[node.state] = True

        # Return if the node contains a goal state
        if grid.objective_test(node.state):
            return Solution(node, reached)

        # Initialize frontier with the initial node
        # In this example, the frontier is a queue
        frontier = QueueFrontier()
        frontier.add(node)

        while True:

            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(reached)

            # Remove a node from the frontier
            node = frontier.remove()

            # Iterate through the possible actions
            for act in grid.actions(node.state):

                # Ignore all actions except "right"
                if act != "right":
                    continue

                # Get the successor
                new_state = grid.result(node.state, act)

                # Check if the successor is reached
                if new_state in reached:
                    continue

                # Initialize the son node
                new_node = Node(
                    "",
                    new_state,
                    cost=node.cost + grid.individual_cost(node.state, act),
                    parent=node,
                    action="right",
                )

                # Mark the successor as reached
                reached[new_state] = True

                # Return if the node contains a goal state
                # In this example, the goal test is run before adding the son to the
                # frontier
                if grid.objective_test(new_state):
                    return Solution(new_node, reached)

                # Add the new node to the frontier
                frontier.add(new_node)
