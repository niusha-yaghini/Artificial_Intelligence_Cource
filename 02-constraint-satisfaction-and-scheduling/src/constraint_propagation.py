from collections import deque

def revise(
    csp,
    xi,
    xj,
    domains,
):
    revised = False

    for x in domains[xi].copy():
        has_support = False

        for y in domains[xj]:
            assignment = {
                xi: x,
                xj: y,
            }

            if csp.is_consistent(
                assignment
            ):
                has_support = True
                break

        if not has_support:
            domains[xi].remove(x)
            revised = True

    return revised


def ac3(
    csp,
    domains,
):
    queue = deque()

    for constraint in csp.constraints:
        xi = constraint.var1
        xj = constraint.var2

        queue.append(
            (xi, xj)
        )
        queue.append(
            (xj, xi)
        )

    while queue:
        xi, xj = queue.popleft()

        if revise(
            csp,
            xi,
            xj,
            domains,
        ):
            if len(domains[xi]) == 0:
                return False

            for xk in csp.neighbors[xi]:
                if xk != xj:
                    queue.append(
                        (xk, xi)
                    )

    return True

