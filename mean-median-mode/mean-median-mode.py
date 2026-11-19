import numpy as np
from collections import Counter

def mean_median_mode(x):
    arr = np.asarray(x, dtype=float)

    mean = float(np.mean(arr))
    median = float(np.median(arr))

    counts = Counter(arr.tolist())
    max_freq = max(counts.values())
    mode = min(k for k, v in counts.items() if v == max_freq)

    return {"mean": mean, "median": median, "mode": float(mode)}