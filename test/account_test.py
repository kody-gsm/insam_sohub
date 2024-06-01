from fastapi.testclient import TestClient
from httpx import Response
from main import app  # 위의 FastAPI 애플리케이션 코드가 'main.py'에 저장되어 있다고 가정합니다.

SUPER_TOKEN = "IT'S_SUPER_TOKEN"
SUPER_REFRESH_TOKEN = "IT'S_SUPER_REFRESH_TOKEN"

USER_EMAIL = "test@test.test"
USER_PASSWORD = "itistestPW"

client = TestClient(app)

def test_login():
    response:Response = client.post("user/account/login", json={"email":USER_EMAIL, "password": USER_PASSWORD})
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {
        "refresh_token":SUPER_TOKEN,
        "access_token":SUPER_REFRESH_TOKEN}