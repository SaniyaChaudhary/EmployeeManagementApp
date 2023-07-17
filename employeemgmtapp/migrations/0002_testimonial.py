# Generated by Django 4.2.3 on 2023-07-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeemgmtapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('testimonial', models.TextField()),
                ('picture', models.ImageField(upload_to='testimonials/')),
                ('rating', models.IntegerField(max_length=1)),
            ],
        ),
    ]