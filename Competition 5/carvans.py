T = int(input())

for t in range(T):
    N = int(input())
    car_speeds = [int(x) for x in input().split()]
    max_speed = car_speeds[0]
    max_speed_count = 0
    for speed in car_speeds:
        if speed <= max_speed:
            max_speed_count += 1
            max_speed = speed
    print(max_speed_count)
