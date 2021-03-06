# Generated by Django 3.2.3 on 2021-06-05 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalancingGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='PowerPlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('balancing_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.balancinggroup')),
            ],
        ),
        migrations.CreateModel(
            name='Generator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('power_plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.powerplant')),
            ],
        ),
        migrations.AddField(
            model_name='balancinggroup',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='impressions', to='sample.company', verbose_name='書籍'),
        ),
    ]
