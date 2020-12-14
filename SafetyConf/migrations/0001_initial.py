from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer1', models.CharField(max_length=30)),
                ('answer2', models.CharField(max_length=30)),
                ('sendDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emergencyContactId', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('sendDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeId', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=30)),
                ('mailaddress', models.EmailField(max_length=254)),
                ('subMailaddress', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupId', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SafetyConf.Group'),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='destinationGroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SafetyConf.Group'),
        ),
        migrations.AddField(
            model_name='answer',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SafetyConf.Employee'),
        ),
    ]
