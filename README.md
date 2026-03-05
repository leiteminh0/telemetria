# API Telemetria - Sistema de Controle de Frota Agrícola

Sistema para cadastro e controle por telemetria de frota de veículos agrícolas desenvolvido com Django REST Framework.

## 📋 Requisitos

- Python 3.10+
- MySQL 8.0+
- pip (gerenciador de pacotes Python)

## 🚀 Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd telemetria
```

### 2. Crie e ative o ambiente virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para `.env`:

```bash
copy .env.example .env  # Windows
cp .env.example .env    # Linux/Mac
```

Edite o arquivo `.env` com suas configurações do MySQL:

```
DB_NAME=telemetria
DB_USER=root
DB_PASSWORD=sua_senha_aqui
DB_HOST=localhost
DB_PORT=3306
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
```

### 5. Crie o banco de dados MySQL

Acesse o MySQL e crie o banco de dados:

```sql
CREATE DATABASE telemetria CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 6. Execute as migrações

```bash
python manage.py migrate
```

### 7. (Opcional) Crie um superusuário

```bash
python manage.py createsuperuser
```

### 8. Inicie o servidor

```bash
python manage.py runserver
```

O servidor estará disponível em: `http://localhost:8000`

## 📚 Documentação da API

Após iniciar o servidor, acesse a documentação interativa:

- **Swagger UI:** http://localhost:8000/swagger/
- **ReDoc:** http://localhost:8000/redoc/
- **Admin Django:** http://localhost:8000/admin/

## 🔗 Endpoints da API

Todos os endpoints estão disponíveis em `/api/`:

- `/api/marcas/` - CRUD de Marcas
- `/api/modelos/` - CRUD de Modelos
- `/api/unidades-medida/` - CRUD de Unidades de Medida
- `/api/veiculos/` - CRUD de Veículos
- `/api/medicoes/` - CRUD de Medições
- `/api/medicoes-veiculo/` - CRUD de Medições de Veículos

Cada endpoint suporta:
- `GET` - Listar todos ou buscar por ID
- `POST` - Criar novo registro
- `PUT` - Atualizar registro completo
- `PATCH` - Atualizar registro parcialmente
- `DELETE` - Remover registro

## 🗄️ Estrutura do Banco de Dados

O projeto possui 6 models principais:

1. **Marca** - Marcas de veículos
2. **Modelo** - Modelos de veículos
3. **UnidadeMedida** - Unidades de medida (km, litros, etc)
4. **Veiculo** - Cadastro de veículos (relacionado com Marca e Modelo)
5. **Medicao** - Tipos de medição (relacionado com UnidadeMedida)
6. **MedicaoVeiculo** - Registro de medições dos veículos (relacionado com Veiculo e Medicao)

## 🧪 Testes SQL

Consulte o arquivo `TESTES_SQL.md` para queries SQL de validação com JOINs entre as tabelas.

## 🛠️ Tecnologias Utilizadas

- Django 5.0+
- Django REST Framework 3.14+
- drf-yasg (Swagger/OpenAPI)
- django-filter
- mysqlclient
- django-cors-headers
- python-decouple

## 📝 Notas

- O projeto usa `on_delete=models.CASCADE` em todas as ForeignKeys
- CORS está habilitado para todas as origens (apenas para desenvolvimento)
- A documentação Swagger está configurada com todos os endpoints documentados
