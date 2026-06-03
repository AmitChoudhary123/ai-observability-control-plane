from __future__ import annotations

import csv
from pathlib import Path


def summarize_request(latency_ms: int, token_cost_usd: float, quality_score: float) -> dict:
    healthy = latency_ms <= 3000 and token_cost_usd <= 0.05 and quality_score >= 0.8
    return {"latency_ms": latency_ms, "cost_usd": round(token_cost_usd, 4), "quality_score": quality_score, "healthy": healthy}


def load_telemetry(path: str | Path) -> list[dict]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        row["latency_ms"] = int(row["latency_ms"])
        row["cost_usd"] = float(row["cost_usd"])
        row["quality_score"] = float(row["quality_score"])
    return rows


def evaluate_slo(rows: list[dict]) -> dict:
    evaluated = [{**row, **summarize_request(row["latency_ms"], row["cost_usd"], row["quality_score"])} for row in rows]
    healthy_count = sum(1 for row in evaluated if row["healthy"])
    avg_cost = sum(row["cost_usd"] for row in evaluated) / len(evaluated)
    p95_latency = sorted(row["latency_ms"] for row in evaluated)[-1]
    return {"requests": evaluated, "healthy_rate": round(healthy_count / len(evaluated), 2), "avg_cost_usd": round(avg_cost, 4), "p95_latency_ms": p95_latency}