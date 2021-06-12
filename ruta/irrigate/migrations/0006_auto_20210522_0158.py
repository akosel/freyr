# Generated by Django 3.2.3 on 2021-05-22 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("irrigate", "0005_auto_20210522_0143"),
    ]

    operations = [
        migrations.CreateModel(
            name="ScheduleDay",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "weekday",
                    models.IntegerField(
                        choices=[
                            (0, "Monday"),
                            (1, "Tuesday"),
                            (2, "Wednesday"),
                            (3, "Thursday"),
                            (4, "Friday"),
                            (5, "Saturday"),
                            (6, "Sunday"),
                        ]
                    ),
                ),
                (
                    "month",
                    models.IntegerField(
                        choices=[
                            (0, "January"),
                            (1, "February"),
                            (2, "March"),
                            (3, "April"),
                            (4, "May"),
                            (5, "June"),
                            (6, "July"),
                            (7, "August"),
                            (8, "September"),
                            (9, "October"),
                            (10, "November"),
                            (11, "December"),
                        ]
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="scheduletime",
            name="actuator",
        ),
        migrations.RemoveField(
            model_name="scheduletime",
            name="weekday",
        ),
        migrations.AddField(
            model_name="scheduletime",
            name="actuators",
            field=models.ManyToManyField(to="irrigate.Actuator"),
        ),
        migrations.AddField(
            model_name="scheduletime",
            name="schedule_day",
            field=models.ManyToManyField(to="irrigate.ScheduleDay"),
        ),
    ]
