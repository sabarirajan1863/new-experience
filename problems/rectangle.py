A = [1, 2, 5, 1, 1, 2, 3, 5, 1]
X = 5
def solution(A, X):
    counts = {}
    for length in A:
        counts[length] = counts(length, 0) + 1
    lengths = sorted(list(set(A)), reverse=True)
    num_rectangles = 0
    for i in range(len(lengths)):
        for j in range(i, len(lengths)):
            area = lengths[i] * lengths[j]
            if area >= X:
                if counts[lengths[i]] >= 2 and counts[lengths[j]] >= 2:
                    num_rectangles += 1
                    if num_rectangles > 1000000000:
                        return -1
    return num_rectangles
result = solution(A, X)
print(result)