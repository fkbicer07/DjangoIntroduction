# Generated by Django 4.1 on 2022-09-30 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("learning", "0004_book_intro"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProxyBook",
            fields=[],
            options={
                "ordering": ["name"],
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("learning.book",),
        ),
    ]
