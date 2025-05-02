class AbiturientMag:
    abiturient_count = 0 

    def __init__(self, id, last_name, first_name, middle_name, address, phone, scores):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.address = address
        self.phone = phone
        self.scores = scores
        AbiturientMag.abiturient_count += 1

    @classmethod
    def create_multiple(cls, abiturient_data):
        return [cls(*data) for data in abiturient_data]

#Строковое представление объекта
    def __str__(self):
       return f"Абитуриент( {self.last_name}, {self.first_name}, {self.middle_name}, {self.address}, {self.phone}, {self.scores})"

#Проверяет на положительные числа при установке оценки
    def __setattr__(self, key, value):
        if key == 'scores':
            if not all(isinstance(score, (int, float)) and 0 <= score <= 10 for score in value):
                raise ValueError("Оценка должна быть в диапазоне от 0 до 10")
        super().__setattr__(key, value)

#Сравнивает абитуриентов по идентификатору
    def __eq__(self, other):
        if isinstance(other, AbiturientMag):
            return self.id == other.id
        return False

#Уменьшает счетчик абитуриентов при удалении объекта
    def __del__(self):
        AbiturientMag.abiturient_count -= 1

#Возвращает длину списка оценок
    def __len__(self):
        return len(self.scores)

data = [
    (1, "Иванов", "Иван", "Иванович", "г. Москва, ул. Первомайская, д. 1", "123-456-789", [8, 9, 7]),
    (2, "Петров", "Петр", "Петрович", "г. Санкт-Петербург, ул. Невский, д. 2", "987-654-321", [5, 5, 4]),
    (3, "Сидорова", "Анна", "Сидоровна", "г. Казань, ул. Кораблестроителей, д. 3", "456-123-789", [1, 6, 8])
]

abiturients = AbiturientMag.create_multiple(data)

#Вывод данных

print(abiturients[0])
print(abiturients[1])
print(abiturients[2])

print(abiturients[0] == abiturients[1]) # проверка по идентификатору

print(len(abiturients[0]))

del(abiturients[1])
print(f'Общее количество абитуриентов: {AbiturientMag.abiturient_count}')

