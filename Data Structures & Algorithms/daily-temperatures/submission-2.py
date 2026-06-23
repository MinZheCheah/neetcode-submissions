class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Stack
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            # see if stack empty and if it is the temperature greater than the top of the stack
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                # for the index of temp we want to compute the num of days it took to find a greater temp
                # current temp - index of temperature just popped
                # add back into the stack with the corresponding position
                res[stackInd] = (i - stackInd) 
            stack.append([t, i])
        return res

        # T: O(n)
        # S: O(n)