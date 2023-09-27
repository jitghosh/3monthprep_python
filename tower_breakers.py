def towerBreakers(n, m):
    # Write your code here
    return Move(1,[m]*n)

def Move(player_num: int, tower_state: list):
    '''
    What does "playing optimally" mean ? Always reduce a tower to 1 ?
    '''
    # find the tower with longest current height 
    longest_tower_length = max(tower_state)
    longest_tower_idx = tower_state.index(longest_tower_length)
    # current player has no moves left - so other player wins
    if longest_tower_length == 1:
        return 1 if player_num == 2 else 2
    # find what possible lengths we can reduce the tower to
    possible_reduced_heights = factors(longest_tower_length)
    # take the longest of those and reduce tower to it
    tower_state[longest_tower_idx] = max(possible_reduced_heights)

    return Move(1 if player_num == 2 else 2,tower_state)
    


def factors(tower_length: int):
    return [i for i in range(1,tower_length // 2 + 1) if tower_length % i == 0]


print(towerBreakers(1,4))