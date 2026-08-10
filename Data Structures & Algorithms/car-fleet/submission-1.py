class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Main pointers:
        #We get the position and speed of cars into a pair array
        #We sort them by position in reverse order, so we know if any car behind them is going to catch up with them
        #For each pair, we append their time, and if the stack length is greater than two, and the time under the top is less than the time above it
            # we pop the lesser value because it becomes a fleet with the slower car
        #The length of the stack then becomes the number of car fleets.
        pairs = [(p,s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        for position, speed in pairs:
            time = ((target - position) / speed)
            stack.append(time)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)



