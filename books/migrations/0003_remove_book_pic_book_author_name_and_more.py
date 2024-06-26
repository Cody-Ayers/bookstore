# Generated by Django 4.2.11 on 2024-05-16 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='pic',
        ),
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='No Name', max_length=120),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_type',
            field=models.CharField(choices=[('hc', 'Hard cover'), ('eb', 'E-Book'), ('ab', 'Audiobook')], default='hc', max_length=12),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('cl', 'Classic'), ('ro', 'Romantic'), ('co', 'Comic'), ('fa', 'Fantasy'), ('ho', 'Horror'), ('ed', 'Educational')], default='cl', max_length=12),
        ),
    ]
