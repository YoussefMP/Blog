# Generated by Django 4.1.7 on 2023-04-08 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OJ_Blog', '0006_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='OJ_Blog.tag'),
        ),
    ]