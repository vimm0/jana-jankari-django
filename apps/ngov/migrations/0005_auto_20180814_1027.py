# Generated by Django 2.1 on 2018-08-14 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ngov', '0004_auto_20180814_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ngov.Department', verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='office',
            name='department_en',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ngov.Department', verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='office',
            name='department_ne',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ngov.Department', verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='office',
            name='ministry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ngov.Ministry', verbose_name='Ministry'),
        ),
        migrations.AlterField(
            model_name='office',
            name='ministry_en',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ngov.Ministry', verbose_name='Ministry'),
        ),
        migrations.AlterField(
            model_name='office',
            name='ministry_ne',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ngov.Ministry', verbose_name='Ministry'),
        ),
    ]
