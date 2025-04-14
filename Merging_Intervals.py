# sort
# first will hve value [1,3]
# keep checking 
def merge(intervals):
    intervals.sort()
    new = intervals[0]
    arr = []
    arr.append(new)
    for i in intervals:
        if new[1] >= i[0]:
            new[1] = max(i[1], new[1])
        else:
            new = i
            arr.append(new)
    return arr

def merge(intervals):
    intervals.sort()
    new = intervals[0]
    arr = []
    arr.append(new)
    for i in intervals:
        if i[0] <= new[1]:
            new[1] = max(i[1], new[1])
        else:
            new = i 
            arr.append(i)
    return arr