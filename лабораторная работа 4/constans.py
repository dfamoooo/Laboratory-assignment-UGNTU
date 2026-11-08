# коэффициенты типов нагрузок
K_ACTIVE: float = 1.0     #активная
K_INDUCTIVE: float = 0.85 #индуктивная
K_MIXED: float = 0.75     #смешанная

#Допустимые диапазоны
U_MIN=12
U_MAX=1000
I_MIN=0.1
I_MAX=500

#Пороговые значения границ напряжения
U_MIN_LIMIT: float = 220.0
U_MAX_LIMIT: float = 400.0

"""def is_voltage_normal(u: float) -> bool:
    return U_MIN_LIMIT < u < U_MAX_LIMIT"""

import math

#Коэффициенты мощности (cos)
COS_ACTIVE: float = 1.0     # активная нагрузка
COS_INDUCTIVE: float = 0.85 # индуктивная
COS_MIXED: float = 0.75     # смешанная

#Допустимые диапазоны входных данных
U_MIN: float = 12.0
U_MAX: float = 1000.0
I_MIN: float = 0.1
I_MAX: float = 500.0

#Пороговые значения для классификации напряжения
U_LOW_LIMIT: float = 220.0     # U<220 — низкое
U_HIGH_LIMIT: float = 400.0    # U>400 — высокое

#Файл журнала ошибок
LOG_FILE: str = "input_errors.log"