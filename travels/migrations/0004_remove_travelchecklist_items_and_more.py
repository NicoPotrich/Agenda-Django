# Generated by Django 5.0.2 on 2024-03-24 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0003_rename_items_checklistitem_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travelchecklist',
            name='items',
        ),
        migrations.RemoveField(
            model_name='travelchecklist',
            name='travel',
        ),
        migrations.DeleteModel(
            name='ChecklistItem',
        ),
        migrations.DeleteModel(
            name='TravelChecklist',
        ),
    ]