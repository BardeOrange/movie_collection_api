class TestHealth:
    """Tests for the health check endpoint."""

    def test_health_check(self, client):
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "running"
        assert "app" in data
