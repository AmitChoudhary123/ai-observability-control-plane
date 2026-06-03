from pathlib import Path
from src.observability.main import evaluate_slo, load_telemetry

if __name__ == "__main__":
    summary = evaluate_slo(load_telemetry(Path("data/genai_request_traces.csv")))
    print("Healthy rate:", summary["healthy_rate"])
    print("Average cost:", summary["avg_cost_usd"])
    print("p95 latency:", summary["p95_latency_ms"])
    for request in summary["requests"]:
        print(request["request_id"], "healthy=" + str(request["healthy"]))