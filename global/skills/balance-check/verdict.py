"""Win-rate verdict for a balance batch (balance-check skill, step 3).

The 95% Wilson range of a win rate, the verdict against a fair band, and roughly how many more decided matches would
settle an unclear batch. Ported from the first game project's balance-stats tool (SU-Q76); standard library only.
"""

import argparse
import math
import sys

Z95 = 1.96
MAX_MORE = 5000  # beyond this many extra matches a batch is called borderline


def wilson(wins, n, z=Z95):
    """Wilson score range of wins out of n, as (low, high) fractions; (0, 1) for n = 0."""
    if n <= 0:
        return (0.0, 1.0)
    p = wins / n
    z2 = z * z
    centre = (p + z2 / (2 * n)) / (1 + z2 / n)
    half = (z * math.sqrt(p * (1 - p) / n + z2 / (4 * n * n))) / (1 + z2 / n)
    return (max(0.0, centre - half), min(1.0, centre + half))


def verdict(rng, band):
    """'fair' when the range sits inside the band, 'unbalanced' when wholly outside it, else 'unclear'."""
    low, high = rng
    if low >= band[0] and high <= band[1]:
        return "fair"
    if high < band[0] or low > band[1]:
        return "unbalanced"
    return "unclear"


def more_needed(wins, n, band, z=Z95):
    """Extra decided matches until the range clears the band edge nearest the rate, if the rate holds.

    0 when already settled; math.inf when the rate sits on a band edge (no batch size settles it).
    """
    if n > 0 and verdict(wilson(wins, n, z), band) != "unclear":
        return 0
    p = wins / n if n > 0 else 0.5
    mid = (band[0] + band[1]) / 2
    half_band = (band[1] - band[0]) / 2
    margin = abs(abs(p - mid) - half_band)
    if margin < 1e-9:
        return math.inf
    variance = max(p * (1 - p), 0.01)
    total = math.ceil(z * z * variance / (margin * margin))
    return max(1, total - n)


def report(wins, n, band):
    low, high = wilson(wins, n)
    v = verdict((low, high), band)
    line = f"{wins}/{n} = {100 * wins / n:.1f}%, 95% range {100 * low:.1f}-{100 * high:.1f}%"
    if v == "unclear":
        more = more_needed(wins, n, band)
        v = "borderline" if more > MAX_MORE else f"unclear, run about {more} more"
    return f"{line}: {v}"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Verdict for a batch's win rate against a fair band.")
    ap.add_argument("wins", type=int, help="matches the side under test won")
    ap.add_argument("decided", type=int, help="decided matches (time-limit draws left out)")
    ap.add_argument("--band", type=float, nargs=2, default=[45, 55], metavar=("LOW", "HIGH"),
                    help="fair band in percent (default 45 55)")
    a = ap.parse_args(argv)
    if a.decided <= 0 or not 0 <= a.wins <= a.decided:
        ap.error("need 0 <= wins <= decided and decided > 0")
    band = (a.band[0] / 100, a.band[1] / 100)
    print(report(a.wins, a.decided, band))
    return 0


if __name__ == "__main__":
    sys.exit(main())
