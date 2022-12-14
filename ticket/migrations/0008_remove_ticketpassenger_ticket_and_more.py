# Generated by Django 4.1.3 on 2022-11-14 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0007_ticket_passengers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketpassenger',
            name='ticket',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='passengers',
            field=models.ManyToManyField(to='ticket.ticketpassenger'),
        ),
        migrations.AlterField(
            model_name='ticketpassenger',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
