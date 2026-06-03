def summarize_request(latency_ms: int, token_cost_usd: float, quality_score: float) -> dict:
    """Classify a GenAI request against enterprise SLO thresholds."""
    healthy = latency_ms <= 3000 and token_cost_usd <= 0.05 and quality_score >= 0.8
    return {"latency_ms": latency_ms, "cost_usd": round(token_cost_usd, 4), "quality_score": quality_score, "healthy": healthy}