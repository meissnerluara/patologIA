#!/bin/bash

pip install --upgrade pip
pip install --force-reinstall Django

# Instalar dependências
pip install -r requirements.txt

# Aplicar migrações do banco de dados
python manage.py migrate

# Coletar arquivos estáticos
python manage.py collectstatic --noinput
