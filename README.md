# Тестовое задание

# Задачи
Оригинальное задание можно прочитать в файле: `test_description.txt`

# Решение
1. задача 1
    * код: `src.solution.correct_text`
    * тест `test.test_solution.TestSolution.test_correct_text`
2. задача 2
    * код: `src.solution.count_elements`
    * тест `test.test_solution.TestSolution.test_count_elements`
3. задача 3
    * код: `src.solution.json_diff`
    * тест `test.test_solution.TestSolution.test_json_diff`
4. задача 4
    * В MongoDB существует так называемый индекс TTL (Time To Live). Его используют, чтобы удалять документы через определенное время. Он ставится на BSON date type документа следующим образом. `db.tempdocs.createIndex({"lastModified": 1}, {expireAfterSeconds: 86400})` В этом примере коллекция документов называется `tempdocs` и поле на которое мы ставим индекс `lastModified`. 
5. задача 5
    * Можно рассмотреть следующею архитектуру. Контроллер, который получает реквест (например POST) на адрес `/Datalore` использует router object который в свою очередь вызывает нужную функцию зависимо от значения `function` и передает ей полученные данные. Для выдачи ответа есть две опции. Можно в обратном порядке `function return - router return - controller - HTTP response`. Также можно дать ответ асинхронно. В этом случае controller сразу дает ответ `HTTP 202 Accepted` с адресом на который придет результат.
    * В контексте ботов, архитектура похожая. На определенный адрес (вебхоок адрес) приходит сообщение с командой (имя функции может совпадать) и данные (payload). Диспачер играет роль раутера и запускает нужную функцию. Функции могут быть запущенны синхронно, асинхронно или как background tasks через celery. Аналогично с веб фрамеворком, можно между диспачером и функцией установить middleware. Ответ, или результат, отправляется в определенный чат через апи/бот библиотеку.
