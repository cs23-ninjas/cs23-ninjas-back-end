# Generated by Django 2.2.7 on 2019-11-21 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0003_auto_20191120_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interactable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='DEFAULT INTERACTABLE', max_length=50)),
                ('description', models.CharField(default='DEFAULT DESCRIPTION', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='DEFAULT ITEM', max_length=50)),
                ('description', models.CharField(default='DEFAULT DESCRIPTION', max_length=500)),
                ('item_type', models.CharField(default='DEFAULT TYPE', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='DEFAULT TITLE', max_length=50)),
                ('description', models.CharField(default='DEFAULT DESCRIPTION', max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='description_b',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.CreateModel(
            name='RoomItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
                ('last_taken', models.DateTimeField(null=True)),
                ('respawn', models.DurationField(null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.Item')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.Room')),
            ],
        ),
        migrations.CreateModel(
            name='RoomInteractable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='DEFAULT STATUS', max_length=50)),
                ('interactable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.Interactable')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.Room')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerVisited',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.Player')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.Room')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.Item')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adventure.Player')),
            ],
        ),
    ]
