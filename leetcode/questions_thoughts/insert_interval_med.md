- Input:
    1. `intervals` array containing existing intervals.
    2. `newInterval` array that is to be inserted in `intervals`.
- Output:
    - Merged intervals array (that merges overlapping intervals after inserting).

## Brute Force solution

There are two steps to the solution.
1. Inserting the `newInterval` array at the right place in `intervals`. (based on the start and end times).
2. Merging after insertion. (I used recursion for merging).

### Insertion
(This is the part where I messed up and took ChatGPT's help).

1. If intervals array is empty, just append the newInterval.
2. If the intervals array contains 1 element, there are two places to insert the newInterval array. 
```python
if endNew < i[0]:
    insert at 0
elif startNew > i[1]:
    insert at 1
else:
    insert at 0 # To handle one overlapping interval.
```
3. If len(intervals) > 1
```python
maintain a bool = False
for each value in intervals:
    # As we are merging the overlapping intervals, we just need to check based on the start times.
    if startNew <= startval at i:
        insert at i
        bool = True

if not bool:
    just append at the end
```

### Merging
I used recursion to merge after insertion.
1. Maintain a flag to see if there are any changes made in the array (this is to exit out of recursion).
2. For each element in intervals:
    - check if the end interval of current index is `>=` start interval of next index. If yes, there is an overlap.
    - update the flag to True
    - update the current interval at index `i` using `min` and `max` for the overlapping intervals.
    - remove `i+1` interval
    - `break` (this is important because I ran just one update per recursion call as the len(arr) is changed)
3. if flag then merge again; else return the array as there are no more changes.

```python
def merge(arr):
    flag = False
    for each element:
        check if end at i >= start at i+1:
            flag = True
            update interval at i based on min and max
            break
    if flag:
        return merge(arr)
    else:
        return arr
```

## Overall pseudocode

```python
def insert_interval(intervals, new_interval):
    
    insert_at_position(intervals, new_interval)
    
    def merge(arr):
        returns merged_array

    return merge(intervals)
```
