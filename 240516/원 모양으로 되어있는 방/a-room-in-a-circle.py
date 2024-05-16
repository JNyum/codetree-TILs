n = int(input())
rooms = [int(input()) for _ in range(n)]
distances = []

for _ in range(n):
    i = 0
    distance = 0
    for room in rooms:
        distance += room*i
        i += 1
    distances.append(distance)
    rooms.append(rooms[0])
    rooms.pop(0)
print(min(distances))