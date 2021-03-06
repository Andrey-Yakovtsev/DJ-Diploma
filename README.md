## Дипломный проект по курсу «Django: создание функциональных веб-приложений»

Cайт спортивного интернет-магазина. Прототипом выступал www.tri-sport.ru, написанный на PHP.
Реализована клиентская часть сервиса и интерфейс администрирования.



## Описание клиентской части
Главное меню слева изменяет содердимое в зависимости от авторизации пользователя: вход/выход
Состояние корзины привязано к сессии.
Ниже товарного листинга приведен листинг статей, к каждой из которых привязаны соответствующие товары.
    
Меню:

Кнопка - "Все категории" формирует меню динамически, через процессор контекста. При добавлении категории в админке - 
она появится в меню сайта.
Иерархия меню реалзована через всязь родительской-детской категории. В меню для соответствующего ыводав используется
фильтрация кверисетов. 

* Кнопка входа/выхода в зависимости от статуса авторизации.


Для авторизации и входа используется аутентификацию по email'у.


### Интерфейс администратора имеет возможности:

* Редактирование разделов.
* Редактирование товаров.
* Редактирование статей на главной странице и привязывание к ним товаров,
  которые должны отображаться после нее.
* Просмотр списка заказов пользователей, отсортированных по дате создания,
    с указанием пользователя и количества товаров.
* Страница детализации заказа с просмотром списка заказанных товаров.

## Дизайн
Применен шаблон с MDBootstrap.com

## Требования к организации системы

Провести миграции:

```bash
python manage.py migrate
```

Загрузить тестовые данные:

```bash
python manage.py loaddata products.json
```
Создать суперпользователя:

```bash
python manage.py createsuperuser
```