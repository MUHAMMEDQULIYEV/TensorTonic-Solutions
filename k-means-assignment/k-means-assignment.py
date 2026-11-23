def k_means_assignment(points: list, centroids: list) -> list:
    def dist(p, c):
        return sum((a - b) ** 2 for a, b in zip(p, c))

    return [min(range(len(centroids)), key=lambda i: dist(p, centroids[i]))
            for p in points]