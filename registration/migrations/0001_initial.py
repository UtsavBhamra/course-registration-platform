# Generated by Django 5.1.1 on 2024-10-04 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('schedule', models.CharField(max_length=50)),
                ('credits', models.IntegerField()),
                ('accepted_students', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='accepted_students', to='accounts.student')),
                ('instructors', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='accounts.faculty')),
                ('requested_students', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='requested_students', to='accounts.student')),
            ],
        ),
    ]
