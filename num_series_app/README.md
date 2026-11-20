markdown
### Замер производительности скользящей средней
Для сравнения реализаций SMA через список и через `deque` используйте флаг `--
benchmark`:
```bash
python main.py --kind random --n 5000 --window 20 --benchmark
Будут выведены средние времена выполнения (в секундах) для обеих реализаций.
text
---
## 5. (Опционально) Тесты
Можно добавить тест в `tests/test_moving_average.py`:
```python
def test_simple_moving_average_deque():
 from num_series.moving_average import simple_moving_average_deque
 assert simple_moving_average_deque([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0]
 with pytest.raises(ValueError):
 simple_moving_average_deque([1, 2], 3)