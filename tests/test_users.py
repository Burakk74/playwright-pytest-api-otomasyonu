import pytest
from jsonschema import validate
from schemas.user_schema import USER_SCHEMA

# Birden fazla kullanıcıyı tek seferde test edelim
@pytest.mark.parametrize("user_id", [1, 2, 5])
def test_get_multiple_users_schema(api_context, user_id):
    response = api_context.get(f"/users/{user_id}")
    assert response.ok
    
    response_body = response.json()
    validate(instance=response_body, schema=USER_SCHEMA)
    print(f"\nKullanıcı ID {user_id} için şema doğrulaması başarılı.")

# Negatif Test: Olmayan kullanıcı
def test_get_non_existing_user(api_context):
    response = api_context.get("/users/999")
    
    # 404 dönmesini bekliyoruz
    assert response.status == 404
    assert not response.ok