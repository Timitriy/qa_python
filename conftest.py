# conftest.py
import pytest
from main import BooksCollector


@pytest.fixture()
def collector() -> BooksCollector:
    """Свежий экземпляр BooksCollector для каждого теста.
    Помещён в conftest.py, чтобы был доступен во всех тест-модулях без импортов.
    """
    return BooksCollector()