# Тестовое задание

# Задачи
Оригинальное задание можно прочитать в файле: `test_description.txt`

# Решение
1. имплементация находиться в функции `correct_text`. Подходяший тест `TestSolution.test_correct_text``

2. имплементация находиться в функции `count_elements`. Подходяший тест `TestSolution.test_count_elements`

3. имплементация находиться в функции `json_diff`. Подходяший тест `TestSolution.test_json_diff`

4. В MongoDB существует так называемый индекс TTL (Time To Live). Его используют, чтобы удалять документы через определенное время. Он ставится на BSON date type документа следующим образом.
```
    db.tempdocs.createIndex({"lastModified": 1}, {expireAfterSeconds: 86400})
```
В этом примере коллекция документов называется `tempdocs` и поле на которое мы ставим индекс `lastModified`.

5.
  1. Можно рассмотреть следующею архитектуру. Контроллер, который получает реквест (например POST) на адрес `/Datalore` использует router object который в свою очередь вызывает нужную функцию зависимо от значения `function` и передает ей полученные данные. Для выдачи ответа есть две опции. Можно в обратном порядке `function return - router return - controller - HTTP response`. Также можно дать ответ асинхронно. В этом случае controller сразу дает ответ `HTTP 202 Accepted` с адресом на который придет результат.
  2. В контексте ботов, архитектура похожая. На определенный адрес (вебхоок адрес) приходит сообщение с командой (имя функции может совпадать) и данные (payload). Диспачер играет роль раутера и запускает нужную функцию. Функции могут быть запущенны синхронно, асинхронно или как background tasks через celery. Аналогично с веб фрамеворком, можно между диспачером и функцией установить middleware. Ответ, или результат, отправляется в определенный чат через апи/бот библиотеку.