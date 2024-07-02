# Generated by Django 5.0.6 on 2024-07-01 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, max_length=200, null=True, verbose_name='부서')),
                ('category', models.CharField(blank=True, choices=[('전 근무지', '전 근무지'), ('현 근무지', '현 근무지'), ('인턴', '인턴')], max_length=15, null=True, verbose_name='유형')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(blank=True, max_length=200, null=True, verbose_name='학교명')),
                ('grade', models.CharField(blank=True, choices=[('1학년', '1학년'), ('2학년', '2학년'), ('3학년', '3학년'), ('4학년 이상', '4학년 이상'), ('졸업', '졸업')], max_length=15, null=True, verbose_name='학년')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_image', models.ImageField(upload_to='profile_image', verbose_name='프로필사진')),
                ('short_intro', models.CharField(max_length=200, verbose_name='한줄소개')),
                ('certificate', models.CharField(blank=True, max_length=300, null=True, verbose_name='자격증')),
                ('interest', models.CharField(max_length=200, verbose_name='대표관심분야')),
                ('current_job', models.CharField(max_length=200, verbose_name='현재관심분야')),
                ('introduce', models.TextField(default='', verbose_name='소개')),
                ('career', models.ManyToManyField(to='myprofile.career', verbose_name='경력')),
                ('education', models.ManyToManyField(to='myprofile.education', verbose_name='학력')),
            ],
        ),
    ]
