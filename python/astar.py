import heapq
class astar:
    def __init__(self, initial, trans_f, end_f = None, estimate_f = lambda x:0):
    # initial: starting state for search
    # trans_f: function taking a state and returning a list of tuples
    #          giving states reachable from that state with their costs
    # end_f: function taking a state and returning True if it is an end state
    # estimate_f: heuristic function for A* search (default is Dijkstra search)
        self.initial_state = initial
        self.trans_func = trans_f
        self.end_func = end_f
        self.estimate_func = estimate_f
    def run(self, target_state = None):
    # Search for a path to the specified target state or,
    # if target_state == None, any state for which end_f returns True.
    # Return the cost and the reverse path to the target.
    # Run with target_state == end_f == None to explore fully.
    # In this case, if the state space is finite, return a list of tuples
    # giving all reachable states with their associated costs.
        maxcost = 0
        counter = 0
        visited = dict() # state => (cost, ancestor)
        queue = []
        def get_path(state):
            path = []
            while state != None:
                path.append(state)
                state = visited[state][1]
            return path
        initial_est = self.estimate_func(self.initial_state)
        heapq.heappush(queue, (initial_est, counter, 0, self.initial_state, None))
        while queue:
            rank, _, cost, state, ancestor = heapq.heappop(queue)
            if state in visited: continue
            visited[state] = (cost,ancestor)
            if state == target_state or (self.end_func and self.end_func(state)):
                return (cost, get_path(state))
            transitions = self.trans_func(state)
            for next_state, next_cost in transitions:
                new_cost = cost + next_cost
                new_rank = new_cost + self.estimate_func(next_state)
                counter += 1
                heapq.heappush(queue, (new_rank, counter, new_cost, next_state, state))
        if target_state == None and self.end_func == None:
            return [(s,visited[s][0]) for s in visited]
