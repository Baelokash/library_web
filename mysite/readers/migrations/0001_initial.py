# Generated by Django 4.2.1 on 2023-06-04 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
