#!/usr/bin/env python3
"""Snap a requested MiniMax H3 duration to ComfyUI's 17k+5 frame grid."""

from __future__ import annotations

import argparse
import json
import math


FPS = 24
MIN_SECONDS = 4.0
MAX_SECONDS = 15.0
MIN_K = 6
MAX_K = 21


def snap_duration(requested_seconds: float) -> dict[str, float | int]:
    if not MIN_SECONDS <= requested_seconds <= MAX_SECONDS:
        raise ValueError(
            f"requested duration must be between {MIN_SECONDS:g} and {MAX_SECONDS:g} seconds"
        )

    raw_k = (requested_seconds * FPS - 5) / 17
    k = math.floor(raw_k + 0.5)
    k = min(MAX_K, max(MIN_K, k))
    frames = 17 * k + 5
    effective_seconds = frames / FPS
    effective_seconds_2dp = math.floor(effective_seconds * 100 + 0.5) / 100

    return {
        "requested_seconds": requested_seconds,
        "k": k,
        "frames": frames,
        "fps": FPS,
        "effective_seconds": effective_seconds,
        "effective_seconds_2dp": effective_seconds_2dp,
        "delta_seconds": effective_seconds - requested_seconds,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Snap 4-15 seconds to MiniMax H3's ComfyUI 17k+5 frame grid."
    )
    parser.add_argument("seconds", type=float, help="requested duration in seconds")
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    args = parser.parse_args()

    try:
        result = snap_duration(args.seconds)
    except ValueError as exc:
        parser.error(str(exc))

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    print(f"requested: {result['requested_seconds']:.2f} s")
    print(f"frames: {result['frames']} ({result['k']} blocks on 17k+5 grid)")
    print(f"effective: {result['effective_seconds']:.6f} s")
    print(f"alignment: {result['effective_seconds_2dp']:.2f} s")
    print(f"delta: {result['delta_seconds']:+.6f} s")


if __name__ == "__main__":
    main()
