# Generated by Django 3.2.7 on 2021-10-31 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Product_name', models.CharField(max_length=30)),
                ('Product_desc', models.CharField(max_length=300)),
                ('publish_date', models.DateField()),
                ('image', models.ImageField(default=' ', upload_to='shop/images')),
                ('price', models.IntegerField(default=0)),
                ('category', models.CharField(default=' ', max_length=50)),
            ],
        ),
    ]
