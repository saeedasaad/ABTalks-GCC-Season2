from collections import Counter
import heapq

def topKFrequent(nums, k):

    freq_map = Counter(nums)

    heap = [(-freq, num) for num, freq in freq_map.items()]
    heapq.heapify(heap)

    result = []
    for _ in range(k):
        freq, num = heapq.heappop(heap)
        result.append(num)
    
    return result

if __name__ == "__main__":
    nums = [1,1,1,2,2,3,3,3,3,4,5,5]
    k = 2
    print("Top K Frequent Elements:", topKFrequent(nums, k))