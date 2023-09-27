from collections import Counter

def sockMerchant(n, ar):
    sock_counts = Counter(ar)
    pair_cnt = 0

    for key in sock_counts.keys():
        pair_cnt += sock_counts[key] // 2 # each pair has 2 identical socks. So for example if we had 7 socks of type 2, we will get 3 pairs i.e. 7 // 2
    
    return pair_cnt