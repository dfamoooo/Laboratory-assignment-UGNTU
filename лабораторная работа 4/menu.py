
#Меню выбора типа нагрузки через match-case.

from __future__ import annotations
from constans import COS_ACTIVE, COS_INDUCTIVE, COS_MIXED


def show_menu() -> None:
    """Вывести меню типов нагрузки."""
    print('-'*50)
    print(" Выберите тип нагрузки:")
    print("  1 — активная нагрузка, cos φ = 1.0")
    print("  2 — индуктивная, cos φ = 0.85")
    print("  3 — смешанная, cos φ = 0.75")
    print("  0 — выход")
    print('-'*50)
    


def select_mode() -> tuple[float, str] | None:
    """
    Циклически запрашивать режим.
    Возвращает (cos_phi, name) или None при выходе.
    """
    while True:
        choice = input("Введите номер режима (от 0 до 3): ").strip()
        match choice:
            case "1":
                return COS_ACTIVE, "активная"
            case "2":
                return COS_INDUCTIVE, "индуктивная"
            case "3":
                return COS_MIXED, "смешанная"
            case "0":
                return None
            case _:
                print("Ошибка: неверный пункт меню. Повторите ввод.")