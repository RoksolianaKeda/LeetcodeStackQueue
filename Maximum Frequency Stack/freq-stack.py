from collections import defaultdict, deque

class FreqStack:
    def __init__(self):
        self.freq_map = defaultdict(int)
        self.group_map = defaultdict(deque)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq_map[val] += 1

        freq = self.freq_map[val]

        self.max_freq = max(self.max_freq, freq)

        self.group_map[freq].append(val)

    def pop(self) -> int:
        val = self.group_map[self.max_freq].pop()
        self.freq_map[val] -= 1
    
        if not self.group_map[self.max_freq]:
            self.max_freq -= 1

        return val
