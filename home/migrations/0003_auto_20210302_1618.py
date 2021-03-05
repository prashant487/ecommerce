# Generated by Django 3.1.7 on 2021-03-02 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210302_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='label',
            field=models.CharField(choices=[('new', 'New Product'), ('hot', 'Hot Product'), ('sale', 'Sale Product')], default='new', max_length=60),
        ),
    ]