# Generated by Django 2.0.3 on 2018-07-15 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook_news_scraper', '0010_article_total_reactions'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
