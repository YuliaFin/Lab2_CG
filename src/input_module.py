from tkinter import ttk

class InputModule:
    """
    Класс для создания графического интерфейса и ввода параметров пружины.

    Параметры:
        root (Tk): Корневой элемент Tkinter, на котором будет создан пользовательский интерфейс.
    """
    def __init__(self, root):
        """
        Инициализация экземпляра класса.

        :param root: Корневой элемент Tkinter, на котором будет создан пользовательский интерфейс.
        """
        self.root = root
        self.root.title("Параметры пружины")

        # Метка и поле ввода для длины недеформированной пружины L
        self.length_label = ttk.Label(root, text="Длина недеформированной пружины (L, м):")
        self.length_label.pack()
        self.length_entry = ttk.Entry(root)
        self.length_entry.insert(0, "0.5")  # Значение по умолчанию
        self.length_entry.pack()

        # Метка и поле ввода для коэффициента упругости C
        self.stiffness_label = ttk.Label(root, text="Коэффициент упругости пружины (C, Н/м):")
        self.stiffness_label.pack()
        self.stiffness_entry = ttk.Entry(root)
        self.stiffness_entry.insert(0, "10.0")  # Значение по умолчанию
        self.stiffness_entry.pack()

        # Метка и поле ввода для смещения шарика h
        self.h_label = ttk.Label(root, text="Смещение шарика вниз (h, см):")
        self.h_label.pack()
        self.h_entry = ttk.Entry(root)
        self.h_entry.insert(0, "10.0")  # Значение по умолчанию
        self.h_entry.pack()

    def get_parameters(self):
        """
        Получает введенные пользователем параметры.

        :return: Кортеж с параметрами (L, C, h).
        """
        L = float(self.length_entry.get())
        C = float(self.stiffness_entry.get())
        h = float(self.h_entry.get())
        return L, C, h
