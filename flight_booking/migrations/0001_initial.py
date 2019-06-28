# Generated by Django 2.2.2 on 2019-06-27 19:56

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
                ('P_type', models.CharField(choices=[('boeing', 'bg'), ('airbus', 'as'), ('jet', 'jt')], default='airbus', max_length=6)),
                ('P_Capacity', models.PositiveIntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SeatConf',
            fields=[
                ('seat_conf_id', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('FC', 'FC'), ('BC', 'BC'), ('EC', 'EC')], default='EC', max_length=2)),
                ('rows', models.IntegerField(max_length=100)),
                ('start_row', models.IntegerField(max_length=100)),
                ('seats_row', models.IntegerField(max_length=10)),
                ('EC_base_price', models.IntegerField()),
                ('BC_base_price', models.IntegerField()),
                ('FC_base_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('FC', 'FC'), ('BC', 'BC'), ('EC', 'EC')], default='EC', max_length=2)),
                ('plane_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_booking.Airplane')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('seat_PNR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_booking.Seat')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='airplane',
            name='seat_conf_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_booking.SeatConf'),
        ),
    ]
