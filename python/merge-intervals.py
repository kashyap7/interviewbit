# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
def tuplelist_to_intervallist(A):
    new_list = []
    for i in range(0, len(A)):
        new_interval = Interval(A[i][0], A[i][1])
        new_list.append(new_interval)
    return new_list

# @param intervals, a list of Intervals
# @param new_interval, a Interval
# @return a list of Interval
def insert(intervals, new_interval):
    n = len(intervals)
    i =0
    new_list = []
    remaining_intervals = []
    while i < n and intervals[i].start < new_interval.start :
        i = i + 1;
    # if the last interval with start less than the new interval's start
    # we have to merge this interval.
    # would using a for avoid the below statement
    merge_interval = Interval(0,0)
    if i == 0 :
        merge_interval.start = new_interval.start
        remaining_intervals = intervals  
    # print "FIRST: ", intervals[i].start, intervals[i].end
    
    # this the following case is exclusive of the above situtation where the interval.start
    # is greater than the new_interval's start
    else :
        i = i -1
        if intervals[i].end < new_interval.start :
            new_list = intervals[:i+1]
            remaining_intervals = intervals[i+1:]
            merge_interval.start = new_interval.start
        else :
            merge_interval.start = intervals[i].start
            new_list = intervals[:i]
            remaining_intervals = intervals[i:]
    N = len(remaining_intervals)
    k = 0
    while k < N and remaining_intervals[k].end < new_interval.end : 
        k = k + 1
    if k == N :
        merge_interval.end = new_interval.end
        new_list.append(merge_interval)
        return new_list
    if remaining_intervals[k].start > new_interval.end :
        merge_interval.end = new_interval.end
        new_list.append(merge_interval)
        new_list = new_list + remaining_intervals[k:]
    else :
        merge_interval.end = remaining_intervals[k].end
        new_list.append(merge_interval)
        new_list = new_list + remaining_intervals[k+1:]
    return new_list
A  = [ (6037774, 6198243), (6726550, 7004541), (8842554, 10866536), (11027721, 11341296), (11972532, 14746848), (16374805, 16706396), (17557262, 20518214), (22139780, 22379559), (27212352, 28404611), (28921768, 29621583), (29823256, 32060921), (33950165, 36418956), (37225039, 37785557), (40087908, 41184444), (41922814, 45297414), (48142402, 48244133), (48622983, 50443163), (50898369, 55612831), (57030757, 58120901), (59772759, 59943999), (61141939, 64859907), (65277782, 65296274), (67497842, 68386607), (70414085, 73339545), (73896106, 75605861), (79672668, 84539434), (84821550, 86558001), (91116470, 92198054), (96147808, 98979097) ]
B  = (36210193, 61984219)
blah_interval = Interval(B[0], B[1])
print blah_interval
def PRINT_S(A) :
    for i in range(0,len(A)) :
        print "(", A[i].start, A[i].end, ") "
PRINT_S(insert(tuplelist_to_intervallist(A),blah_interval))
print "-----------------------------------------------------------------"
PRINT_S(tuplelist_to_intervallist(A))