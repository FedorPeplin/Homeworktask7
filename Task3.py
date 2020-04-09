documents = [
 {"type": "passport", "number": "2207 876234", "name": "Геннадий Покемонов"},
 {"type": "invoice", "number": "11-2", "name": "Вася Пупкин"},
 {"type": "insurance", "number": "10006",}
 ]

def exception():
        for i in documents:
            try:
                namecheck=i["name"]
            except KeyError:
                indexoferror=int(documents.index(i))+1 #прибавляем 1, т.к. нумерация "людей" начинается с 1, а не 0, как делает питон
                print ('У одного из владельцев документа отсутствует имя, а именно у пользователя номер', indexoferror)

exception()