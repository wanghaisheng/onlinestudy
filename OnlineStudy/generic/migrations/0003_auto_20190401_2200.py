# Generated by Django 2.1.1 on 2019-04-01 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0002_auto_20190401_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courselesson',
            name='course_lesson_type',
            field=models.SmallIntegerField(choices=[(0, '视频'), (1, '文档'), (2, '练习题')], default=0, verbose_name='课时类型'),
        ),
    ]