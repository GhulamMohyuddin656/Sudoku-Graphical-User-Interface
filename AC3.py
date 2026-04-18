from collections import deque
import Backtrack
def revise(domains, xi, xj):
    revised = False

    for x in domains[xi][:]:
        # If no value in xj allows (xi != xj), remove x
        if not any(x != y for y in domains[xj]):
            domains[xi].remove(x)
            revised = True

    return revised


def ac3(domains, constraints):
    queue = deque()
    for xi in constraints:
        for xj in constraints[xi]:
            queue.append((xi, xj))

    while queue:
        xi, xj = queue.popleft()

        if revise(domains, xi, xj):
            if len(domains[xi]) == 0:
                return False

            for xk in constraints[xi]:
                if xk != xj:
                    queue.append((xk, xi))

    return True

def solve_with_ac3(assignment, domains, constraints):
    if not ac3(domains, constraints):
        return None
    return Backtrack.simple_backtrack(assignment, domains, constraints)
