# Generated by Django 4.1.2 on 2022-10-24 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_customer_store_custo_last_na_e6a359_idx_and_more'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO store_collection (title)
            VALUES ('collection1') 
        """, """
            DELETE FROM store_collection
            WHERE title='collection1'
        """)
    ]
