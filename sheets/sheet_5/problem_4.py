def solution(points):
    # Answer
    intervals = []

    # Sort the points ascending
    sortedPoints = sorted(points)

    # Current point of time we are at
    currPoint = sortedPoints[0]
    for point in sortedPoints[1:]:
        currInterval = (currPoint, currPoint + 1)
        intervals.append(currInterval)
        currPoint = point

    return intervals


points = [1, 3, 2, 4.5, 6, 8, 7]
print(solution(points))
