from positions import positions

# IF A* algorithm
# ADD TOP_LEFT, BOTTOM_LEFT, TOP_RIGHT, BOTTOM_RIGHT


class Node:
    # Constructor
    # Position is state of node
    def __init__(self, position=None, parent=None):
        self.parent = parent
        self.position = position

        self.g = 0  # PATH-COST to the node
        self.h = 0  # heuristic to the goal: straight-line distance hueristic
        self.f = 0  # evaluation function f(n) = g(n) + h(n)

    # Create list child node
    def expand(self, problem):
        return [Node(position, self) for position in problem.actions(self.position)]

    #  Get solution
    def solution(self):
        return [node.position for node in self.path()]

    #  Get ALL node from init to goal
    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __eq__(self, other):
        if isinstance(other, Node):
            return other.position == self.position


class MazeProblem:
    # Constructor
    def __init__(self, init, goal, maze):
        self.maze = maze
        self.init = init
        self.goal = goal

    # Return list posible actions
    def actions(self, state):
        possible_actions = []
        for position in positions:
            node_position = (
                state[0] + position[0],
                state[1] + position[1],
            )
            # Make sure within range
            if (
                node_position[0] > (len(self.maze) - 1)
                or node_position[0] < 0
                or node_position[1] > (len(self.maze[len(self.maze) - 1]) - 1)
                or node_position[1] < 0
            ):
                continue

            # Make sure walkable terrain
            if self.maze[node_position[0]][node_position[1]] != 0:
                continue

            possible_actions.append(node_position)
        return possible_actions

    # Goal test
    def goal_test(self, state):
        return self.goal == state
