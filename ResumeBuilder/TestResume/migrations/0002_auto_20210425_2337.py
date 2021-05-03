# Generated by Django 3.1.7 on 2021-04-26 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestResume', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='Education',
            new_name='HSC',
        ),
        migrations.AddField(
            model_name='resume',
            name='PG',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='SSC',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='UG',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resume',
            name='Address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='resume',
            name='Certificates',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='resume',
            name='Experience',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='resume',
            name='Languages',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='resume',
            name='Projects',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='resume',
            name='Skills',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='resume',
            name='Summary',
            field=models.TextField(),
        ),
    ]