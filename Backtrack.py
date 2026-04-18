calls = 0
failures = 0
def is_consistent(var, value, assignment, constraints):
    for neighbor in constraints[var]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True


def simple_backtrack(assignment, domains, constraints):
    global calls, failures
    calls += 1

    #Goal check
    if len(assignment) == 81:
        return assignment

    #Select unassigned variable
    unassigned = [v for v in domains if v not in assignment]
    var = unassigned[0]   # (we can improve later)

    #Try values from its domain
    for value in domains[var]:
        if is_consistent(var, value, assignment, constraints):

            assignment[var] = value

            result = simple_backtrack(assignment, domains, constraints)

            if result is not None:
                return result

            #Undo assignment
            del assignment[var]

    #Failure
    failures += 1
    return None
