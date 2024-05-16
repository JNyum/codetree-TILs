n = int(input())
check_points = [tuple(map(int,input().split())) for _ in range(n)]
# print(n)
# print(check_points)
distances = []

for i in range(1,n-1):
    points = check_points[:i] + check_points[i+1:]
    distance = 0
    for j in range(len(points)-1):
        distance += abs(points[j][0] - points[j+1][0]) + abs(points[j][1] - points[j+1][1])
    distances.append(distance)
print(min(distances))