# Generated by Django 5.0.2 on 2024-04-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_remove_portfolio_subject_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfolio",
            name="field",
            field=models.IntegerField(choices=[(1, "기업홍보"), (2, "제품홍보"), (3, "브이로그")]),
        ),
        migrations.AlterField(
            model_name="portfolio",
            name="number",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
