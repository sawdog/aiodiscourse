import pytest
import os


@pytest.fixture(scope='session')
def discourse_url():
    return os.environ.get('DISCOURSE_URL', 'http://localhost:3000')


@pytest.fixture(scope='session')
def api_key():
    return os.environ.get('DISCOURSE_API_KEY', 'dev-key')


@pytest.fixture(scope='session')
def api_user():
    return os.environ.get('DISCOURSE_API_USER', 'system')
