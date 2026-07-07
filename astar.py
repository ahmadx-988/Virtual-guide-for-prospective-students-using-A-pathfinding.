# astar.py

import heapq
from graph import campus_graph


def heuristic(a, b):
    """
    Heuristic function
    Estimates distance between two points.
    For our campus example, we use 0.
    """

    return 0



def a_star(start, goal):

    # Priority queue
    open_list = []

    heapq.heappush(open_list, (0, start))

    # Store previous nodes
    came_from = {}

    # Cost from start point
    g_score = {}

    for node in campus_graph:
        g_score[node] = float("inf")

    g_score[start] = 0


    while open_list:

        current_cost, current = heapq.heappop(open_list)


        # Destination reached
        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)

            path.reverse()

            return path


        # Explore neighbors
        for neighbor, distance in campus_graph[current]:

            new_cost = g_score[current] + distance


            if new_cost < g_score[neighbor]:

                g_score[neighbor] = new_cost

                priority = (
                    new_cost +
                    heuristic(neighbor, goal)
                )

                heapq.heappush(
                    open_list,
                    (priority, neighbor)
                )

                came_from[neighbor] = current


    return None



# Testing

if __name__ == "__main__":

    start = "Main Gate"
    destination = "Boys Hostel"

    route = a_star(start, destination)


    if route:
        print("Shortest Route:")
        print(" → ".join(route))

    else:
        print("No Route Found")