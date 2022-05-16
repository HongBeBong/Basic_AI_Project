from collections import deque
from maze import maze
from index import Node, MazeProblem


def depth_first_graph_search(problem):
    node = Node(problem.init)
    if problem.goal_test(node.position):
        return node.solution(), explored
    frontier = deque([node])
    explored = []
    while frontier:
        node = frontier.pop()
        if node.position not in explored:
            explored.append(node.position)

        for child in node.expand(problem):
            if child.position not in explored and child not in frontier:
                if problem.goal_test(child.position):
                    return child.solution(), explored
                frontier.append(child)

    return None, None


# if __name__ == "__main__":
#     init = (5, 0)
#     goal = (8, 7)
#     problem = MazeProblem(init, goal, maze)
#     solution,explored = depth_first_graph_search(problem)
#     print(solution)
#     print("===================================================================================")
#     print(explored)
