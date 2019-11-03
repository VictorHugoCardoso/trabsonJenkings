# Generated by Django 2.2.5 on 2019-11-03 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_delete_notas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nota1', models.DecimalField(decimal_places=2, default=0, max_digits=9, null=True)),
                ('nota2', models.DecimalField(decimal_places=2, default=0, max_digits=9, null=True)),
                ('nota3', models.DecimalField(decimal_places=2, default=0, max_digits=9, null=True)),
                ('nota4', models.DecimalField(decimal_places=2, default=0, max_digits=9, null=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Aluno')),
                ('discliplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Disciplina')),
            ],
        ),
    ]
