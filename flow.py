import flow_classes as fl

if __name__ == '__main__':
    n = 12

    s = n - 2
    t = n - 1

    solver = fl.NetworkFlowSolver(n, s, t)

    # source arcs
    solver.add_arc(s, 0, 10)
    solver.add_arc(s, 1, 5)
    solver.add_arc(s, 2, 10)

    # middle arcs
    solver.add_arc(0, 3, 10)
    solver.add_arc(1, 2, 10)
    solver.add_arc(2, 5, 15)
    solver.add_arc(3, 1, 2)
    solver.add_arc(3, 6, 15)
    solver.add_arc(4, 1, 15)
    solver.add_arc(4, 3, 3)
    solver.add_arc(5, 4, 4)
    solver.add_arc(5, 8, 10)
    solver.add_arc(6, 7, 10)
    solver.add_arc(7, 4, 10)
    solver.add_arc(7, 5, 7)

    solver.add_arc(6, t, 15)
    solver.add_arc(8, t, 10)

    print('max flow is:', solver.get_max_flow(), '\n')

    graph = solver.get_graph()
    for arcs in graph:
        for arc in arcs:
            print(arc)