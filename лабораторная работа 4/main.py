from validation import input_voltage, input_current
from menu import show_menu, select_mode
from operations import power, voltage_class

def main() -> None:
    """Главный сценарий."""
    print("=== Расчёт мощности электропривода ===")
    while True:
        show_menu()
        result = select_mode()
        if result is None:
            print("Работа завершена.")
            break

        cos_phi, load_name = result

        u = input_voltage()
        i = input_current()

        p = power(u, i, cos_phi)
        v_cls = voltage_class(u)

        print('\n')
        print('='*100)
        print(" Результаты ")
        print(f"Тип нагрузки: {load_name} (cos φ = {cos_phi})")
        print(f"P (мощность): {p:.2f} кВт")
        print(f"Класс напряжения: {v_cls}")
        print('='*100)
        print("\n")
        
        
if __name__ == "__main__":
    main()