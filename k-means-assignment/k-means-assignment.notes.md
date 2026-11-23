## My version has a bug

def k_means_assignment(points: list, centroids: list) -&gt; list:

    """

    Returns the nearest-centroid index for every point.

    """

    rlst=[]

    # Write code here

    for j in points:

       best_dist = float('inf')

       best_idx = 0

       for idx, i in enumerate(centroids):

        dist1=(j[0]-i[0])**2

        dist2=(j[1]-i[1])**2

        s=dist1+dist2

        if s&lt;best_dist:

            best_idx=idx

            best_dist=s

       rlst.append(best_idx)

    return rlst




## AI version

```python
def k_means_assignment(points: list, centroids: list) -&gt; list:
    def dist(p, c):
        return sum((a - b) ** 2 for a, b in zip(p, c))

    return [min(range(len(centroids)), key=lambda i: dist(p, centroids[i]))
            for p in points]
```