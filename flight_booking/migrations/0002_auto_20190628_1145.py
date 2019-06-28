# Generated by Django 2.2.2 on 2019-06-28 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airplane',
            name='P_Capacity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='seatconf',
            name='rows',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='seatconf',
            name='seats_row',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='seatconf',
            name='start_row',
            field=models.IntegerField(),
        ),
    ]