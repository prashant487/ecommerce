# Generated by Django 3.1.7 on 2021-03-01 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='image',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='items',
            name='label',
            field=models.CharField(choices=[('NEW', 'New Product'), ('hot', 'Hot Product'), ('sale', 'Sale Product')], default='new', max_length=60),
        ),
    ]
