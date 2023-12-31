## Brute Force
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # No change to the handling of empty intervals list
        if len(intervals) == 0:
            return [newInterval]

        startNew = newInterval[0]
        endNew = newInterval[1]

        # If the new interval is after all existing intervals, append it.
        if startNew > intervals[-1][1]:  
            intervals.append(newInterval)
        else:
            # Handle the case for a single interval separately
            if len(intervals) == 1:
                if endNew < intervals[0][0]:
                    intervals.insert(0, newInterval)
                elif startNew > intervals[0][1]:
                    intervals.append(newInterval)
                else:
                    # This else part handles the overlap with the single interval
                    intervals.insert(0, newInterval)  # Insert before for merging later
            else:
                # Adjusted loop to handle insertion more accurately
                inserted = False
                for i in range(len(intervals)):
                    # Insert newInterval before the first interval it doesn't come after
                    if startNew <= intervals[i][0]:
                        intervals.insert(i, newInterval)
                        print("Inserted at", i)
                        inserted = True
                        break

                # If not inserted, it means the new interval goes at the end
                if not inserted:
                    intervals.append(newInterval)

        def merge(arr):
            # print(arr)
            flag = 0
            for i in range(len(arr)-1):
                if arr[i][1] >= arr[i+1][0]:
                    flag+=1
                    # print(flag)
                    # print(arr[i])
                    arr[i][0] = min(arr[i][0], arr[i+1][0])
                    arr[i][1] = max(arr[i][1], arr[i+1][1])
                    arr.pop(i+1)
                    break
                    # print(arr)

            if flag == 0:
                return arr
            else:
                return merge(arr)

        return merge(intervals)

if __name__ == "__main__":
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4, 8]

    sol = Solution()

    print(sol.insert(intervals, newInterval))