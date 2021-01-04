# Django-Funcionarios-Departamentos
Projeto de banco de dados com informações de Funcionários e Departamentos

# Projeto Python e Django

Digitar os seguintes comandos no seu terminal

1 - Instalar a venv:
    pip install venv

2 - Criar a venv:
    python -m venv venv (windows)

3 - Entrar na venv:
    cd venv/Scripts/activate.bat (windows)
    source venv/bin/activate (Linux e Mac)

4 - Instalar o Django:
    pip install django

5 - Criar esse projeto:
    django-admin startproject meuProjeto .

6 - Instalar o pylint:
    python -m pip install pylint

7 - Criar o banco de dados:
    python manage.py migrate

8 - Criar o seu usuário admin:
    python manage.py createsuperuser

9 - Para rodar esse projeto em sua máquina local:
    python manage.py runserver