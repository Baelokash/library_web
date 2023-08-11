"""from django.db import models

class Readers(models.Model):
    id_person = models.BigAutoField( primary_key=True)
    surname= models.CharField('Фамилия')
    name = models.CharField('Имя')
    patronymic = models.CharField('Отчество')
    passport_birth_certificate = models.CharField('Данные паспорта или свидетельства о рождении')
    e_mail = models.CharField('E-mail')

    def __str__(self):
        return self.surname
    
    class Meta:
        db_table='person'
        verbose_name="Читатель"
        verbose_name_plural='Читатели'


class Issuance(models.Model):
    id_issuance = models.BigIntegerField( primary_key=True)
    id_book= models.BigIntegerField('Id книги')
    id_person = models.BigIntegerField('Id читателя')
    date = models.DateField('Дата выдачи')
    status = models.CharField('Статус')
    
    class Meta:
        db_table='issuance'
        verbose_name="Таблица Выдачи"
        verbose_name_plural='Таблица Выдач'        
        """
