# Generated by Django 3.0.14 on 2023-01-30 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newtasks', models.CharField(max_length=500)),
                ('post_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]