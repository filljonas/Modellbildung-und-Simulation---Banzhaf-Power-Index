from itertools import chain, combinations


def compute_absolute_banzhaf_power_index(participant, weights, quorum):
    def powerset(iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
    absolute_banzhaf_power_index = 0
    # Weight of the participant we are interested in
    w_participant = weights[participant]
    # Remove index from weights and create powerset
    tmp_weights = weights.copy()
    tmp_weights.pop(participant)
    B = list(powerset(tmp_weights))
    # Searches through all sets -> if the participant can change the result, then increment the counter
    for s in B:
        cur = sum(s)
        if cur < quorum and cur + w_participant >= quorum:
            absolute_banzhaf_power_index += 1
    return absolute_banzhaf_power_index


def compute_relative_banzhaf_power_index(abs_part, abs_total):
    return abs_part / sum(abs_total)


def compute_all_absolute_banzhaf_power_indices(weights, quorum):
    indices = [0] * len(weights)
    for i in range(len(weights)):
        indices[i] = compute_absolute_banzhaf_power_index(i, weights, quorum)
    return indices


def compute_all_relative_banzhaf_power_indices(weights, abs):
    indices = [0] * len(weights)
    for i in range(len(weights)):
        indices[i] = compute_relative_banzhaf_power_index(abs[i], abs)
    return indices


if __name__ == '__main__':
    weights = [4, 4, 4, 2, 2, 1]
    quorum = 12
    absolute = compute_all_absolute_banzhaf_power_indices(weights, quorum)
    relative = compute_all_relative_banzhaf_power_indices(weights, absolute)
    print(relative)





