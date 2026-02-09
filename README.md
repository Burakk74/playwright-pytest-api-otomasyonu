# 🚀 Playwright & Pytest ile API Test Otomasyonu

Bu depo, modern web araçlarını kullanarak bir **API Test Otomasyon** iskeleti sunar. Proje, ölçeklenebilir test senaryoları, dinamik veri yönetimi ve otomatik raporlama özelliklerini bir araya getirir.

## ✨ Öne Çıkan Özellikler

* **Playwright APIRequestContext:** Hızlı ve güvenilir HTTP istek yönetimi.
* **JSON Schema Validation:** API yanıtlarının veri yapısını (kontratını) `jsonschema` ile otomatik doğrulama.
* **Dinamik Test Verileri:** `@pytest.mark.parametrize` ile farklı veri setlerini tek testte koşturma.
* **Uçtan Uca (E2E) Testler:** Birbirini takip eden (POST -> GET) entegrasyon senaryoları.
* **Otomatik Raporlama:** `pytest-html` ile her çalışma sonunda görsel test raporu üretimi.

## 🛠 Kullanılan Teknolojiler

- **Dil:** Python
- **Test Framework:** Pytest
- **API Engine:** Playwright
- **Validation:** JSON Schema
- **Reporting:** pytest-html

## ⚙️ Kurulum ve Kullanım

### 1. Projeyi Hazırlama
```bash
git clone [https://github.com/KULLANICI_ADIN/playwright-api-test.git](https://github.com/KULLANICI_ADIN/playwright-api-test.git)
cd playwright-api-test
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
2. Bağımlılıkları Yükleme
Bash
pip install -r requirements.txt
playwright install
3. Testleri Çalıştırma
Tüm testleri koşturmak ve HTML raporu oluşturmak için:

Bash
pytest
📂 Proje Yapısı
schemas/: API kontrat doğrulama şemaları.

tests/: API istekleri ve mantıksal test senaryoları.

conftest.py: Paylaşılan fixture (API Context) ayarları.

pytest.ini: Raporlama ve çalışma konfigürasyonları.

📊 Örnek Rapor
Testler bittiğinde dizinde oluşan report.html dosyasını tarayıcınızda açarak test sonuçlarını detaylıca inceleyebilirsiniz.