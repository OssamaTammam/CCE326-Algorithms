def activitySelectionIterative(startTimes, finishTimes):
    ans = []

    # Always take the first finishing activity
    ans.append(startTimes[0])

    # Points to the last selected activity
    lastSelectedIndex = 0
    for j in range(1, len(finishTimes)):
        # If the activity starts after the last selected activity finished append it
        if startTimes[j] >= finishTimes[lastSelectedIndex]:
            ans.append(startTimes[j])
            lastSelectedIndex = j

    return ans


def activitySelectionRecursive(startTimes, finishTimes):
    # Always select the first finishing activity as the first activity
    selectedActivities = [finishTimes[0]]

    return _activitySelectionRecursive(
        startTimes, finishTimes, selectedActivities, len(startTimes)
    )


def _activitySelectionRecursive(
    startTimes, finishTimes, selectedActivities, noRemainingActivities
):
    if noRemainingActivities == 0:
        # Base case there are not more activities to consider
        return selectedActivities

    nextActivity = 1
    while (
        nextActivity < noRemainingActivities
        and startTimes[nextActivity] < finishTimes[selectedActivities[-1]]
    ):
        nextActivity += 1


startTimes = [1, 3, 0, 5, 8, 5]
finishTimes = [2, 4, 6, 7, 9, 9]

print(
    f"Iterative method: Selected activities start times are {activitySelectionIterative(startTimes, finishTimes)}"
)
