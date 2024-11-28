import itertools
import threading
import time
import sys, os
from book import Books

done: bool = False
#анимация загрузки
def animate() -> None:
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rЗагрузка ' + c)
        sys.stdout.flush()
        time.sleep(0.1)


if __name__ == "__main__":
    t = threading.Thread(target=animate)
    t.start()
    #длина загрузки
    time.sleep(3)
    done = True

    book = Books()
    while True:
        sys.stdout.write('\rБиблиотека\n1)Просмотр всей библиотеки\n2)Поиск\n3)Редактирование\n4)Добавление\n')
        action = str(input("Введите действие:"))
        os.system('cls')
        if action == '1':
            books = book.show_all()
            sys.stdout.write(books)
            action = str(input("Введите действие:"))
            if action == "0":
                pass
            else:
                book.show(action)
            
            os.system('cls')
        elif action == '2':
            os.system('cls')
            string = str(input('Введите год, автора или заголовок:'))
            string = book.find(string)
            sys.stdout.write(string)
            action = str(input("Введите действие:"))
            if action == "0":
                pass
            else:
                book.show(action)
            
            os.system('cls')
        
        elif action == '3':
            os.system('cls')
            books = book.show_all()
            sys.stdout.write(books)
            num = str(input("Введите книгу которую хотите отредактировать:"))
            os.system('cls')
            sys.stdout.write("\rЧто вы хотите сделать с книгой?\n0)Выйти\n1)Удалить\n2)Отредактировать\n")
            action = str(input("Введите действие:"))
            if action == "0":
                pass
            elif action == "1":
                book.delete(num)
                book.save()
            elif action == "2":
                book.edit(num)
                book.save() 
            else:
                pass
            
            os.system('cls')
        elif action == '4':
            os.system('cls')
            book.add()
            book.save()

            os.system('cls')
        else:
            print('\r\nНет такого варианта попробуйте еще раз' )


