#Расчёты: мощность P, класс напряжения.

from typing import Annotated

from constans import U_LOW_LIMIT, U_HIGH_LIMIT


#Рассчитывает мощность P=U*I*cos_phi/1000 кВт
def power(
    u: Annotated[float, "Напряжение, В"],
    i: Annotated[float, "Ток, А"],
    cos_phi: Annotated[float, "Коэффициент мощности"],
) -> float:
    
    return u * i * cos_phi / 1000.0

""" Классифицировать напряжение через if-elif-else.
    U<220 — низкое
    220<=U<=400 — нормальное
    U>400 — высокое """

def voltage_class(
    u: Annotated[float, "Напряжение, В"],
) -> str:
    if u < U_LOW_LIMIT:
        return "низкое напряжение"
    elif u <= U_HIGH_LIMIT:
        return "нормальное напряжение"
    else:
        return "высокое напряжение"