# Adapted from Andrea Rubi  https://github.com/AndreaRubbi/Set-Cover-problem-solution-Python

def greedy(universe, subsets, costs):
    cost = 0
    elements = set(e for s in subsets for e in s)
    if elements != universe:
        return None
    covered = set()
    cover = []
    while covered != elements:
        subset = max(subsets, key=lambda s: len(s - covered) / costs[subsets.index(s)])
        cover.append(subset)
        cost += costs[subsets.index(subset)]
        covered |= subset

    return cover, cost
