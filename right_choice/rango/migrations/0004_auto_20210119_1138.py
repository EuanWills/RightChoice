# Generated by Django 2.1.5 on 2021-01-19 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_remove_course_apprenticeship_subreqname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apprenticeship',
            name='companyImage',
            field=models.ImageField(default='company.jpg', upload_to='company_images/'),
        ),
    ]
