import json
from typing import Union
import webbrowser



class Books:


    def __init__(self, path='books.json') -> None:
        self.path = path
        with open(path, 'r', encoding='utf-8') as read:
            self.data = json.load(read)


    def show(self, id: str):
        try:
            webbrowser.open(self.data[id][0]['path'])
        except:
            print("error")


    def show_all(self) -> str:
        string: str = "0)Выход\n"
        for key, value in self.data.items():
                string += f"\r{key}){value[0]['title']} {value[0]['author']} {value[0]['year']} {value[0]['status']}\n"
        return(string)


    def find(self, argument: str) -> Union[list, str]:
        x: bool = False
        all_data: list = []
        for i in range(1, len(self.data) + 1):
            for z in self.data[str(i)][0].values():
                if argument == z or argument in z:
                    all_data.append([str(i), self.data[str(i)][0]]) 
                    x = True
        if x == False:
            return("\nИнформация не найдена\n0)Выход")
        else:
            string = '0)Выход\n'
            for i in all_data:
                string += f'{i[0]}){i[1]["title"]} {i[1]["author"]} {i[1]["year"]} {i[1]["status"]}\n'
            return(string)


    def add(self) -> None:
        id = str(int(max(self.data)) + 1)
        title = str(input("Введите заголовок:"))
        author = str(input("Введите автора:"))
        year = str(input("Введите год:"))
        status = str(input("Введите статус:"))
        book_path = str(input("Введите путь до книги:"))
        self.data[id] = [{'title': title, "author": author, "year": year, "status": status, "path": book_path}]


    def edit(self, id: str) -> None:
        title = str(input("Введите заголовок:"))
        author = str(input("Введите автора:"))
        year = str(input("Введите год:"))
        status = str(input("Введите статус:"))
        book_path = str(input("Введите путь до книги:"))
        self.data[id] = [{'title': title, "author": author, "year": year, "status": status, "path": book_path}]


    def delete(self, id: str) -> None:
        del self.data[id]


    def save(self) -> int:
        data = json.dumps(self.data, sort_keys=True, ensure_ascii=False).encode("utf-8")
        file = open(self.path, 'w', encoding='utf-8')
        file.write(data.decode())
        file.close()
        return(1)



if __name__ == "__main__":
    pass