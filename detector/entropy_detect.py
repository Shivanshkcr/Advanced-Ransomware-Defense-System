import math
from collections import Counter


def calculate_entropy(data):
    """
    Calculates Shannon entropy of byte data.
    High entropy (~7.5-8) indicates encrypted/compressed data.
    """

    if not data:
        return 0.0

    try:
        counts = Counter(data)
        entropy = 0.0

        for count in counts.values():
            p = count / len(data)
            entropy -= p * math.log2(p)

        return round(entropy, 3)

    except Exception as e:
        print(f"[ERROR] Entropy calculation failed: {e}")
        return 0.0