# Generated by Django 3.0.2 on 2020-01-24 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0006_classregistration_name'),
        ('student', '0029_auto_20200122_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='registration_no',
            field=models.IntegerField(default=489208, unique=True),
        ),
        migrations.AlterField(
            model_name='enrolledstudent',
            name='class_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.ClassRegistration'),
        ),
    ]
