# Generated by Django 3.0.2 on 2020-01-02 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='uid',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]