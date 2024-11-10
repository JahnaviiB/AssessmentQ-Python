n = 8
memory = [5, 1, 4, 2, 4, 1, 2, 3]

def maximumEfficiency(n, memory):
    MOD = 10**9 + 7

    def calculateEfficiency(arr):
        total_efficiency = 0
        for i, val in enumerate(arr):
            total_efficiency = (total_efficiency + (i + 1) * val) % MOD
        return total_efficiency

    max_efficiency = calculateEfficiency(memory)

    for idx in range(1, n // 2 + 1):
        for i in range(idx, n - idx):
            j = i + idx
            memory[i], memory[j] = memory[j], memory[i]

        max_efficiency = max(max_efficiency, calculateEfficiency(memory))

    return max_efficiency

result = maximumEfficiency(n, memory)
print(result)