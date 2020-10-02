from app.config import get_settings


def test_status(test_app):
    # Given
    # test_app

    # When
    response = test_app.get("/status")

    # Then
    assert response.status_code == 200
    assert response.json() == {
        "version": get_settings().version,
        "status": "running",
        "environment": get_settings().environment,
        "testing": get_settings().testing,
    }
