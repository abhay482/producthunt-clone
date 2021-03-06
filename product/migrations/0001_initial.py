# Generated by Django 2.2.14 on 2020-07-10 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tital', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('votes_total', models.IntegerField(default=1)),
                ('icon', models.ImageField(upload_to='icon/')),
                ('image', models.ImageField(upload_to='images/')),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
