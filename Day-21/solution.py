from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:

    n = len(temperatures)
    result = [0] * n
    stack = []  

    for i, temp in enumerate(temperatures):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)

    return result

if __name__ == "__main__":
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(temps))
