# Generated by Django 2.2 on 2020-04-29 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=225)),
                ('email', models.CharField(max_length=225)),
                ('contact_message', models.TextField()),
                ('creations_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
