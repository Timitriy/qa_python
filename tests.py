import pytest
from main import BooksCollector


# ---------- фикстура ----------
@pytest.fixture()
def collector():
    """Свежий экземпляр BooksCollector для каждого теста."""
    return BooksCollector()


# ---------- add_new_book ----------
@pytest.mark.parametrize(
    'title',
    ['Книга', 'A' * 40]          # граничные значения: 1 и 40 символов
)
def test_add_new_book_positive(collector, title):
    collector.add_new_book(title)
    assert title in collector.books_genre
    assert collector.books_genre[title] == ''          # жанр ещё не задан


@pytest.mark.parametrize(
    'title',
    ['', 'A' * 41]               # пустая строка и 41 символ
)
def test_add_new_book_invalid_length(collector, title):
    collector.add_new_book(title)
    assert title not in collector.books_genre


def test_add_new_book_duplicate(collector):
    collector.add_new_book('Дюна')
    collector.add_new_book('Дюна')
    assert list(collector.books_genre.keys()).count('Дюна') == 1


# ---------- set_book_genre ----------
def test_set_book_genre_valid(collector):
    collector.add_new_book('Дюна')
    collector.set_book_genre('Дюна', 'Фантастика')
    assert collector.books_genre['Дюна'] == 'Фантастика'


def test_set_book_genre_invalid(collector):
    collector.add_new_book('Дюна')
    collector.set_book_genre('Дюна', 'Поэзия')          # жанр вне списка
    assert collector.books_genre['Дюна'] == ''


# ---------- get_book_genre ----------
def test_get_book_genre_returns_value(collector):
    collector.add_new_book('Дюна')
    collector.set_book_genre('Дюна', 'Фантастика')
    assert collector.get_book_genre('Дюна') == 'Фантастика'


# ---------- get_books_with_specific_genre ----------
@pytest.mark.parametrize(
    'genre, expected',
    [
        ('Фантастика', ['Дюна', 'Гиперион']),
        ('Комедии',    [])                       # жанр без книг → пусто
    ]
)
def test_get_books_with_specific_genre(collector, genre, expected):
    for title in ['Дюна', 'Гиперион']:
        collector.add_new_book(title)
        collector.set_book_genre(title, 'Фантастика')
    assert collector.get_books_with_specific_genre(genre) == expected


# ---------- get_books_genre ----------
def test_get_books_genre_returns_full_dict(collector):
    collector.add_new_book('Дюна')
    collector.set_book_genre('Дюна', 'Фантастика')
    assert collector.get_books_genre() == {'Дюна': 'Фантастика'}


# ---------- get_books_for_children ----------
def test_get_books_for_children_filters_age_rating(collector):
    collector.add_new_book('Оно')
    collector.set_book_genre('Оно', 'Ужасы')            # возрастной жанр
    collector.add_new_book('Золушка')
    collector.set_book_genre('Золушка', 'Мультфильмы')  # детский жанр
    assert collector.get_books_for_children() == ['Золушка']


# ---------- favorites (add / delete / get) ----------
def test_favorites_add_and_delete(collector):
    collector.add_new_book('Дюна')

    # добавляем в избранное (повторно не дублируется)
    collector.add_book_in_favorites('Дюна')
    collector.add_book_in_favorites('Дюна')
    assert collector.get_list_of_favorites_books() == ['Дюна']

    # удаляем
    collector.delete_book_from_favorites('Дюна')
    assert collector.get_list_of_favorites_books() == []
