import unittest
from tkinter import Tk
from src.drawing_module import DrawingModule
from src.input_module import InputModule

class TestDrawingModule(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.input_module = InputModule(self.root)
        self.drawing_module = DrawingModule(self.input_module)

    def test_show_animation(self):
        """
        Тест проверяет, что метод show_animation выполняется без ошибок.
        """
        try:
            self.drawing_module.show_animation()
        except Exception as e:
            self.fail(f"show_animation raised an exception: {e}")


if __name__ == '__main__':
    unittest.main()
