def getMessageStatus(timestamps, messages, k):
    last_delivered = {}

    def is_delivered(message, timestamp):
        last_timestamp = last_delivered.get(message, float('-inf'))
        if timestamp - last_timestamp >= k:
            last_delivered[message] = timestamp
            return True
        else:
            return False

    result = []
    for i in range(len(timestamps)):
        message = messages[i]
        timestamp = timestamps[i]
        delivered = is_delivered(message, timestamp)
        result.append(delivered)

    return result

# Example usage
n = 6
timestamps = [1, 4, 5, 10, 11, 14]
messages = ["hello", "bye", "bye", "hello", "bye", "hello"]
k = 5

status = getMessageStatus(timestamps, messages, k)
for i in range(n):
    print(f"Message '{messages[i]}' at timestamp {timestamps[i]}: {status[i]}")
