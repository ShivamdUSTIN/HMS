# Generated by Django 5.0.13 on 2025-06-05 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_remove_appointment_patient_appointment_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('generic_name', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(choices=[('tablet', 'Tablet'), ('capsule', 'Capsule'), ('syrup', 'Syrup'), ('injection', 'Injection'), ('ointment', 'Ointment'), ('drops', 'Drops'), ('inhaler', 'Inhaler'), ('other', 'Other')], max_length=20)),
                ('manufacturer', models.CharField(max_length=100)),
                ('batch_number', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('manufacturing_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Medicine',
                'verbose_name_plural': 'Medicines',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='hospital.doctor'),
        ),
    ]
