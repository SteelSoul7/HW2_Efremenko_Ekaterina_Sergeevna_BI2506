При тестировании исключительных случаев с valueError я столкнулась со сложностью загрузки pytest. Однако проявила инициативу реализовать эту красоту через unittest, пример его использования был найден мною в яндексе, а именно реализация assertRaises.
Для подтверждения своих слов приложу скопированный блок от Алиса AI (в задании было сказано, что для подобных целей нейросети использовать можно). Прошу не снижать оценку за неиспользование именно pytest, так как необходимые валидные случаи мною покрыты. 


import unittest [1](https://codevisionz.com/lessons/python-unittest-module-and-exceptions/)

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b [1](https://codevisionz.com/lessons/python-unittest-module-and-exceptions/)

class TestDivideFunction(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0) [1](https://codevisionz.com/lessons/python-unittest-module-and-exceptions/)

if __name__ == '__main__':
    unittest.main()
``` [1](https://codevisionz.com/lessons/python-unittest-module-and-exceptions/)

В этом примере функция divide должна вызывать ValueError, когда второй аргумент (b) равен нулю. Метод test_divide_by_zero проверяет этот случай с помощью assertRaises. [1](https://codevisionz.com/lessons/python-unittest-module-and-exceptions/)

**Также в unittest есть метод assertRaisesRegex**, который позволяет проверить, что исключение содержит определённый текст в сообщении. [4](https://sky.pro/wiki/media/testirovanie-na-isklyucheniya-v-python/)


Благодарю, что прочитали этот раздел. Да и в целом спасибо за вашу работу)
