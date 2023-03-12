import random
x1, y1 = 1, 1
x2, y2 = 5, 1
x3, y3 = 1, 5
x4, y4 = 5, 5
mid_x = (x1 + x2 + x3 + x4) / 4
mid_y = (y1 + y2 + y3 + y4) / 4
N = 100
p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0
p6_count = 0
p7_count = 0
p8_count = 0

for i in range(N):
    x = random.uniform(x1, x4)
    y = random.uniform(y1, y4)

    if x < mid_x and y < mid_y:
        p1_count += 1
    elif x >= mid_x and y < mid_y:
        p2_count += 1
    elif x >= mid_x and y >= mid_y:
        p3_count += 1
    elif x < mid_x and y >= mid_y:
        p4_count += 1
    elif x < mid_x and y == mid_y:
        p5_count += 1
    elif x == mid_x and y < mid_y:
        p6_count += 1
    elif x > mid_x and y == mid_y:
        p7_count += 1
    elif x == mid_x and y > mid_y:
        p8_count += 1
p1_prob = p1_count / N * 100
p2_prob = p2_count / N * 100
p3_prob = p3_count / N * 100
p4_prob = p4_count / N * 100
p5_prob = p5_count / N * 100
p6_prob = p6_count / N * 100
p7_prob = p7_count / N * 100
p8_prob = p8_count / N * 100
print(f"p1:{p1_prob}%, p2:{p2_prob}%, p3:{p3_prob}%, p4:{p4_prob}%,")