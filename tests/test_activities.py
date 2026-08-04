def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert "Chess Club" in payload
    assert set(payload["Chess Club"].keys()) == expected_keys


def test_get_activities_includes_participant_lists(client):
    # Arrange
    activity_name = "Debate Team"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert payload[activity_name]["participants"] == [
        "nathan@mergington.edu",
        "lily@mergington.edu",
        "mason@mergington.edu",
    ]