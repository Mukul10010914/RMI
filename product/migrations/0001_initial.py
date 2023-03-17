# Generated by Django 4.1.2 on 2022-12-12 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='pics')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('min_order', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=100)),
                ('filter_type', models.CharField(max_length=100)),
                ('usage', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('feature', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=1000)),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
    ]