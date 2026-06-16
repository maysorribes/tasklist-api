import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        # Netejar la llista de tasques abans de cada prova
        from app import tasks
        tasks.clear()
        import app as app_module
        app_module.next_id = 1
        yield client


def test_get_tasks_buida(client):
    resp = client.get("/tasks")
    assert resp.status_code == 200
    assert resp.get_json() == []


def test_crear_tasca(client):
    resp = client.post("/tasks", json={"title": "Comprar pa"})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["title"] == "Comprar pa"
    assert data["done"] is False


def test_crear_tasca_sense_titol(client):
    resp = client.post("/tasks", json={})
    assert resp.status_code == 400


def test_actualitzar_tasca(client):
    client.post("/tasks", json={"title": "Tasca original"})
    resp = client.put("/tasks/1", json={"done": True})
    assert resp.status_code == 200
    assert resp.get_json()["done"] is True


def test_eliminar_tasca(client):
    client.post("/tasks", json={"title": "Tasca a eliminar"})
    resp = client.delete("/tasks/1")
    assert resp.status_code == 200
    assert client.get("/tasks").get_json() == []
