import math # для использования функции sqrt

class Triangle:
    """Класс треугольника"""
    __counter = 0 # счетчик созданных треугольников
    def __init__(self, side1, side2, side3):
        """Создание нового треугольника с длинами сторон side1, side2, side3"""
        self._side1 = side1 # устанавливаем значения сторон
        self._side2 = side2
        self._side3 = side3
        self.angle1 = self.calculate_angle(self.side1, self.side2, self.side3) # вычисляем углы
        self.angle2 = self.calculate_angle(self.side2, self.side1, self.side3) 
        self.angle3 = 180 - self.angle1 - self.angle2 
        Triangle.__counter += 1 # увеличиваем счетчик

    def __del__(self):
            """Разбираем функция"""
            Triangle.__counter -= 1 # уменьшаем счетчик
    
    @classmethod
    def get_instance_count(cls): 
        """Возвращает количество созданных экземпляров треугольника"""
        return cls.__counter # возвращаем значение

    def __str__(self): 
        """Отображение в виде строки"""
        return f"Triangle({self.side1}, {self.side2}, {self.side3})" # возвращаем строку

    def __repr__(self):
        """Представление данных"""
        return f"Triangle(side1={self.side1} side2={self.side2} side3={self.side3})" # возвращаем строку

    @property # декоратор для доступа к полю
    def side1(self): 
        """Доступ к полю side1"""
        #print("Задействован аргумент side1") # выводим сообщение
        return self._side1 # возвращаем значение

    @side1.setter # декоратор для установки значения
    def side1(self, value):
        """Устанавливает значение side1 и обновляет углы треугольника"""
        #print("Изменён аргумент side1") # выводим сообщение
        self._side1 = value # устанавливаем значение
        self.angle1 = self.calculate_angle(self._side1, self._side2, self._side3) # вычисляем углы
        self.angle3 = 180 - self.angle1 - self.angle2 # обновляем углы

    @property # декоратор для доступа к полю
    def side2(self):
        """Доступ к полю side2"""
        #print("Задействован аргумент side2") # выводим сообщение
        return self._side2 # возвращаем значение

    @side2.setter # декоратор для установки значения
    def side2(self, value):
        """Устанавливает значение side2 и обновляет углы треугольника"""
        #print("Изменён аргумент side2") # выводим сообщение
        self._side2 = value # устанавливаем значение
        self.angle2 = self.calculate_angle(self._side2, self._side1, self._side3) # вычисляем углы
        self.angle3 = 180 - self.angle1 - self.angle2 # обновляем углы 

    @property # декоратор для доступа к полю
    def side3(self):
        """Доступ к полю side3"""
        #print("Задействован аргумент side3") # выводим сообщение
        return self._side3 # возвращаем значение

    @side3.setter # декоратор для установки значения
    def side3(self, value):
        """Устанавливает значение side3 и обновляет углы треугольника"""
        #print("Изменён аргумент side3") # выводим сообщение
        self._side3 = value # устанавливаем значение
        self.angle3 = 180 - self.angle1 - self.angle2 # обновляем углы

    def calculate_angle(self, side1, side2, side3): 
        """Вычисление угла треугольника по трем сторонам"""
        return math.degrees(math.acos((side1**2 + side2**2 - side3**2) / (2 * side1 * side2))) # вычисляем углы

    def calculate_area(self):
        """Вычисление площади треугольника"""
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3)) # вычисляем площадь

    def calculate_perimeter(self):
        """Вычисление периметра треугольника"""
        return self.side1 + self.side2 + self.side3 # вычисляем периметр

    def calculate_heights(self):
        """Вычисление высот треугольника"""
        area = self.calculate_area()
        height1 = 2 * area / self.side1 # вычисляем высоты
        height2 = 2 * area / self.side2
        height3 = 2 * area / self.side3
        return height1, height2, height3

    def determine_triangle_type(self):
        """Определение типа треугольника (равносторонний, равнобедренный, прямоугольный или обычный)"""
        if self.side1 == self.side2 == self.side3: # если все стороны равны
            return "Равносторонний треугольник"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3: # если стороны равны
            return "Равнобедренный треугольник"
        elif (
            self.side1**2 + self.side2**2 == self.side3**2  # если стороны равны квадрату
            or self.side1**2 + self.side3**2 == self.side2**2 
            or self.side2**2 + self.side3**2 == self.side1**2 
        ):
            return "Прямоугольный треугольник"
        else:
            return "Обычный треугольник"
