
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20201107_0336'),
    ]

    operations = [
        migrations.CreateModel(
            name='FailedPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txn_date', models.CharField(max_length=23)),
                ('response_message', models.TextField()),
                ('response_code', models.CharField(max_length=3)),
                ('txn_id', models.TextField()),
                ('txn_amount', models.CharField(max_length=9)),
                ('order_id', models.IntegerField()),
                ('status', models.CharField(max_length=12)),
                ('bank_txn_id', models.CharField(max_length=12)),
                ('Payment_mode', models.CharField(max_length=25)),
                ('gateway_name', models.CharField(max_length=25)),
                ('currency', models.CharField(max_length=8)),
            ],
        ),
    ]
