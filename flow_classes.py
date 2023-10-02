INF = 999999999999

class Arc:
    def __init__(self, start: int, end: int, capacity: int) -> None:
        self.start: int = start
        self.end: int = end
        self.capacity: int = capacity
        self.flow: int = 0
        self.residual: Arc = None

    def is_residual(self) -> bool:
        return self.capacity == 0
    
    def get_remaining_capacity(self) -> int:
        return self.capacity - self.flow
    
    def augment(self, bottleneck: int) -> None:
        self.flow += bottleneck
        self.residual.flow -= bottleneck

    def __str__(self) -> str:
        return f"{self.start}->{self.end} | cap = {self.capacity} | flow = {self.flow} | is {'not' if self.capacity != 0 else ''} residual"
    
class NetworkFlowSolver:
    def __init__(self, n: int, s: int, t: int) -> None:
        self.n = n
        self.s: int = s
        self.t: int = t
        self.visited_token: int = 1
        self.visited: list[int] = [0 for _ in range(n)]
        self.solved: bool = False
        self.max_flow: int = 0
        self.adj: list[list[Arc]] = [[] for _ in range(n)]

    def add_arc(self, start: int, end: int, capacity: int) -> None:
        arc1 = Arc(start, end, capacity)
        arc2 = Arc(end, start, 0)

        arc1.residual = arc2
        arc2.residual = arc1

        self.adj[start].append(arc1)
        self.adj[end].append(arc2)

    def get_max_flow(self) -> int:
        self.execute()
        return self.max_flow

    def get_graph(self) -> list[list[Arc]]:
        self.execute()
        return self.adj
    
    def execute(self) -> None:
        if self.solved:
            return
        self.solved = True
        self.solve()

    def _dfs(self, node: int, flow: int) -> int:
        if node == self.t:
            return flow
        
        self.visited[node] = self.visited_token
        
        arcs: list[Arc] = self.adj[node]
        for arc in arcs:
            if arc.get_remaining_capacity() > 0 and self.visited[arc.end] != self.visited_token:
                bottleneck = self._dfs(arc.end, min(flow, arc.get_remaining_capacity()))

                if bottleneck > 0:
                    arc.augment(bottleneck)
                    return bottleneck
                
        return 0
    
    def solve(self) -> None:
        f = self._dfs(self.s, INF)
        while f != 0:
            self.visited_token += 1
            self.max_flow += f
            f = self._dfs(self.s, INF)