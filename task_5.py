class TestCase:
    # Инициализация тест-кейса с пустым списком шагов и результатом
    def __init__(self):
        self.steps = {}
        self.result = None
    # Метод для вывода тест-кейса в консоль
    def set_step(self, step_number, step_tex):
        self.steps[step_number] = step_tex
    # Метод для удаления шага по его номеру
    def delete_step(self, step_number):
        self.steps.pop(step_number)
    # Метод для установки ожидаемого результата тест-кейса
    def set_result(self, result):
        self.result = result
    # Метод для вывода всех шагов и результата тест-кейса
    def get_test_case(self):
        test_case_info={
            'Шаги': self.steps,
            'Ожидаемый результат': self.result
        }
        print(test_case_info)

test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()