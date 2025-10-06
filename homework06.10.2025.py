# Завдання 1
# Програма складається з трьох потоків. Перший
# просить в користувача вводити числа, поки не введено
# порожній рядок, та зберігає числа в список.
# Інші два потоки чекають поки перший завершить
# роботу, і вже потім запускаються. Один рахує суму чисел в
# списку, інший рахує середнє арифметичне.
# Список чисел, сума та середнє виводяться на екран
import threading

def get_nums(nums: list):

    while True:
        user_nums = input('add nums or enter to finish work')
        if  user_nums != '':
            nums.append(int(user_nums))
        else:
            break

    return  nums


def get_avg(nums: list):
    avg = sum(nums) / len(nums)

    return  avg


def get_sum(nums: list):

    return  sum(nums)


def main():
    nums = []


    t1 = threading.Thread(target=get_nums, args=(nums,))
    t1.start()
    t1.join()


    t2 = threading.Thread(target=get_sum, args=(nums,))
    t3 = threading.Thread(target=get_avg, args=(nums,))
    t2.start()
    t3.start()
    t2.join()
    t3.join()
    print(f'Список чисел: {nums}')

