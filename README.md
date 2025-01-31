# FastAPI  Service
Пример бота для ответа на вопросы про ИТМО с использованием модели GigaChat.
Приложение написано на FastAPI, разворачивается при помощи docker-compose.

## Решение

Экземпляр развернутого решения находится на ip 158.160.130.157:8080

Пример запроса:
```bash
curl --location --request POST 'http://localhost:8080/api/request' \
--header 'Content-Type: application/json' \
--data-raw '{
  "query": "В каком городе находится главный кампус Университета ИТМО?\n1. Москва\n2. Санкт-Петербург\n3. Екатеринбург\n4. Нижний Новгород",
  "id": 1
}'
```
Ответ системы:
```json
{
  "id": 1,
  "answer": 2,
  "reasoning": "Из информации на основании источников",
  "sources": [
    "https://ru.wikipedia.org/wiki/%D0%A3%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82_%D0%98%D0%A2%D0%9C%D0%9E",
    "https://itmo.ru/ru/map/karta_korpusov.htm"
  ]
}
```

## Сборка
Для запуска выполните команду:

```bash
docker-compose up -d
```
Она соберёт Docker-образ, а затем запустит контейнер.

После успешного запуска контейнера приложение будет доступно на http://localhost:8080.

## Проверка работы
Отправьте POST-запрос на эндпоинт /api/request. Например, используйте curl:

```bash
curl --location --request POST 'http://localhost:8080/api/request' \
--header 'Content-Type: application/json' \
--data-raw '{
  "query": "В каком городе находится главный кампус Университета ИТМО?\n1. Москва\n2. Санкт-Петербург\n3. Екатеринбург\n4. Нижний Новгород",
  "id": 1
}'
```
В ответ вы получите JSON вида:

```json
{
  "id": 1,
  "answer": 1,
  "reasoning": "Из информации на сайте",
  "sources": [
    "https://itmo.ru/ru/",
    "https://abit.itmo.ru/"
  ]
}
```

id будет соответствовать тому, что вы отправили в запросе,
answer будет содержать правильный вариант ответа.

Чтобы остановить сервис, выполните:

```bash
docker-compose down
```
