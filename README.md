# Unit-тесты для BooksCollector

## Сценарии, покрытые тестами
| № | Метод класса | Что проверяем |
|---|--------------|---------------|
| 1 | add_new_book | граничные значения (1 и 40 символов) |
| 2 | add_new_book | запрет пустой строки и 41+ символов |
| 3 | add_new_book | защита от дублирования |
| 4 | set_book_genre | установка валидного жанра |
| 5 | set_book_genre | игнор невалидного жанра |
| 6 | get_book_genre | возврат жанра по названию |
| 7 | get_books_with_specific_genre | список по жанру / пустой список |
| 8 | get_books_genre | полный словарь книг-жанров |
| 9 | get_books_for_children | фильтр 18+ жанров |
|10 | add_book_in_favorites | добавление в избранное без дублей |
|11 | delete_book_from_favorites | удаление из избранного |
|12 | get_list_of_favorites_books | актуальный список избранных |
|13 | комбинированно | add+delete favorites в одном тесте |

## Запуск тестов
```bash
pytest -v tests.py
