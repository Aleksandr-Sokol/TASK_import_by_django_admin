# Generated by Django 4.0.2 on 2022-02-06 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('import_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('date_upload', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zmk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name_plural': 'Zmk',
            },
        ),
        migrations.AlterModelOptions(
            name='registry',
            options={'verbose_name_plural': 'RTS'},
        ),
        migrations.RemoveField(
            model_name='registry',
            name='name',
        ),
        migrations.AddField(
            model_name='registry',
            name='departure_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registry',
            name='num',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='registry',
            name='receiving_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registry',
            name='weight',
            field=models.FloatField(default=0.0),
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=120)),
                ('zmk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='object', to='import_data.zmk')),
            ],
        ),
        migrations.AddField(
            model_name='registry',
            name='object',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rts', to='import_data.object'),
        ),
        migrations.AddField(
            model_name='registry',
            name='zmk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rts', to='import_data.zmk'),
        ),
    ]
