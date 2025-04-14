from flask_login import logout_user


def test_register_and_login(client):
    # Register
    response = client.post(
        "/register",
        data={"username": "testuser", "password": "testpass"},
        follow_redirects=True,
    )
    assert b"Account created" in response.data or b"Login" in response.data

    # Loging
    response = client.post(
        "/login",
        data={"username": "testuser", "password": "testpass"},
        follow_redirects=True,
    )
    assert b"Logged in succesfully" in response.data or b"Mood tracker" in response.data


def test_logout_user(client):
    # Logout
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

    response = client.get("/logout", follow_redirects=True)
    assert b"Login" in response.data or b"Register" in response.data
