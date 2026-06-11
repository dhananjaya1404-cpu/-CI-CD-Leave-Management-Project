import pytest
from app import app, LEAVES

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_dashboard_loads(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"LeaveSync" in res.data

def test_apply_page_loads(client):
    res = client.get("/apply")
    assert res.status_code == 200

def test_submit_leave(client):
    before = len(LEAVES)
    client.post("/apply", data={
        "type": "Sick", "from_date": "2026-06-01",
        "to_date": "2026-06-01", "days": 1, "reason": "Cold"
    }, follow_redirects=True)
    assert len(LEAVES) == before + 1

def test_submit_leave_no_reason(client):
    before = len(LEAVES)
    client.post("/apply", data={
        "type": "Casual", "from_date": "2026-06-05",
        "to_date": "2026-06-05", "days": 1, "reason": ""
    }, follow_redirects=True)
    assert len(LEAVES) == before

def test_my_leaves(client):
    res = client.get("/my-leaves")
    assert res.status_code == 200

def test_team_page(client):
    res = client.get("/team")
    assert res.status_code == 200

def test_admin_page(client):
    res = client.get("/admin")
    assert res.status_code == 200

def test_admin_approve(client):
    client.post("/admin/action/L001/approve", follow_redirects=True)
    leave = next(l for l in LEAVES if l["id"] == "L001")
    assert leave["status"] == "Approved"

def test_health(client):
    res = client.get("/health")
    assert res.get_json()["status"] == "healthy"