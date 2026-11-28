from django.apps.registry import Apps
from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor

SEGMENT_ID = "members.with_home_delivery_this_week"
CITY_COLUMN_ID = "member_delivery_city"
DROP_OFF_LOCATION_COLUMN_ID = "member_delivery_drop_off_location"
DROP_OFF_LOCATION_COLUMN_NAME = "Alternativer Ablageort"


def add_drop_off_location_column(apps: Apps, schema_editor: BaseDatabaseSchemaEditor):
    CsvExport = apps.get_model("generic_exports", "CsvExport")
    for export in CsvExport.objects.filter(export_segment_id=SEGMENT_ID):
        if DROP_OFF_LOCATION_COLUMN_ID in export.column_ids:
            continue

        index = (
            export.column_ids.index(CITY_COLUMN_ID) + 1
            if CITY_COLUMN_ID in export.column_ids
            else len(export.column_ids)
        )
        export.column_ids.insert(index, DROP_OFF_LOCATION_COLUMN_ID)
        export.custom_column_names.insert(index, DROP_OFF_LOCATION_COLUMN_NAME)
        export.save(update_fields=["column_ids", "custom_column_names"])


class Migration(migrations.Migration):

    dependencies = [
        ("generic_exports", "0014_normalise_email_addresses"),
    ]

    operations = [
        migrations.RunPython(add_drop_off_location_column, migrations.RunPython.noop),
    ]
