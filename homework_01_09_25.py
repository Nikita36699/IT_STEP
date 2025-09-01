# Завдання 1
# Створіть наступні класи:
#  CreditCardPayment – атрибути currency
#  PayPalPayment – атрибути currency
#  CryptoPayment – атрибути currency
# Методи:
#  pay(amount) – виводить повідомлення
# o CreditCardPayment – оплата карткою {amount}{currency}
# o PayPalPayment – оплата PayPal {amount}{currency}
# o CryptoPayment – оплата криптогаманцем {amount}{currency}
# Напишіть функцію create_payment() яка запитує у
# користувача тип рахунку та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька рахунків, добавте їх у список та для
# кожної викличте відповідні методи.
import typing

class CreditCardPayment:
    def __init__(self,currency):
        self.currency = currency

    def pay(self,amount):
        print(f'оплата карткою {amount}--{self.currency}')


class PayPalPayment:
    def __init__(self,currency):
        self.currency = currency

    def pay(self, amount):
        print(f'оплата PayPal {amount}--{self.currency}')

class CryptoPayment:
    def __init__(self,currency):
        self.currency = currency

    def pay(self, amount):
        print(f'оплата криптогаманцем {amount}--{self.currency}')

def create_payment():
    user_choice = int(input('оберіть спосіб оплати де: \n\t\t1(КАРТА) \n\t\t2(PAYPAL) \n\t\t3(CRYPTO)  '))
    if user_choice not in (1, 2, 3):
        print(" Невірний вибір способу оплати")
        return


    currency = input("Оберіть валюту у якій хочете здійснити оплату - ").strip().upper()
    if len(currency) < 2 or not currency.isalpha():
        print('помилка - введіть валюту корректно')
        return

    if user_choice == 1:

        credit_card = CreditCardPayment(currency)

        return credit_card

    if user_choice == 2:

        paypal = PayPalPayment(currency)

        return paypal

    if user_choice == 3:

            crypto_pay = CryptoPayment(currency)

            return crypto_pay

pays_ways:typing.List[CreditCardPayment | PayPalPayment | CryptoPayment ] = []

for _ in range(3):
    pay = create_payment()
    if pay is not None:
        pays_ways.append(pay)

for pay in pays_ways:
    amount = int(input('введіть сумму для оплати '))
    pay.pay(amount)
