# Generated by Django 4.0.2 on 2022-02-17 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0002_alter_supertypes_type'),
        ('supers', '0002_super_alter_ego_super_catchphrase_super_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='super',
            name='super_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='super_types.supertypes'),
        ),
    ]
