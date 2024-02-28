# API for a fake financial institution 

### Описание
API представляет собой простое банковское приложение, разработанное на Django REST Framework. Приложение позволяет пользователям создавать банковские аккаунты, совершать транзакции между аккаунтами и просматривать историю транзакций.

## Требования для пользования приложением

Убедитесь, что Docker и Docker-Compose установлены на вашем ПК.


### 1. Склонируйте репозиторий:

    git clone https://github.com/IgChern/bank_api

### 2. Перейдите по пути проекта:

    cd bank_api

### 3. Создайте файл .env со своими собственными настройками (либо, вы можете оставить .env пустым):

    POSTGRES_NAME=<your_settings>
    POSTGRES_USER=<your_settings>
    POSTGRES_PASSWORD=<your_settings>
    POSTGRES_HOST=<your_settings>
    POSTGRES_PORT=<your_settings>

### 4. Соберите и запустите Docker контейнер:

    docker-compose build

    docker-compose up

### 5. Доступ к интерфейсу проекта:  
1. [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) - Страница API маршрутов
2. [http://127.0.0.1:8000/api/customer/](http://127.0.0.1:8000/api/customer/) - URL создания клиента
3. [http://127.0.0.1:8000/api/account/](http://127.0.0.1:8000/api/account/) - URL создания банковского аккаунта
4. [http://127.0.0.1:8000/api/transfer/](http://127.0.0.1:8000/api/transfer/) - URL обработки трансфера между аккаунтами
5. [http://127.0.0.1:8000/api/account/<account_id>/all_transfers/](http://127.0.0.1:8000/api/account/<account_id>/all_transfers/) - URL для просмотра транзакций для выбранного аккаунта <account_id>

### 6. Отправка GET, POST, PUT, DELETE запросов

Вы можете использовать Postman для отправки запросов по адресам.  
1. [http://127.0.0.1:8000/api/customer/](http://127.0.0.1:8000/api/customer/)  
GET(получить список клиентов)  
POST(зарегистрировать клиента, указать имя клиента)  
`{
    "name": ""
}`  
2. [http://127.0.0.1:8000/api/account/](http://127.0.0.1:8000/api/account/)  
GET(получить список аккаунтов)  
POST(зарегистрировать аккаунт клиента, указать id клиента в поле customer, указать депозит)  
`{
    "customer": null,
    "deposit": null
}`  
3. [http://127.0.0.1:8000/api/transfer/](http://127.0.0.1:8000/api/transfer/)  
GET(получить список транзакций)  
POST(зарегистрировать транзакцию между аккаунтами, указать id клиента-отправителя, id клиента-получателя, сумму к переводу)  
`{
    "sender": null,
    "recipient": null,
    "amount": null
}`  
4. [http://127.0.0.1:8000/api/customer/<id_customer>](http://127.0.0.1:8000/api/customer/<id_customer>/)  
GET(получить информацию по клиенту)  
PUT/PATCH(изменить поле name)  
DELETE(удалить клиента)  
5. [http://127.0.0.1:8000/api/account/<id_account> ](http://127.0.0.1:8000/api/account/<id_account>/)  
GET(получить информацию по аккаунту)  
PUT/PATCH(изменить поле депозита)  
DELETE(удалить аккаунт у клиента)
6. [http://127.0.0.1:8000/api/transfer/<id_transfer>](http://127.0.0.1:8000/api/transfer/<id_transfer>)
GET(получить информацию по транзакции) 

### 7. Запуск тестов

    docker ps
    docker exec -it <ID_bank_api-django> coverage run manage.py test
    docker exec -it <ID_bank_api-django> coverage report - результат покрытия тестами

### 7. Остановка Docker контейнера:

    docker-compose down
