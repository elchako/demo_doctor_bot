# Generated by Django 4.1.3 on 2022-11-18 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='photo',
            field=models.ImageField(default=12, upload_to='photo/', verbose_name='Фото врача'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctors',
            name='special',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='records.specials', verbose_name='Специальность'),
        ),
        migrations.AlterField(
            model_name='records',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='records.doctors', verbose_name='Врач'),
        ),
        migrations.AlterField(
            model_name='records',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='records.clients', verbose_name='Клиент'),
        ),
    ]
