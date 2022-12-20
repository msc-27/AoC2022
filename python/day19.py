import astar
import re
with open('input') as f: lines = [x.strip('\n') for x in f]
numbers = [list(map(int, re.findall('-?[0-9]+',line))) for line in lines]

cost_basis = 100 # arbitrary number higher than any possible number of geode robots

# Transition function for A* search
def make_trans(ore_cost, cla_cost, obs_cost, geo_cost):
    max_ore_cost = max(ore_cost, cla_cost, obs_cost[0], geo_cost[0])
    def trans(s): # s = (t, ore_stock,cla_stock,obs_stock, ore_robots,cla_robots,obs_robots,geo_robots)
        # state indicates t minutes left *after* this one
        # return cost = cost_basis - number of geodes cracked next minute
        t, ore_stock,cla_stock,obs_stock, ore_robots,cla_robots,obs_robots,geo_robots = s
        if t == 0:
            yield ((0,0,0,0,0,0,0,0), 0) # Dummy end state
        else:
            ore_next = ore_stock + ore_robots
            cla_next = cla_stock + cla_robots
            obs_next = obs_stock + obs_robots
            cost = cost_basis - geo_robots

            ore_tried = False
            cla_tried = False
            obs_tried = False
            geo_tried = False

            geo_poss = (ore_stock >= geo_cost[0] and obs_stock >= geo_cost[1])
            if geo_poss:
                yield ((t-1, ore_next - geo_cost[0], cla_next, obs_next - geo_cost[1], ore_robots, cla_robots, obs_robots, geo_robots+1), cost - 1)
                geo_tried = True
            obs_poss = (ore_stock >= obs_cost[0] and cla_stock >= obs_cost[1])
            if obs_poss and t >= 3 and obs_stock + obs_robots*t < geo_cost[1]*t:
            # don't build obsidian with less than three minutes left or if we have enough obsidian to build geode every turn
                yield ((t-1, ore_next - obs_cost[0], cla_next - obs_cost[1], obs_next, ore_robots, cla_robots, obs_robots+1, geo_robots), cost)
                obs_tried = True
            cla_poss = (ore_stock >= cla_cost)
            if cla_poss and t >= 5 and cla_stock + cla_robots*t < obs_cost[1]*(t-1):
            # don't build clay with less than five minutes left or if we have enough clay to build obsidian every turn but the last
                yield ((t-1, ore_next - cla_cost, cla_next, obs_next, ore_robots, cla_robots+1, obs_robots, geo_robots), cost)
                cla_tried = True
            ore_poss = (ore_stock >= ore_cost)
            if ore_poss and t >= 3 and ore_stock + ore_robots*t < max_ore_cost*t:
            # don't build ore with less than three minutes left or if we have enough ore to build something every turn
                yield ((t-1, ore_next - ore_cost, cla_next, obs_next, ore_robots+1, cla_robots, obs_robots, geo_robots), cost)
                ore_tried = True
            if not any([geo_tried,obs_tried,cla_tried,ore_tried]) or ore_stock + ore_robots*t < max_ore_cost*(t+1):
            # consider doing nothing if we didn't try building anything, or to conserve ore if we don't have enough ore to build now and every turn from now
                yield ((t-1, ore_next, cla_next, obs_next, ore_robots, cla_robots, obs_robots, geo_robots), cost)
    return trans

def end_f(s): return s[0] == 0 # end search with 0 minutes left

def est_f(s): # consistent heuristic function for A*
# assume we can build a geode robot every turn from now
    t = s[0]
    geo_robots = s[7]
    return cost_basis*t - (geo_robots+1)*t - t*(t-1)//2

# Part 1
quality_sum = 0
for line in numbers:
    ore_cost = line[1]
    cla_cost = line[2]
    obs_cost = (line[3],line[4]) # ore, cla
    geo_cost = (line[5],line[6]) # ore, obs
    start = (23, 0, 0, 0, 1, 0, 0, 0)
    a = astar.astar(start, make_trans(ore_cost, cla_cost, obs_cost, geo_cost), end_f, est_f)
    cost,_ = a.run()
    open_geodes = 23*cost_basis - cost
    print(line[0], open_geodes)
    quality_sum += line[0] * open_geodes
print("Part 1:", quality_sum)

print()

# Part 2
geode_product = 1
for line in numbers[:3]:
    ore_cost = line[1]
    cla_cost = line[2]
    obs_cost = (line[3],line[4]) # ore, cla
    geo_cost = (line[5],line[6]) # ore, obs
    start = (31, 0, 0, 0, 1, 0, 0, 0)
    a = astar.astar(start, make_trans(ore_cost, cla_cost, obs_cost, geo_cost), end_f, est_f)
    cost,_ = a.run()
    open_geodes = 31*cost_basis - cost
    print(line[0], open_geodes)
    geode_product *= open_geodes
print("Part 2:", geode_product)
