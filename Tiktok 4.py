def getMaxRequests(bandwidth, requests, total_bandwidth):
    n = len(bandwidth)
    max_requests = 0

    def getmax_1(index, current_bandwidth, current_requests):
        nonlocal max_requests

        if index == n:
            max_requests = max(max_requests, current_requests)
            return

        # Try allocating bandwidth to the current endpoint
        if current_bandwidth + bandwidth[index] <= total_bandwidth:
            getmax_1(index + 1, current_bandwidth + bandwidth[index], current_requests + requests[index])

        # Skip the current endpoint
        getmax_1(index + 1, current_bandwidth, current_requests)

    getmax_1(0, 0, 0)
    return max_requests

# Example usage
n = 5
total_bandwidth = 500
bandwidth = [200, 100, 350, 50, 100]
requests = [270, 142, 450, 124, 189]

result = getMaxRequests(bandwidth, requests, total_bandwidth)
print(result)