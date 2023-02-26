from djmoney.models.fields import MoneyField
from djmoney.models.fields import Money
from django.db import models

# Create your models here.
class Receipt(models.Model): 
    # модель - ПОСТУПЛЕНИЯ (денежные поступления на счет компании)
  
    name = models.CharField('Name', max_length=150) # example: ИП Пирогов, оплата -> название поступления
    senders = models.CharField('Sender', max_length=300) # example: ИП Пирогов -> отправитель (от кого)
    purpose = models.CharField('Purpose', max_length=150) # example: Оплата по договору -> назначение поступления
    bank = models.CharField('Bank', max_length=150) # example: СберБанк -> наименование банка, который перевел средства
    money = MoneyField('Money', max_digits=14, decimal_places=2, default=Money("0", "USD")) # example: 50.000$ -> кол-во денег 
    date = models.DateField('Date') # example: 17.02.2023 -> дата поступления
    
    def __str__(self):
        return f'{self.name}, {self.senders}, {self.money}, {self.date}'
    
    class Meta: 
        verbose_name = 'Receipt'
        verbose_name_plural = 'Receipts'

class Debit(models.Model): 
    # модель - СПИСАНИЯ (денежные списания со счета компании)

    STATUS_DEBIT = [
        ('1', 'Expectation'), # ожидание
        ('2', 'Successfully completed'), # успешно выполнено
        ('3', 'Error Debit') # ошибка списания
    ]

    name = models.CharField('Name', max_length=150) # example: Оплата счета за электроэнергию -> название списания
    name_debit = models.CharField('Name Debit', max_length=300) # example: Электросети -> название орг., на чей счет произошло списание 
    purpose = models.CharField('Purpose', max_length=150) # example: Оплата счета за электроэнергию -> назначение списания
    bank = models.CharField('Bank', max_length=150) # example: СберБанк -> наименование банка, благодаря которому произведена операция
    money = MoneyField('Money', max_digits=14, decimal_places=2, default=Money("0", "USD")) # example: 50.000$ -> кол-во денег 
    date = models.DateField('Date') # example: 17.02.2023 -> дата заявки на списание
    status = models.CharField('Status', max_length=50, choices=STATUS_DEBIT, default=1) # example: Expectation -> статус списания

    def __str__(self):
        return f'{self.name}, {self.name_debit} ,{self.money}, {self.date}, {self.status}'
    
    class Meta: 
        verbose_name = 'Debit'
        verbose_name_plural = 'Debits'