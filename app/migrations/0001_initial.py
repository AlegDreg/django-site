
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Title_info",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("description", models.TextField()),
                ("tags", models.TextField()),
                ("ru_name", models.TextField()),
                ("en_name", models.TextField()),
                ("alt_name", models.TextField()),
            ],
            options={
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Title",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("description", models.TextField()),
                ("ru_name", models.TextField(max_length=100)),
                ("en_name", models.TextField(max_length=100)),
                ("alt_name", models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Volume",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.TextField(max_length=200)),
                ("price", models.IntegerField()),
                ("title_number", models.IntegerField()),
                (
                    "title",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="app.title"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Title_tag",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="app.tag"
                    ),
                ),
                (
                    "title",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="app.title"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Chapter",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("content", models.TextField()),
                ("chapter_number", models.IntegerField()),
                ("likes", models.IntegerField()),
                ("views", models.IntegerField()),
                (
                    "volume",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="app.volume"
                    ),
                ),
            ],
        )
    ]