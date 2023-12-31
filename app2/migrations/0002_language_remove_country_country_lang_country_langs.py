# Generated by Django 4.2.3 on 2023-07-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='country',
            name='country_lang',
        ),
        migrations.AddField(
            model_name='country',
            name='langs',
            field=models.ManyToManyField(to='app2.language'),
        ),
    ]
