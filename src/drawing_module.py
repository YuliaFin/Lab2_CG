import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math

class DrawingModule:
    """
    Класс для отрисовки анимации вертикальных колебаний пружины и шарика.
    """

    def __init__(self, input_module):
        """
        Инициализация экземпляра класса.

        :param input_module: Экземпляр класса InputModule, предоставляющий параметры пружины.
        """
        self.input_module = input_module

    def show_animation(self):
        """
        Отображает анимацию вертикальных колебаний пружины и шарика на графике.
        """
        L, C, h = self.input_module.get_parameters()
        m = 0.1  # масса шарика (в кг)
        duration = 5.0  # продолжительность анимации (в секундах)
        fps = 30  # количество кадров в секунду

        t = np.linspace(0, duration, int(duration * fps))
        displacements = [self.vertical_oscillation(m, L, C, h, ti) for ti in t]

        fig, ax = plt.subplots()
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.set_aspect('equal')
        plt.axis('off')

        line, = ax.plot([], [], 'o-', lw=2)

        def animate(i):
            """
            Обновляет анимацию на каждом кадре.

            :param i: Индекс текущего кадра.
            :return: Обновленный графический объект.
            """
            x = 0
            y = displacements[i]
            spring_length = L + y
            line.set_data([x, x], [0.5, -spring_length])
            line.set_markeredgecolor('b')
            line.set_markersize(10)
            return line,

        anim = FuncAnimation(fig, animate, frames=len(t), interval=1000 / fps, blit=True)
        plt.show()

    def vertical_oscillation(self, m, L, C, h, t):
        """
        Рассчитывает вертикальное колебание шарика.

        :param m: Масса шарика (в кг).
        :param L: Длина недеформированной пружины (в м).
        :param C: Коэффициент упругости пружины (в Н/м).
        :param h: Смещение шарика вниз (в см).
        :param t: Время (в секундах).

        :return: Величина вертикального смещения шарика.
        """
        g = 9.8
        omega = math.sqrt(C / m)
        A = h / 100  # Переводим см в м
        phi = math.pi / 2
        displacement = A * math.cos(omega * t + phi)
        return displacement
