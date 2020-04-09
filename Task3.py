documents = [
 {"type": "passport", "number": "2207 876234"},
 {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
 {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
 ]

def exception():
        for i in documents:
            try:
                print (i ["name"])
            except KeyError:
                print ('У одного из владельцев документа отсутствует имя')
                break


exception()