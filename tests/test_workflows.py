from src.app import activities


def test_register_then_unregister_roundtrip(client):
    # Arrange
    activity_name = "Chess Club"
    activity_path = "Chess%20Club"
    email = "roundtrip.student@mergington.edu"

    # Act
    signup_response = client.post(f"/activities/{activity_path}/signup", params={"email": email})
    unregister_response = client.delete(f"/activities/{activity_path}/signup", params={"email": email})

    # Assert
    assert signup_response.status_code == 200
    assert unregister_response.status_code == 200
    assert email not in activities[activity_name]["participants"]


def test_duplicate_signup_regression(client):
    # Arrange
    activity_name = "Science Club"
    email = "repeat.student@mergington.edu"

    # Act
    first_response = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    second_response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert first_response.status_code == 200
    assert second_response.status_code == 400
    assert second_response.json() == {
        "detail": "Student already signed up for this activity"
    }