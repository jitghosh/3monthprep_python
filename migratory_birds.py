from collections import Counter
def migratoryBirds(arr):
    bird_counter = Counter(arr)
    bird_counts = list(zip(bird_counter.keys(), bird_counter.values()))
    # -x[1] is same as reverse=True. We could have done
    # sorted(bird_counts,key = lambda x: (x[1],x[0]), reverse=True) 
    # Note reverse only impacts the first key
    # Also note the use of tuple to use multiple keys
    bird_counts = sorted(bird_counts,key = lambda x: (-x[1],x[0])) 
    return bird_counts[0][0]

str = []
with(open("test_migratory_birds.txt",mode="r") as test_file):
    str = test_file.readlines()

print(migratoryBirds([int(s) for s in str[0].split(" ")]))
