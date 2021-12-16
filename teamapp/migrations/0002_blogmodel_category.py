# Generated by Django 3.2.9 on 2021-12-15 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='category',
            field=models.CharField(choices=[('business', 'ビジネス'), ('life', '生活'), ('other', 'その他')], default='', max_length=50),
            preserve_default=False,
        ),
    ]
