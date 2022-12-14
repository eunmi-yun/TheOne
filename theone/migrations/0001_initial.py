# Generated by Django 4.0.3 on 2022-10-20 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dobonggu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Dongdaemungu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Dongjakgu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Eunpyeonggu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Gangbukgu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Gangdonggu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Gangnamgu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Gangseogu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Geumcheongu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Gurogu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Gwanakgu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Gwangjingu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Jongnogu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Junggu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Jungnanggu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Mapogu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Nowongu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Seochogu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Seodaemungu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Seongbukgu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Seongdonggu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Songpagu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Yangcheongu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Yeongdeungpogu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Yongsangu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_Date', models.DateTimeField()),
            ],
        ),
    ]
