class Abiturient:
    abiturient_count = 0 #статическое поле

    def __init__(self, id, last_name, first_name, middle_name, address, phone, scores):
        self.id = id #динамические поля
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.address = address
        self.phone = phone
        self.scores = scores
        Abiturient.abiturient_count += 1

    def display_info(self): #метод объекта
        return "Абитуриент: "+ str(self.first_name) + " " + str(self.last_name) + ", проживающий по адресу: " + str(self.address) + ", телефон: " + str(self.phone) + " с оценками: " + str(self.scores)

    @staticmethod #статистический метод
    def get_abiturient_count():
        return f"Общее количество абитуриентов: {Abiturient.abiturient_count}"

    @classmethod
    def create_abiturient(cls, id, last_name, first_name, middle_name, address, phone, scores):
        return cls(id, last_name, first_name, middle_name, address, phone, scores)

    def set_score(self, score): #сеттер инкапсулированного поля
        if score > 0:
            self.__scores = score
        else:
            raise ValueError("Оценка должна быть положительной")

    def get_score(self): #геттер инкапсулированного поля
        return self.__scores

# Вывод списка абитуриентов, имеющих неудовлетворительные оценки

    def bad_marks(self):
        return any(score <= 3 for score in self.scores)

    @staticmethod
    def abiturients_with_bad_marks(abiturients):
        unsatisfactory = [abiturient.last_name for abiturient in abiturients if abiturient.bad_marks()]
        return unsatisfactory

#Вывод списка абитуриентов, у которых сумма баллов выше заданной

    def total_score(self):
        return sum(self.scores)

    @staticmethod
    def abiturients_above_threshold(abiturients, threshold):
        return [abiturient for abiturient in abiturients if abiturient.total_score() >= threshold]

#Создание списка объектов
if __name__ == "__main__":
    abiturients = [
        Abiturient(1, "Пупкин", "Василий", "Илларионович", "ул. Солнечная, д. 1", "+3751111111",[4, 5, 3, 4]),
        Abiturient(2, "Ложкин", "Иван", "Филлиопович", "ул. Веселкина, д. 1", "+3755555111", [5, 5, 5, 5]),
        Abiturient(3, "Селедкина", "Евгения", "Поликарповна", "ул. Простоквашина, д. 1", "+3758888111", [2, 3, 3, 4])
    ]

    threshold = 15 #пороговое значение

    filtered_abiturients = Abiturient.abiturients_above_threshold(abiturients, threshold)
    print ("\nCписок абитуриентов, у которых сумма баллов выше заданной: ")
    for abiturient in filtered_abiturients:
        print(f"{abiturient.first_name} {abiturient.last_name}: {abiturient.total_score()}")

    unsatisfactory_abiturients = Abiturient.abiturients_with_bad_marks(abiturients)
    print("\nАбитуриенты с неудовлетворительными оценками:", unsatisfactory_abiturients)


