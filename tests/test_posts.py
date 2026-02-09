import pytest
from jsonschema import validate
from schemas.user_schema import CREATE_POST_SCHEMA

# --- 1. Test: Tekil Kayıt Testi ---
def test_create_new_post(api_context):
    # 1. Gönderilecek Veri (Payload)
    payload = {
        "title": "Playwright ile API Testi",
        "body": "Bu içerik otomatik test ile oluşturuldu.",
        "userId": 1
    }

    # 2. POST İsteği Atma
    response = api_context.post("/posts", data=payload)

    # 3. Temel Kontroller
    assert response.status == 201  # HTTP 201 Created
    
    response_body = response.json()
    
    # 4. Şema Doğrulaması
    validate(instance=response_body, schema=CREATE_POST_SCHEMA)

    # 5. İçerik Doğrulaması
    assert response_body["title"] == payload["title"]
    assert response_body["userId"] == payload["userId"]


# --- 2. Test: Dinamik Verili Çoklu Kayıt Testi ---
@pytest.mark.parametrize("title, userId", [
    ("Kısa Başlık", 1),
    ("!@#$%^&*()_+", 2),
    ("Çok " * 20 + "Uzun Başlık", 3)
])
def test_create_post_dynamic(api_context, title, userId):
    # Payload hazırlama
    payload = {
        "title": title,
        "body": "Test gövdesi",
        "userId": userId
    }
    
    # İstek gönderme
    response = api_context.post("/posts", data=payload)
    
    # Durum kodu kontrolü
    assert response.status == 201 
    
    # Dönen datanın başlık doğruluğunu kontrol etme
    assert response.json()["title"] == title