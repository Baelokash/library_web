from django.db import models

class Books(models.Model):
    title= models.CharField('Название')
    author = models.CharField('Автор')
    year_publication = models.DateField('Дата печати')
    place_publication = models.CharField('Место Издания')
    number_pages = models.BigIntegerField('Количество страниц')
    price = models.BigIntegerField('Цена')
    category = models.CharField('Категория')
    type = models.CharField('Тип')
    method_issue = models.CharField('Способ выдачи')
    id_book = models.BigAutoField( primary_key=True)

    def __str__(self):
        #price = str(self.price) + ' р.'
        #out= [self.title , self.author , price]
        return self.title
    
    class Meta:
        db_table='books'
        verbose_name="Книга"
        verbose_name_plural='Книги'

class Readers(models.Model):
    id_person = models.BigAutoField( primary_key=True)
    surname= models.CharField('Фамилия')
    name = models.CharField('Имя')
    patronymic = models.CharField('Отчество')
    passport_birth_certificate = models.CharField('Данные паспорта или свидетельства о рождении')
    e_mail = models.CharField('E-mail')

    def __str__(self):
        out= self.surname + ' ' + self.name
        return self.surname
    
    class Meta:
        db_table='person'
        verbose_name="Читатель"
        verbose_name_plural='Читатели'


class Issuance(models.Model):
    id_issuance = models.BigAutoField( primary_key=True)
    id_book= models.BigIntegerField('Id книги')
    id_person = models.BigIntegerField('Id читателя')
    date = models.DateField('Дата выдачи')
    status = models.CharField('Статус')

    def __str__(self):
        return self.status
    
    class Meta:
        db_table='issuance'
        verbose_name="Таблица Выдачи"
        verbose_name_plural='Таблица Выдач' 


class Notice(models.Model):
    id_notice = models.BigAutoField( primary_key=True)
    fio= models.CharField('Фамилия')
    count_books = models.BigIntegerField('Количство подлежащих возврату книг')
    e_mail = models.CharField('E-mail')
    refund_period = models.DateField('Крайняя дата возврата')
    text_in = models.CharField('Сообщение')

    def __str__(self):
        return self.id_notice
    
    class Meta:
        db_table='notice'
        verbose_name="Таблица Должников"
        verbose_name_plural='Таблица Должников'
            