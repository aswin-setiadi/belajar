# https://www.geeksforgeeks.org/job-sequencing-problem/ greedy algorithm with: always loop each possible day for a job / use heap to find max profit for given day
# https://www.geeksforgeeks.org/job-sequencing-problem-using-disjoint-set/ use disjoint set? # TODO read first
# function to schedule the jobs take 2
# arguments array and no of jobs to schedule


def printJobScheduling(arr: list[list[int]], t: int):
    # length of array
    n = len(arr)

    # Sort all jobs according to
    # decreasing order of profit (this is bubble sort implementation)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # To keep track of free time slots
    result = [False] * t

    # To store result (Sequence of jobs)
    job = ["-1"] * t

    print(arr)
    # Iterate through all given jobs
    for i in range(len(arr)):
        # Find a free slot for this job
        # (Note that we start from the
        # last possible slot)
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            # Free slot found
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break

    # print the sequence
    print(job)


# TODO
# heap implementation when storing possible jobs in currently empty deadline

# Driver's Code
if __name__ == "__main__":
    arr = [
        ["a", 2, 100],  # Job Array
        ["b", 1, 19],
        ["c", 2, 27],
        ["d", 1, 25],
        ["e", 3, 15],
    ]

    print("Following is maximum profit sequence of jobs")

    # Function Call
    printJobScheduling(arr, 3)

# This code is contributed
# by Anubhav Raj Singh
