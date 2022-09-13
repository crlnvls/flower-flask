
def test_index_route(api):

    response = api.get("/")

    assert response.status == "200 OK"
    
    assert b"Welcome to the Flower Factory!" in response.data

def test_flowers_post_route(api):

    response = api.post("/flowers")

    assert response.status == "405 METHOD NOT ALLOWED"
    assert response.status_code == 405

def test_new_flower_route(api):

    response = api.post("/flowers/new")

    assert response.status_code == 400

    data = {
        "color": "green"
    }

    response = api.post("/flowers/new", json=data)

    assert response.status_code == 201
