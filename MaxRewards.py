def getmaxrewards(k,rewards1,rewards2):
    for i in range(len(rewards1)):
        diff = [rewards1[i] - rewards2[i]]
        diff.sort()

    max_reward = 0
    for i in range(len(rewards1)):
        if i < k:
            max_reward += rewards1[i]
        else:
            max_reward += max(rewards2[i],rewards1[i])
    return max_reward
n = 5
k = 3
rewards1 = [5, 4, 3, 2, 1]
rewards2 = [1, 2, 3, 4, 5]
result = getmaxrewards(k,rewards1,rewards2)
print("Maximum rewards earned is:", result)