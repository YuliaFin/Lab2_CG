import unittest
from tkinter import Tk
from src.input_module import InputModule

class TestInputModuleInputValidation(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.input_module = InputModule(self.root)

    def test_get_parameters(self):
        """
        Тест проверяет, что метод get_parameters корректно возвращает параметры при правильном вводе данных
        """
        self.input_module.length_entry.delete(0, "end")
        self.input_module.length_entry.insert(0, "0.5")
        self.input_module.stiffness_entry.delete(0, "end")
        self.input_module.stiffness_entry.insert(0, "10.0")
        self.input_module.h_entry.delete(0, "end")
        self.input_module.h_entry.insert(0, "10.0")

        L, C, h = self.input_module.get_parameters()

        self.assertEqual(L, 0.5)
        self.assertEqual(C, 10.0)
        self.assertEqual(h, 10.0)

    def test_invalid_input(self):
        """
        Тест проверяет, что метод get_parameters генерирует исключение ValueError при некорректном вводе данных
        """
        self.input_module.length_entry.insert(0, "abc")  # Длина должна быть числом
        self.input_module.stiffness_entry.insert(0, "xyz")  # Коэффициент упругости должен быть числом
        self.input_module.h_entry.insert(0, "-5.0")  # Смещение не может быть отрицательным

        # Попытка получить параметры должна вызвать ValueError
        with self.assertRaises(ValueError):
            self.input_module.get_parameters()

if __name__ == '__main__':
    unittest.main()
