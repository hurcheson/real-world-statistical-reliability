from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "outputs" / "determinism" / "run1" / "2016"
OUT = ROOT / "outputs" / "figures"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name: str) -> None:
    fig.tight_layout()
    fig.savefig(OUT / f"{name}.png", dpi=220, bbox_inches="tight")
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight")
    plt.close(fig)


def population_gradient() -> None:
    data = pd.read_csv(SOURCE / "population_quintiles.csv")
    data["loss_percent"] = 100 * data["loss_rate"]
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    bars = ax.bar(data["population_quintile"].astype(str), data["loss_percent"], color="#286486")
    ax.set_xlabel("Population quintile (Q1 = lowest)")
    ax.set_ylabel("Eligibility loss rate (%)")
    ax.set_title("Eligibility loss under the tighter precision screen")
    ax.set_ylim(0, 12)
    ax.grid(axis="y", color="#d9d9d9", linewidth=0.8)
    ax.set_axisbelow(True)
    for bar, value in zip(bars, data["loss_percent"]):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 0.25, f"{value:.2f}%", ha="center", fontsize=9)
    save(fig, "figure_1_population_loss_gradient")


def churn_decomposition() -> None:
    result = pd.read_csv(SOURCE / "annual_result.csv").iloc[0]
    categories = ["L1", "L2", "L3", "G1", "G2"]
    values = [int(result[c]) for c in categories]
    labels = ["Eligibility loss", "Own-screen loss", "Strict non-local loss",
              "Own-screen gain", "Strict non-local gain"]
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    bars = ax.barh(labels[::-1], values[::-1], color=["#6a9f58", "#6a9f58", "#b06b4f", "#b06b4f", "#b06b4f"])
    ax.set_xlabel("Records")
    ax.set_title("Five-part decomposition of 864 designation changes")
    ax.grid(axis="x", color="#d9d9d9", linewidth=0.8)
    ax.set_axisbelow(True)
    for bar, value in zip(bars, values[::-1]):
        ax.text(value + 7, bar.get_y() + bar.get_height() / 2, f"{value}", va="center", fontsize=9)
    ax.set_xlim(0, 520)
    save(fig, "figure_2_churn_decomposition")


if __name__ == "__main__":
    population_gradient()
    churn_decomposition()
