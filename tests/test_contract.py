from pathlib import Path
from src.observability.main import evaluate_slo, load_telemetry, summarize_request


def test_observability_demo_detects_breaches():
    summary = evaluate_slo(load_telemetry(Path("data/genai_request_traces.csv")))
    assert summary["healthy_rate"] < 1.0
    assert summary["p95_latency_ms"] >= 4100


def test_latency_breach_fails_slo():
    assert summarize_request(5000, 0.02, 0.9)["healthy"] is False