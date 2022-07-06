from search import *

def best_first_graph_search(problem, f, display=False):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    f = memoize(f, 'f')
    node = Node(problem.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()

    print('initial')
    print('frontier', frontier.heap)
    print('explored', explored)

    while frontier:
        print('begin')
        print('frontier', frontier.heap)
        print('explored', explored)

        node = frontier.pop()

        print('pop', node)

        if problem.goal_test(node.state):
            print('goal', node)
            if display:
                print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
            return node
        explored.add(node.state)


        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
                print('append', child)
            elif child in frontier:
                if f(child) < frontier[child]:                    
                    print('update')

                    del frontier[child]                    
                    print('delete', child)
                    
                    frontier.append(child)
                    print('apend', child)
         
        print('frontier', frontier.heap)
        print('explored', explored)
        print('end')   
    
    return None

def astar_search(problem, h=None, display=False):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n), display)


romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)
sol = astar_search(romania_problem).solution()
print(sol)
