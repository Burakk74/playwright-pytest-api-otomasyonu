import pytest
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
    # Bu 'playwright' objesi artık pytest-playwright eklentisi tarafından otomatik sağlanacak
    request_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    yield request_context
    request_context.dispose()