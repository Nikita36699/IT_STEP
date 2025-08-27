# Завдання 1
# Напишіть клас Банківський рахунок з атрибутами:
#  ім'я клієнта
#  баланс
#  валюта
#  словник з курсом валют(однаковий для всіх)
# Додайте методи:
#  вивід загальної інформації
#  перевірка чи відома валюта(якщо ні, викликати
# ValueError)
#  перевести гроші з однієї валюти в іншу(ця операція
# часто використовується, тому зрочно реалізувати
# окремим методом)
#  зміна валюти
#  поповнення балансу(валюта та сама)
#  зняття грошей з балансу(валюта та сама).

class BankId:
    def __init__(self, client_name, currency):
        self.client_name = client_name
        self.currency = currency

        self.balance = 0
        self.exchange_rates = {
                "USD": 1.0,
                "EUR": 0.92,
                "UAH": 40.0,
                "GBP": 0.78,
                "PLN": 4.1
                            }
    def show_info(self):
        print("Данні вашого рахунку:")
        print(f'\t\t Доброго дня {self.client_name} ')
        print(f'\t\t на вашому рахунку - {self.balance} - {self.currency}')

    def check_currency(self, client_currency):
        if client_currency not in self.exchange_rates:
            raise ValueError("Наш банк не має такої валюти")

        print("Ваша валюта є")

    def convert_to(self,target_currency):
        self.check_currency(target_currency)

        amount_usd = self.balance / self.exchange_rates[self.currency]

        return  amount_usd * self.exchange_rates[target_currency]

    def change_currency(self,new_currency):
        new_balance = self.convert_to(new_currency)

        self.currency = new_currency
        self.balance =  new_balance

        print(f"Валюта змінена. Тепер у вас {self.balance:.2f} {self.currency}")

    def top_up_balance(self,client_sum,chosed_currency):
        self.check_currency(chosed_currency)
        self.change_currency(chosed_currency)

        self.balance += client_sum
        print(f'Ваш баланс поповнено на {client_sum},{chosed_currency}')
        print(f'на разі ваш баланс = {self.balance}')

    def cash_withdrawal(self,withdrawal,value):
        self.check_currency(value)
        self.change_currency(value)

        self.balance -= withdrawal


client1 = BankId('Nikita','USD')

client1.show_info()
client1.top_up_balance(100,"EUR")
client1.show_info()
client1.top_up_balance(100,"USD")
client1.show_info()