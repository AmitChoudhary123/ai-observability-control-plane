from src.observability.main import summarize_request


def test_healthy_request_meets_slo():
    assert summarize_request(1200, 0.02, 0.9)["healthy"] is True


def test_latency_breach_fails_slo():
    assert summarize_request(5000, 0.02, 0.9)["healthy"] is False