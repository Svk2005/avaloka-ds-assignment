def can_attend_all(events):
    events = sorted(events)
    for i in range(1, len(events)):
        # an event can start exactly when the previous one ends
        if events[i][0] < events[i - 1][1]:
            return False
    return True

def min_rooms_required(events):
    starts = sorted(e[0] for e in events)
    ends = sorted(e[1] for e in events)
    s = 0          # pointer in starts
    e = 0          # pointer in ends
    rooms = 0      # meetings running right now
    most = 0       # highest value of rooms seen
    while s < len(starts):
        if starts[s] < ends[e]:
            rooms += 1      # a meeting starts before the earliest one ends
            s += 1
        else:
            rooms -= 1      # the earliest meeting has ended, room is free
            e += 1
        most = max(most, rooms)
    return most


if __name__ == "__main__":
    # Small tests
    events1 = [(9, 10), (10, 11), (11, 12)]
    print(can_attend_all(events1))       # True
    print(min_rooms_required(events1))   # 1
    events2 = [(9, 11), (10, 12), (11, 13)]
    print(can_attend_all(events2))       # False
    print(min_rooms_required(events2))   # 2
