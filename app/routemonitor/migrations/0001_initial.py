# Generated by Django 3.2.11 on 2022-02-13 10:39

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Gebruik een duidelijke naam. Bijvoorbeeld: Regelscenario wedstrijd Ajax', max_length=50, unique=True)),
                ('iv_project', models.CharField(help_text='Gebruik de Iv projectcode, bijvoorbeeld INFR191089.', max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('description', models.TextField(blank=True, help_text='Eventuele aanvullende opmerkingen')),
                ('routeType', models.CharField(choices=[('fastest', 'fastest'), ('shortest', 'shortest'), ('eco', 'eco'), ('thrilling', 'thrilling')], default='fastest', help_text="Leave this at 'fastest' unless you know what you are doing.", max_length=10)),
                ('travelMode', models.CharField(choices=[('car', 'car'), ('truck', 'truck'), ('taxi', 'taxi'), ('bus', 'bus'), ('motorcycle', 'motorcycle'), ('bicycle', 'bicycle'), ('pedestrian', 'pedestrian')], default='car', help_text='The mode of travel for the requested route.', max_length=20)),
                ('traffic', models.BooleanField(default=True, help_text='Determines whether current traffic is used in route calculations')),
                ('avoid', models.CharField(default='unpavedRoads', editable=False, max_length=50)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collections', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Gebruik een duidelijke naam. Bijvoorbeeld: Omleidingsroute via A58-A2', max_length=50, unique=True)),
                ('points', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
                ('description', models.TextField(blank=True, help_text='Eventuele aanvullende opmerkingen')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route', to='routemonitor.project')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Gebruik een duidelijke naam. Bijvoorbeeld: Zaterdag overdag', max_length=50)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='routemonitor.project')),
            ],
        ),
        migrations.CreateModel(
            name='RouteData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('travel_time', models.DecimalField(decimal_places=2, max_digits=9)),
                ('route_length', models.DecimalField(decimal_places=2, max_digits=9)),
                ('delay', models.DecimalField(decimal_places=2, max_digits=9)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='routemonitor.route')),
            ],
            options={
                'verbose_name': 'Route data',
                'verbose_name_plural': 'Route data',
                'get_latest_by': 'timestamp',
            },
        ),
    ]
