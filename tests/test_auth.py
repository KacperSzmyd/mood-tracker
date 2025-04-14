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
