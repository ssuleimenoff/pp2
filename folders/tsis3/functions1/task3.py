def solve(numheads, numlegs):
    rabbits = 0.5 * numlegs - numheads
    chickens = 2 * numheads - 0.5 * numlegs
    print("Rabbits =", rabbits)
    print("Chickens =", chickens)


a = int(input())
b = int(input())
print(solve(a, b))