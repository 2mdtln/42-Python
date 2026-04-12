# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   loading.py                                          :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/12 10:49:22 by mtaheri            #+#    #+#             #
#   Updated: 2026/04/12 13:14:12 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys
import importlib
import importlib.util


def check_dependencies() -> list[str]:
    missing = []

    print("Checking dependencies:")
    for package in ["pandas", "numpy", "matplotlib", "requests"]:
        spec = importlib.util.find_spec(package)
        if spec is None:
            print(f"[MISSING] {package}")
            missing.append(package)
        else:
            version = getattr(importlib.import_module(package),
                              "__version__", "unknown")
            print(f"[OK] {package} ({version})")
    return missing


def fetch_contributions() -> list[dict]:
    import requests

    html = requests.get("https://github.com/users/2mdtln/contributions").text
    dates = [p[:10] for p in html.split('data-date="')[1:]]
    tips = [p[:p.find("<")]
            for p in html.split('class="sr-only position-absolute">')[1:]]
    rows = []

    for date_str, tip in zip(dates, tips):
        count = 0 if tip.startswith("No") else int(tip.split()[0])
        rows.append({"date": date_str, "count": count})
    return rows


def run_analysis() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print("\nFetching contribution history...")
    df = pd.DataFrame(fetch_contributions())
    df["date"] = pd.to_datetime(df["date"])

    since = pd.Timestamp.now() - pd.DateOffset(months=5)
    df = df[df["date"] >= since].copy()

    total = int(df["count"].sum())
    print(f"Processing {total} contributions over 5 months...")

    df["week"] = df["date"].dt.to_period("W").apply(lambda p: p.start_time)
    weekly = df.groupby("week")["count"].sum().reset_index()
    counts = np.array(weekly["count"])

    print("Generating visualization...")

    fig, axes = plt.subplots(1, 1, figsize=(8, 6))
    fig.suptitle(
        f"2mdtln — last 5 months  "
        f"({total} contributions, avg {counts.mean():.1f}/week)",
        fontsize=13,
    )

    axes.bar(weekly["week"], weekly["count"],
             color="green", alpha=0.8, width=5)
    axes.set_title("Contributions per Week")
    axes.set_xlabel("Week")
    axes.set_ylabel("Contributions")
    axes.tick_params(axis="x", rotation=45)

    plt.tight_layout()
    output = "contribution-analysis.png"
    plt.savefig(output, dpi=150)
    plt.close()

    print("\nAnalysis complete!")
    print(f"Results saved to: {output}")


def main() -> None:
    missing = check_dependencies()
    if missing:
        print("\nInstall with pip:")
        print("  pip install -r requirements.txt\n")
        print("Install with Poetry:")
        print("  poetry install")
        sys.exit(1)
    run_analysis()


if __name__ == "__main__":
    main()
