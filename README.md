# Avaloka Take-Home Assignment

Data Structures & Systems Design, for the AI / Multi-Agent Systems Intern role at Avaloka (Guruvai Sciences).

## Problem 1: LRU Cache (`lru_cache.py`)
A hash map plus a doubly linked list. The map finds a key's node in O(1), and the list keeps the usage order, so `get` and `put` are both O(1).

Run: `python lru_cache.py`

## Problem 2: Event Scheduler (`event_scheduler.py`)
- `can_attend_all`: sort by start time and check neighbouring events. O(n log n).
- `min_rooms_required`: sort starts and ends separately and use two pointers. O(n log n).

Events that end exactly when another starts are not treated as overlapping.

Run: `python event_scheduler.py`

The full explanations and the discussion answers are in the submitted PDF.
