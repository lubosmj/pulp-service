# Generated by Django 4.2.11 on 2024-08-23 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0120_get_url_removal'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='domainorg',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='domainorg',
            name='group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='core.group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='domainorg',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='domainorg',
            name='org_id',
            field=models.CharField(db_index=True, null=True),
        ),
    ]