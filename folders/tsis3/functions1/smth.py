from itertools import chain


class Solution(object):
    def employeeFreeTime(self, schedule):
        if not schedule: return []

        timeline = sorted(chain(*schedule), key=lambda x: x
        start)
        result = []
        work = timeline[0]

        for interval in timeline:
            if work.end < interval.start:
                result.append(Interval(work.end, interval.start))
            work = interval

        elif work.end < interval.end:
        work = interval


return result
