# Sistema CRUD de Pacientes para Clínica de Saúde

Este projeto foi desenvolvido como parte de um trabalho acadêmico para a disciplina de Banco de Dados, com o objetivo de implementar um sistema CRUD (Create, Read, Update, Delete) completo para gerenciar informações de pacientes em uma clínica de saúde. O sistema permite o cadastro, visualização, edição e exclusão de dados de pacientes de forma eficiente e organizada.

## Funcionalidades

- **Cadastro de Pacientes**: Adicione novos pacientes ao sistema com informações detalhadas como nome, data de nascimento, sexo, telefone, CPF e peso.
- **Visualização de Pacientes**: Consulte os dados de pacientes individualmente ou em uma lista completa.
- **Edição de Pacientes**: Atualize as informações de pacientes existentes.
- **Exclusão de Pacientes**: Remova registros de pacientes do sistema.
- **Interface Web Amigável**: Acesso e interação com o sistema através de um navegador web.

## Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes tecnologias:

- **Python**: Linguagem de programação principal.
- **Django**: Framework web de alto nível para o desenvolvimento rápido e seguro de aplicações web.
- **SQLite**: Banco de dados leve e integrado, ideal para projetos de pequeno a médio porte e desenvolvimento local.

## Estrutura do Projeto

Abaixo estão alguns trechos de código que ilustram a estrutura e os componentes chave do projeto:

### Modelo `Paciente` (Django Models)

O modelo `Paciente` define a estrutura dos dados dos pacientes no banco de dados:

```python
class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField(max_length=30)
    sexo = models.CharField(max_length=1)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11)
    peso = models.IntegerField()

    def __str__(self):
        return self.nome
```

### Configuração de URLs (Django `urls.py`)

As URLs do projeto são configuradas para rotear as requisições para as respectivas views:

```python
from django.contrib import admin
from django.urls import path
from app.views import home, form, create, view, edit, update, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
]
```
## Como Executar o Projeto

Para executar este projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Apolo442/API-Django.git
    cd <DIRETÓRIO>
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    # venv\Scripts\activate  # No Windows
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Crie um superusuário (opcional, para acessar o admin do Django):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

7.  **Acesse o sistema:**
    Abra seu navegador e acesse `http://127.0.0.1:8000/`.


