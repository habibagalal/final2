# Generated by Django 4.0.2 on 2022-05-11 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(default='', upload_to='photos/%y/%m/%d')),
                ('active', models.BooleanField(default=True)),
                ('condition', models.TextField(default='describe your house ')),
                ('floors', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('view', models.TextField(default='describe your house')),
                ('lat', models.IntegerField()),
                ('SQFT_Living', models.IntegerField()),
                ('SQFT_above', models.IntegerField()),
                ('SQFT_basement', models.IntegerField()),
                ('SQFT_lot15', models.IntegerField()),
                ('SQFT_living15', models.IntegerField()),
                ('yr_renovated', models.IntegerField()),
                ('zip_code', models.IntegerField()),
            ],
        ),
    ]