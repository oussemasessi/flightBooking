# Generated by Django 2.2.2 on 2019-07-23 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_Capacity', models.PositiveIntegerField()),
                ('P_type', models.CharField(choices=[('boeing', 'bg'), ('airbus', 'as'), ('jet', 'jt')], default='airbus', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('airplane_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_booking.Airplane')),
            ],
        ),
        migrations.CreateModel(
            name='SeatConf',
            fields=[
                ('seat_conf_id', models.AutoField(primary_key=True, serialize=False)),
                ('BC_rows', models.IntegerField()),
                ('BC_start_row', models.IntegerField()),
                ('BC_seats_row', models.IntegerField()),
                ('BC_base_price', models.IntegerField()),
                ('FC_rows', models.IntegerField()),
                ('FC_start_row', models.IntegerField()),
                ('FC_seats_row', models.IntegerField()),
                ('FC_base_price', models.IntegerField()),
                ('EC_rows', models.IntegerField()),
                ('EC_start_row', models.IntegerField()),
                ('EC_seats_row', models.IntegerField()),
                ('EC_base_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('PNR', models.IntegerField(primary_key=True, serialize=False)),
                ('row_number', models.IntegerField()),
                ('seat_number', models.IntegerField()),
                ('category', models.CharField(choices=[('First_Class', 'First_Class'), ('Business_Class', 'Business_Class'), ('Economic_Class', 'Economic_Class')], default='Economic_Class', max_length=14)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_booking.Flight')),
            ],
        ),
        migrations.AddField(
            model_name='airplane',
            name='seat_conf_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_booking.SeatConf'),
        ),
        migrations.CreateModel(
            name='BookedSeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_booking.Flight')),
                ('seat_PNR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_booking.Seat')),
            ],
            options={
                'unique_together': {('seat_PNR', 'flight')},
            },
        ),
    ]
