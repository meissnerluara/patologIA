from django.db import migrations

def create_category(apps, schema_editor):
    Category = apps.get_model('QuestionsApp', 'QuestionTypesModel')
    
    Category.objects.create(Category='Questões de múltipla escolha')
    Category.objects.create(Category='Questões de Demarcação de Imagens')


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsApp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_category),
    ]
