# Generated by Django 2.1.7 on 2019-03-15 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=20)),
                ('book_pmail', models.EmailField(max_length=254)),
                ('book_isbn10', models.IntegerField()),
                ('book_author', models.CharField(max_length=20)),
                ('book_publisher', models.CharField(max_length=20)),
                ('book_copies', models.IntegerField()),
                ('book_price', models.IntegerField()),
                ('book_description', models.TextField()),
                ('book_lang', models.CharField(max_length=20)),
                ('book_year', models.IntegerField()),
                ('book_image', models.ImageField(blank=True, upload_to='')),
                ('book_genre', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate_name', models.CharField(max_length=20)),
                ('cate_img', models.ImageField(upload_to='images/genre/')),
            ],
        ),
        migrations.CreateModel(
            name='Ureg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ufname', models.CharField(max_length=20)),
                ('usname', models.CharField(max_length=20)),
                ('uname', models.CharField(max_length=20)),
                ('umail', models.EmailField(max_length=254)),
                ('upass', models.CharField(max_length=20)),
                ('uphone', models.CharField(max_length=10)),
                ('uaddr', models.TextField()),
                ('ucard', models.CharField(max_length=12)),
                ('utype', models.CharField(default='provider', max_length=10)),
            ],
        ),
    ]
