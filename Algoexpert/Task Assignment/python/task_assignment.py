import unittest

def taskAssignment(k, tasks):

    pairedTasks = []

    taskDurationsToIndices = getTaskDurationsToIndices(tasks)

    sortedTasks = sorted(tasks)

    for i in range(k):

        task1Duration = sortedTasks[i]
        task1Index = taskDurationsToIndices[task1Duration].pop()

        task2SortedIndex = len(tasks) - 1 - i
        task2Duration = sortedTasks[task2SortedIndex]
        task2Index = taskDurationsToIndices[task2Duration].pop()

        pairedTasks.append([task1Index, task2Index])

    return pairedTasks

def getTaskDurationsToIndices(tasks):
    taskDurationsToIndices = {}

    for i, taskDuration in enumerate(tasks):
        if taskDuration in taskDurationsToIndices:
            taskDurationsToIndices[taskDuration].append(i)
        else:
            taskDurationsToIndices[taskDuration] = [i]

    return taskDurationsToIndices

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        k = 3
        tasks = [1, 3, 5, 3, 1, 4]
        expected = [[4, 2], [0, 5], [3, 1]]
        actual = taskAssignment(k, tasks)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()