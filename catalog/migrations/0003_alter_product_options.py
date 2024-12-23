from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_product_options_product_owner_product_status"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name"],
                "permissions": [
                    ("can_unpublish_product", "can unpublish product"),
                    ("can_delete_product", "can delete product"),
                ],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
    ]
