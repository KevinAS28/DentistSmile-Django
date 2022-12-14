# Generated by Django 4.0.3 on 2022-10-14 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('token_authentication', '0002_alter_userauthentication_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_file', models.CharField(max_length=50)),
                ('article_cover_file', models.CharField(default='', max_length=50)),
                ('title', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('article_type', models.CharField(max_length=20)),
                ('article_sub_type', models.CharField(default='', max_length=20)),
                ('article_tags', models.CharField(default='', max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='FunStuntQA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_file', models.CharField(max_length=50)),
                ('answers_file', models.CharField(max_length=50)),
                ('level', models.IntegerField()),
                ('correct_answer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GeneralConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StuntPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_lat', models.FloatField()),
                ('location_lng', models.FloatField()),
                ('place_name', models.CharField(max_length=50)),
                ('gmap_place_id', models.CharField(max_length=50)),
                ('img_url', models.CharField(default='', max_length=150)),
                ('phone', models.CharField(default='', max_length=15)),
                ('desc', models.CharField(default='', max_length=100)),
                ('avg_rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('profile_file', models.CharField(max_length=40)),
                ('authentication', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='token_authentication.userauthentication')),
            ],
        ),
        migrations.CreateModel(
            name='StuntReminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clock', models.TimeField()),
                ('repeat_each', models.TextField(max_length=50)),
                ('on', models.BooleanField(default=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apiv1.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='StuntPlaceReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('desc', models.CharField(max_length=200)),
                ('stunt_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apiv1.stuntplace')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apiv1.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='HealthWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('specialization', models.CharField(max_length=25)),
                ('desc', models.CharField(default='', max_length=150)),
                ('work_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apiv1.stuntplace')),
            ],
        ),
        migrations.CreateModel(
            name='FunStuntUserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField()),
                ('answer_is_correct', models.BooleanField()),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apiv1.funstuntqa')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apiv1.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('born_date', models.DateField()),
                ('gender', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apiv1.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='DentistsmileTrace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('age_day', models.IntegerField(default=0)),
                ('exclusive_asi', models.BooleanField(default=True)),
                ('disease_history', models.BooleanField(default=True)),
                ('immunization_history', models.CharField(max_length=60)),
                ('z_score', models.FloatField()),
                ('growth_level', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('children', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apiv1.children')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apiv1.userprofile')),
            ],
            options={
                'unique_together': {('user', 'week', 'children')},
            },
        ),
    ]
