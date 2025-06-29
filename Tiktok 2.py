def getMaxRequests(bandwidth, requests, total_bandwidth):
    n = len(bandwidth)
    m = 0

    def getmax_1(i, band, req):
        nonlocal m

        if i == n:
            m = max(m,req)
            return

        if band + bandwidth[i] <= total_bandwidth:
            getmax_1(i + 1, band + bandwidth[i], req + requests[i])

        getmax_1(i + 1, band, req)

    getmax_1(0, 0, 0)
    return m
n = 5
total_bandwidth = 500
bandwidth = [200, 100, 350, 50, 100]
requests = [270, 142, 450, 124, 189]

result = getMaxRequests(bandwidth, requests, total_bandwidth)
print(result)
