def login_user(client):
    client.post(
        "/register",
        data={"username": "testuser", "password": "testpass"},
        follow_redirects=True,
    )

    client.post(
        "/login",
        data={"username": "testuser", "password": "testpass"},
        follow_redirects=True,
    )


def test_mood_view_requires_login(client):
    response = client.get("/", follow_redirects=True)
    assert b"Login" in response.data


def test_add_mood(client):
    login_user(client)

    response = client.post("/", data={"mood": "happy"}, follow_redirects=True)
    assert b"happy" in response.data


def test_moods_are_user_specific(client):
    #USER A
    client.post("/register", data={"username": "testuserA", "password": "a"}, follow_redirects=True)
    client.post("/login", data={"username": "testuserA", "password": "a"}, follow_redirects=True)
    client.post("/", data={"mood": "confident"}, follow_redirects=True)
    client.get("/logout", follow_redirects=True)
    
    #USER B
    client.post("/register", data={"username": "testuserB", "password": "b"}, follow_redirects=True)
    client.post("/login", data={"username": "testuserB", "password": "b"}, follow_redirects=True)
    response = client.get("/", follow_redirects=True)
    assert b'confident' not in response.data