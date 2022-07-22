# Generated by Django 2.2.24 on 2022-07-19 16:26

from django.db import migrations

def fill_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all().iterator():
        Owner.objects.get_or_create(
            name=flat.owner,
            phonenumber=flat.owners_phonenumber,
            defaults={
                'name': flat.owner,
                'phonenumber': flat.owners_phonenumber,
                'pure_phone': flat.owner_pure_phone,
            })

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20220719_2115'),
    ]

    operations = [
        migrations.RunPython(fill_owner),
    ]
