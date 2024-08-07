DIRECTION = {
             'l': (0, -1),
             'r': (0, 1),
             'u': (-1, 0),
             'd': (1, 0)
            }

FLOW = {
        'l': {'2': 'l', '3': 'd', '6': 'u', '7': 'l'},
        'r': {'2': 'r', '4': 'd', '5': 'u', '7': 'r'},
        'd': {'1': 'd', '5': 'l', '6': 'r', '7': 'd'},
        'u': {'1': 'u', '3': 'r', '4': 'l', '7': 'u'}
       }

_IN_RANGE = lambda x, y, state: 0<=x<len(state) and 0<=y<len(state[0])

"""
pipes: ['q', 'a']
starts:  {'q': [3, 2], 'a': [5, 7]
"""
def find_starting_points(state):
    """Finds the starting nodes of the state"""
    pipes = list(filter(lambda x: 'a'<=x<='z',''.join(state)))
    starts = {}

    for i in range(len(state)):
        for j in range(len(state[0])):
            if 'a'<=state[i][j]<='z':
                starts[state[i][j]] = [i,j]
    
    return starts, pipes

def follow_flow(flow, current_path, state, end, final_path):
    """Recursive function that follows the flow of the pipe"""
    x, y = [x+y for x,y in zip(current_path[-1], DIRECTION[flow])]

    if _IN_RANGE(x, y, state) and state[x][y] == end:
        final_path.append(current_path + [''])
    elif _IN_RANGE(x, y, state) and state[x][y] in FLOW[flow]:
        return follow_flow(FLOW[flow][state[x][y]], current_path + [[x, y]], state, end, final_path)
    else:
        final_path.append(current_path + ['leak'])

    print(final_path)
    return final_path

def sum_water(total_path):
    """"Sums the water flowed if leakage found return sum * -1"""
    final_cells = set()
    first_leak = list(map(lambda x: len(x), filter(lambda x: 'leak' in x, total_path)))
    first_leak = 0 if len(first_leak) == 0 else min(first_leak) - 1

    for path in total_path:
        path = path[:-1]
        path = list(map(lambda x: str(x[0]) + ' ' + str(x[1]), path))
        idx = min(first_leak, len(path)) if first_leak else len(path)
        final_cells |= set(path[:idx])

    return len(final_cells) * (-1 if first_leak > 0 else 1)

def solution(state):
    """"Main CodeFights function"""
    starts, pipes = find_starting_points(state)
    total_path = []

    for pipe in pipes:
        end = pipe.upper()
        for di in DIRECTION:
            x, y = [x+y for x,y in zip(starts[pipe], DIRECTION[di])]
            if _IN_RANGE(x, y, state) and state[x][y] in FLOW[di]:
                total_path += follow_flow(FLOW[di][state[x][y]], [[x, y]], state, end, [])

    return sum_water(total_path)

state = ["3222222400000000", 
 "1000032A40000000", 
 "1000010110000000", 
 "72q227277Q000000", 
 "1000010110000000", 
 "1000062a50000000", 
 "6222222500000000"]

print(solution(state=state))