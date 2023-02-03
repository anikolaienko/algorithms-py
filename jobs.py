from functools import reduce
import typing


class Job:
    def __init__(self, arr):
        self.start = arr[0]
        self.end = arr[1]
        self.load = arr[2]


def solution(jobValues: typing.List[typing.List[int]]) -> int:
    if any(len(job) != 3 or any(x < 0 for x in job) or job[0] > job[1] for job in jobValues):
        return -1
    jobs = list(map(Job, (j for j in jobValues)))

    timeline_size = max(job.end for job in jobs) + 1
    cpu_timeline = [0] * timeline_size
    for job in jobs:
        for i in range(job.start, job.end + 1):
            cpu_timeline[i] += job.load

    return max(cpu_timeline)


if __name__ == "__main__":
    print(solution([[1, 5, 3], [2, 5, 4], [7, 9, 6]]))
