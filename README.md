# Тестовое задание

# Задачи
Оригинальное задание можно почитать в файле: ´test_description.txt´

# Решение
1. имплементация находиться в функции ´correct_text´. Подходяший тест ´TestSolution.test_correct_text´
2. имплементация находиться в функции ´count_elements´. Подходяший тест ´TestSolution.test_count_elements´
3. имплементация находиться в функции ´json_diff´. Подходяший тест ´TestSolution.test_json_diff´
4. В MongoDB сошествует так называемый индекс TTL (Time To Live). Его используют чтобы удалять документы через определенное время. Он ставиться на BSON date type документа следующим образом.
´´´
db.tempdocs.createIndex({"lastModified": 1}, {expireAfterSeconds: 86400})
´´´
В этом примери коллекция документов называеться ´tempdocs´ и поле на которое мы ставим индекс ´lastModified´.
5. Можно рассмотреть следующею архитектуру. Контроллер, который получает реквест (например POST) на адрес ´/Datalore´ использует router object который в свою очередь вызывает нужную функцую зависимо от значения ´function´ и передает ей полученные данные. Для выдачи ответа есть две опции. Можно в обратном порядке ´function return - router return - controller - http response´. Также можно дать ответ асинхронно. Router сразу дает ответ ´HTTP 202 Accepted´ с адресом на который придет результат.
