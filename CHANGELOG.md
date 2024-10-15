# Changelog

## 0.14.0 (2024-10-15)

### Feat

- improve validators

## 0.13.1 (2024-10-14)

### Refactor

- change helper to types conversion
- create a helper to mapping models
- create a helper to mapping forms
- remove unused operations
- change how SupplierCreateController handle forms
- change how ServiceOrderCreateController handle forms
- change how EmployeePositionCreateController handle forms
- change how EmployeeCreateController handle forms
- change how ClientCreateController handle forms
- change how BrandCreateController handle forms

## 0.13.0 (2024-10-14)

### Feat

- add brands
- add SQLAlchemy-Utils

### Fix

- use email fields for email columns

### Refactor

- use a default param to index templates
- add an helper to create model forms
- move pages to a pages folder
- add field_args type
- rename forms to model forms

## 0.12.0 (2024-10-13)

### Feat

- add Flask-Alembic

### Refactor

- reconfigure alembic hooks and app models

## 0.11.1 (2024-10-12)

### Refactor

- add SQLModel

## 0.11.0 (2024-10-10)

### Feat

- change reopen button color
- add employees

### Refactor

- improve forms
- change forms to use model_form function
- add wtforms-sqlalchemy

## 0.10.0 (2024-10-09)

### Feat

- add open/close service order button
- add open status to service_order
- change buttons design
- add Bootstrap Icons

### Refactor

- rename many forms and models

## 0.9.0 (2024-10-08)

### Feat

- add client selection on service ordem form
- create InjectChoicesOperation
- add 'other' to genders

## 0.8.0 (2024-10-08)

### Feat

- add service order creation and visualization

## 0.7.0 (2024-10-07)

### Feat

- add suppliers creation and visualization
- add route for suppliers

## 0.6.0 (2024-10-07)

### Feat

- add SupplierIndexView
- add SupplierListController
- add extra verification on ClientCreateController

### Refactor

- move client controllers to a folder
- improve general type hints
- improve models type hints
- move app configuration to a function
- remove manual method definitions on views
- inject form into controller

## 0.5.0 (2024-10-06)

### Feat

- query clients to a table
- add query to list all clients
- add ClientIndexView
- move validation to utils layer

### Refactor

- apply dependency reversion to views
- create factories for views
- reorganize project folder structure
- make some publics attributes privates and constants
- move DB Framework logic to DbOperations class
- move messages and header to includes folder
- improve FlaskSqlAlchemyOperations type hints
- rename views files to match classes names

## 0.4.0 (2024-10-05)

### Feat

- **clients**: add database and validation

## 0.3.0 (2024-10-05)

### Feat

- **clients**: add ClientCreateController

## 0.2.0 (2024-10-05)

### Feat

- add a form to sign up clients
- adicione sistema de forms no Flask
- termine de configurar a primeira rota
- termine de configurar os models e o servidor
- add OrdemServicoModel
- add some models
