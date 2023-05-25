# Generated by Django 4.0.3 on 2023-04-11 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hosting', '0002_hostingtemplate_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('waiting', 'waiting'), ('completed', 'completed'), ('canceled', 'canceled')], default='waiting', max_length=50)),
                ('payment', models.CharField(max_length=150)),
                ('check_id', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.IntegerField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
