# Generated by Django 2.2.6 on 2019-11-01 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20191027_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='frequencia',
            name='discliplina',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Disciplina'),
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='aluno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Aluno'),
        ),
        migrations.AlterField(
            model_name='notas',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Aluno'),
        ),
        migrations.AlterField(
            model_name='notas',
            name='discliplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Disciplina'),
        ),
        migrations.AlterField(
            model_name='notas',
            name='nota1',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='notas',
            name='nota2',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='notas',
            name='nota3',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='notas',
            name='nota4',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, null=True),
        ),
    ]