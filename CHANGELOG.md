# Changelog

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
