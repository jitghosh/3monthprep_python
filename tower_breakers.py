def towerBreakers(n, m):
    # Write your code here
    pass

def Move(player_num: int, tower_state: list, move_ctr: int):
    longest_tower_length = max(tower_state)
    possible_reduced_heights = factors(longest_tower_length)

    if possible_reduced_heights == [1]:
        layer_num
    for ht in possible_reduced_heights:


def factors(tower_length: int):
    return [i for i in range(1,tower_length // 2 + 1) if tower_length % i == 0]


