import sys

N = int(sys.stdin.readline().strip())
meetings = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().strip().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))

able_meetings = []

for meeting in meetings:
    if len(able_meetings) == 0:
        able_meetings.append(meeting)
    else:
        before_meeting = able_meetings[-1]
        if meeting[0] >= before_meeting[1]:
            able_meetings.append(meeting)
print(len(able_meetings))
