# Generated by Django 4.2.6 on 2023-10-30 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editor',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Editores'},
        ),
        migrations.AlterModelOptions(
            name='libro',
            options={'ordering': ['titulo'], 'verbose_name_plural': 'Libros'},
        ),
        migrations.RenameField(
            model_name='libro',
            old_name='autor',
            new_name='autores',
        ),
    ]
