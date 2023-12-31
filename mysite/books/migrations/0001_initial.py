# Generated by Django 4.2.1 on 2023-06-04 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('title', models.CharField(verbose_name='Название')),
                ('author', models.CharField(verbose_name='Автор')),
                ('year_publication', models.DateField(verbose_name='Дата печати')),
                ('place_publication', models.CharField(verbose_name='Место Издания')),
                ('number_pages', models.BigIntegerField(verbose_name='Количество страниц')),
                ('price', models.BigIntegerField(verbose_name='Цена')),
                ('category', models.CharField(verbose_name='Категория')),
                ('type', models.CharField(verbose_name='Тип')),
                ('method_issue', models.CharField(verbose_name='Способ выдачи')),
                ('id_book', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='Issuance',
            fields=[
                ('id_issuance', models.BigIntegerField(primary_key=True, serialize=False)),
                ('id_book', models.BigIntegerField(verbose_name='Id книги')),
                ('id_person', models.BigIntegerField(verbose_name='Id читателя')),
                ('date', models.DateField(verbose_name='Дата выдачи')),
                ('status', models.CharField(verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Таблица Выдачи',
                'verbose_name_plural': 'Таблица Выдач',
                'db_table': 'issuance',
            },
        ),
        migrations.CreateModel(
            name='Readers',
            fields=[
                ('id_person', models.BigAutoField(primary_key=True, serialize=False)),
                ('surname', models.CharField(verbose_name='Фамилия')),
                ('name', models.CharField(verbose_name='Имя')),
                ('patronymic', models.CharField(verbose_name='Отчество')),
                ('passport_birth_certificate', models.CharField(verbose_name='Данные паспорта или свидетельства о рождении')),
                ('e_mail', models.CharField(verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Читатель',
                'verbose_name_plural': 'Читатели',
                'db_table': 'person',
            },
        ),
    ]
