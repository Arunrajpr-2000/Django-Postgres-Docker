# Generated by Django 4.2.11 on 2024-03-30 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_closure_lead_id_alter_closure_project_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_to_cma', models.BooleanField(default=False)),
                ('lead_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.lead')),
                ('project_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_id', to='app.project')),
            ],
        ),
    ]
