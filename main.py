import time

# def test_time(fn):
#     def wrapper(*args, **kwargs):
#         st = time.time()
#         res = fn(*args, **kwargs)
#         dt = time.time() - st
#         print(f"Время работы: {dt} сек")
#         return res
#
#     return wrapper
#
#
# @test_time
# def get_nod(a, b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a
#
#
# get_nod = get_nod(265432, 10065000)
# print(get_nod)


# --------------------------------------------------------------------


# import sys
#
#
# class StreamData:
#
#     def create(self, fields, lst_values):
#         self.fields = fields
#         self.lst_in  = lst_values
#         if len(self.lst_in) != len(self.fields):
#             return False
#         else:
#             return True
# # здесь объявляется класс StreamData
#
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
#
#
# sr = StreamReader()
# data, result = sr.readlines()


# --------------------------------------------------------------------


# import sys
#
# # программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#
#
# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     def insert(self, data):
#         for i in data:
#             self.lst_data.append(dict(zip(self.FIELDS, i.split())))
#
#     def select(self, a, b):
#         return self.lst_data[a:b+1]
#
#
#     # здесь добавлять методы
#
#
# db = DataBase()
# db.insert(lst_in)


# --------------------------------------------------------------------

# class Translator:
#     def add(self, eng, rus):
#         if 'tr' not in self.__dict__:
#             self.tr = {}
#
#         self.tr.setdefault(eng, [])
#         if rus not in self.tr[eng]:
#             self.tr[eng].append(rus)
#         # здесь продолжайте метод add
#
#     def remove(self, eng):
#         self.tr.pop(eng, False)
#
#     def translate(self, eng):
#         return self.tr[eng]
#
#
#
# tr = Translator()
# tr.add("tree", "дерево")
# tr.add("car", "машина")
# tr.add("car", "автомобиль")
# tr.add("leaf", "лист")
# tr.add("river", "река")
# tr.add("go", "идти")
# tr.add("go", "ехать")
# tr.add("go", "ходить")
# tr.add("milk", "молоко")
#
# tr.remove('car')
#
# print(*tr.translate('go'))


# --------------------------------------------------------------------

# class Point:
#     def __init__(self, x, y, color='black'):
#         self.x = x
#         self.y = y
#         self.color = color
#
# points = []
#
# for i in range(1, 2001, 2):
#     points.append(Point(i, i))
# points[1].color = 'red'

# --------------------------------------------------------------------


# class Line:
#
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Rect:
#
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Ellipse:
#
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
# from random import randint
#
#
# elements = [(Line, Rect, Ellipse)[randint(0, 2)](1, 2, 3, 4) for i in range(217)]
# for i in elements:
#     if isinstance(i, Line):
#         i.ep, i.sp = 0, 0

# --------------------------------------------------------------------

# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if type(self.a) not in (int, float) or type(self.b) not in (int, float) or type(self.c) not in (int, float):
#             return 1
#         if self.a + self.b > self.c  or self.a + self.c > self.b or self.b + self.c > self.a:
#             return 3
#         else:
#             return 2
#
#
# TriangleChecker(1, 2, 3).is_triangle()

# --------------------------------------------------------------------

# class Graph:
#     def __init__(self, data: list[int, float]):
#         self.data = data
#         self.is_show = True
#
#     def set_data(self, data):
#         self.data = data
#
#     def show_table(self):
#         if not self.is_show:
#             return "Отображение данных закрыто"
#
#         else:
#             print([i for i in self.data])
#
#     def show_graph(self):
#         print(f"Графическое отображение данных {[i for i in self.data]}")
#
#     def show_bar(self):
#         if not self.is_show:
#             return "Отображение данных закрыто"
#
#     def set_show(self, fl_show: bool):
#         self.is_show = fl_show

# --------------------------------------------------------------------


# class CPU:
#     def __init__(self, name, fr):
#         self.fr = fr
#         self.name = name
#
#
# class Memory:
#     def __init__(self, name, volume ):
#         self.volume = volume
#         self.name = name
#
#
#
# class MotherBoard:
#     def __init__(self, name, cpu):
#         self.name = name
#         self.cpu = CPU
#         self.total_mem_slots = 4
#
#     def get_config(self):
#         ...

# --------------------------------------------------------------------

# class Cart:
#     def __init__(self):
#         self.goods = []
#
#     def add(self, gd):
#         self.goods.append(gd)
#
#     def remove(self, indx):
#         self.goods.pop(indx)
#
#     def get_list(self):
#         return [f"{x.name}: {x.price}" for x in self.goods]
#
#
# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class TV:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Notebook:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Cup:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# cart = Cart()
# tv1 = TV("samsung", 1111)
# tv2 = TV("LG", 1234)
# table = Table("ikea", 2345)
# n1 = Notebook("msi", 5433)
# n2 = Notebook("apple", 542)
# c = Cup("keepcup", 43)
#
# cart.add(tv1)
# cart.add(tv2)
# cart.add(n1)
# cart.add(n2)
# cart.add(c)
# print(cart.get_list())
# --------------------------------------------------------------------


'''

Объявите два класса: 

Cell - для представления клетки игрового поля;
GamePole - для управления игровым полем, размером N x N клеток.

С помощью класса Cell предполагается создавать отдельные клетки командой:

c1 = Cell(around_mines, mine)
Здесь around_mines - число мин вокруг данной клетки поля; 
mine - булева величина (True/False), означающая наличие мины в текущей клетке. 
При этом, в каждом объекте класса Cell должны создаваться локальные свойства:

around_mines - число мин вокруг клетки (начальное значение 0);

mine - наличие/отсутствие мины в текущей клетке (True/False);

fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).


С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:

pole_game = GamePole(N, M)
Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка представляется объектом класса Cell и 
все объекты хранятся в двумерном списке N x N элементов - локальном свойстве pole объекта класса GamePole. 

В классе GamePole должны быть также реализованы следующие методы:

init() - инициализация поля с новой расстановкой M мин 
(случайным образом по игровому полю, разумеется каждая мина должна находиться в отдельной клетке).

show() - отображение поля в консоли в виде таблицы чисел открытых клеток 
(если клетка не открыта, то отображается символ #; мина отображается символом *; между клетками при отображении ставить пробел).

При создании экземпляра класса GamePole в его инициализаторе следует 
вызывать метод init() для первоначальной инициализации игрового поля.

В классе GamePole могут быть и другие вспомогательные методы.

Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12. 

P.S. На экран в программе ничего выводить не нужно.

'''


# class Cell:
#     def __init__(self, around_mines, mine):
#         self.around_mines = around_mines
#         self.mine = mine
#         self.fl_open = False
#
#
# class GamePole:
#     def __init__(self, N: int, M):
#         self.N = N
#         self.M = M
#         self.pole = []
#
#     def init(self):
#         for i in range(N):
#             self.pole[i].append()
#
#     def show(self):
#         ...
#
#
# pole_game = GamePole(10, 12)
#
#
#
#
# assert isinstance(pole_game, GamePole) and hasattr(GamePole, 'init') and hasattr(GamePole, 'show')
#
# # Cell.__doc__
#
# N = 10
# M = 10
#
#
# def get_around_mines(i, j):
#     n = 0
#     for k in range(-1, 2):
#         for l in range(-1, 2):
#             ii, jj = k + i, l + j
#             if ii < 0 or jj < 0 or ii >= N or jj >= N:
#                 continue
#             if pole_game.pole[ii][jj].mine:
#                 n += 1
#     return n
#
#
# for i in range(N):
#     for j in range(N):
#         if not pole_game.pole[i][j].mine:
#             assert pole_game.pole[i][j].around_mines == get_around_mines(i,
#                                                                          j), f"неверное число мин вокруг клетки с индексами {i, j}"


# --------------------------------------------------------------------


# class DataBase:
#
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self, db_name, host, port, user, pwd):
#         self.db_name = db_name
#         self.pwd = pwd
#         self.user = user
#         self.port = port
#         self.host = host
#
#     def connect(self):
#         print(f"connect to db {self.db_name}, {self.user}, {self.port}, {self.pwd}")
#
#     def close(self):
#         print(f"close db {self.db_name}")
#
#     def read(self, *args):
#         print(f"read from {self.db_name} {args}")
#
#     def write(self, data):
#         print(f"write to {self.db_name} {data}")

# --------------------------------------------------------------------

# class SingletonFive:
#     __instance = []
#     __instance = __instance[:5]
#
#     def __new__(cls, *args, **kwargs):
#         cls.__instance.append(super().__new__(cls))
#         return cls.__instance[-1]
#
#     def __init__(self, name):
#         self.name = name
#
#
# objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять

# --------------------------------------------------------------------


# TYPE_OS = 1 # 1 - Windows; 2 - Linux
# 
# class DialogWindows:
#     name_class = "DialogWindows"
# 
# 
# class DialogLinux:
#     name_class = "DialogLinux"
# 
# class Dialog:
#     def __new__(cls, *args, **kwargs):
#         dlg = super().__new__(DialogWindows) if TYPE_OS == 1 else super().__new__(DialogLinux)
#         dlg.name = args[0]
#         return dlg
# 
# 
# dlg = Dialog("name")
# print(dlg)
# здесь объявляйте класс Dialog

# --------------------------------------------------------------------

# class Point:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#             return cls.__instance
#
#     def __init__(self, x, y):
#         self.y = y
#         self.x = x
#
#     def clone(self):
#         return self.__instance
#
#
# pt = Point(1, 2)
# pt_clone = pt.clone()
# print(pt)
# print(pt_clone)

# --------------------------------------------------------------------

# class Factory:
#
#     def build_sequence(self):
#         return []
#
#     def build_number(self, string):
#         return float(string)
#
# class Loader:
#     def parse_format(self, string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
#
# # эти строчки не менять!
# ld = Loader()
# s = input()
# res = ld.parse_format(s, Factory())

# --------------------------------------------------------------------


# class Coord:
#     limit_min = 0
#     limit_max = 10
#
#     def __init__(self, x, y):
#         self.y = y if self.validate(y) else 0
#         self.x = x if self.validate(x) else 0
#
#     @classmethod
#     def validate(cls, arg):
#         return cls.limit_min <= arg <= cls.limit_max


# --------------------------------------------------------------------

# # Здесь объявляется класс Factory
#
# class Factory:
#     @staticmethod
#     def build_sequence():
#         return list
#
#     @staticmethod
#     def build_number(string):
#         return int(string)
#
# class Loader:
#     @staticmethod
#     def parse_format(string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
#
# # эти строчки не менять!
# res = Loader.parse_format("1, 2, 3, -5, 10", Factory)


# --------------------------------------------------------------------
# from string import ascii_lowercase, digits
#
#
# class TextInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     def __init__(self, name, size=10):
#         self.check_name(name)
#         self.size = size
#         self.name = name
#
#     def get_html(self):
#         return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
#
#     @classmethod
#     def check_name(cls, name):
#         for i in name:
#             if i not in cls.CHARS_CORRECT:
#                 raise ValueError("некорректное поле name")
#
#         if len(name) > 50 or len(name) < 3:
#             raise ValueError("некорректное поле name")
#
#
# class PasswordInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     def __init__(self, name, size=10):
#         self.check_name(name)
#         self.size = size
#         self.name = name
#
#     def get_html(self):
#         return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
#
#     @classmethod
#     def check_name(cls, name):
#         for i in name:
#             if i not in cls.CHARS_CORRECT:
#                 raise ValueError("некорректное поле name")
#
#         if len(name) > 50 or len(name) < 3:
#             raise ValueError("некорректное поле name")
#
#
# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login = lgn
#         self.password = psw
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
#
#
# # эти строчки не менять
# login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
# html = login.render_template()

# --------------------------------------------------------------------

# from string import ascii_lowercase, digits
#
#
# class CardCheck:
#     CHARS_FOR_NAME = ascii_lowercase.upper() + digits
#     def a(self):
#         print()
#
#     @staticmethod
#     def check_card_number(number):
#         if len(number.replace('-', '')) != 16:
#             return False
#         for i in number.split('-'):
#             if not i.isnumeric() or len(i) != 4:
#                 return False
#         return True
#
#     @staticmethod
#     def check_name(name):
#         result = name.split()
#         if len(result) != 2:
#             return False
#
#         return set(name.replace(' ', '')) < set(CardCheck.CHARS_FOR_NAME)

# --------------------------------------------------------------------
# 1.7!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Video:

    def __init__(self, name):
        self.name = self.create(name)

    def create(self, name):
        ...

    def play(self):
        print(f"воспроизведение видео {self.name}")


class YouTube:
    @classmethod
    def add_video(cls, video):
        ...

    @classmethod
    def play(cls, video_indx):
        ...


# --------------------------------------------------------------------


# class AppStore:
#
#     lst_app = {}
#
#     def add_application(self, app):
#         self.lst_app[app.name] = app.blocked
#
#     def remove_application(self, app):
#         self.lst_app.pop(app.name)
#
#     def block_application(self, app):
#         app.__setattr__('blocked', True)
#
#     def total_apps(self):
#         return len(self.lst_app)
#
#
# class Application:
#     def __init__(self, name, blocked=False):
#         self.blocked = blocked
#         self.name = name

# --------------------------------------------------------------------

# class Viber:
#
#     messages = []
#
#     @staticmethod
#     def add_message(msg):
#         Viber.messages.append([msg.__dict__['text'], msg.__dict__['fl_like']])
#
#     @staticmethod
#     def remove_message(msg):
#         Viber.messages.remove([msg.__dict__['text'], msg.__dict__['fl_like']])
#
#     @staticmethod
#     def set_like(msg):
#         msg.change()
#
#     @staticmethod
#     def show_last_message(count: int):
#         return ' '.join([i[0] for i in Viber.messages[-count:]])
#
#
#     @staticmethod
#     def total_messages():
#         return len(Viber.messages)
#
#
# class Message:
#     def __init__(self, text, fl_like=False):
#         self.text = text
#         self.fl_like = fl_like
#
#     def change(self):
#         self.fl_like = not self.fl_like
#         return self.fl_like


# --------------------------------------------------------------------


# class Server:
#     """для описания работы серверов в сети
#     Соответственно в объектах класса Server должны быть локальные свойства:
#     buffer - список принятых пакетов (изначально пустой);
#     ip - IP-адрес текущего сервера.
#     """
#
#     count = 0
#
#     def __new__(cls, *args, **kwargs):
#         cls.count += 1
#         return super().__new__(cls)
#
#     def __init__(self):
#         self.ip = self.count
#         self.buffer = []
#         self.connect = None
#
#     def send_data(self, data):
#         """для отправки информационного пакета data (объекта класса Data)
#         с указанным IP-адресом получателя (пакет отправляется роутеру и
#         сохраняется в его буфере - локальном свойстве buffer);
#         """
#         self.buffer.append([data.data, data.ip])
#
#     def get_data(self):
#         """возвращает список принятых пакетов (если ничего принято не было,
#         то возвращается пустой список) и очищает входной буфер;
#         """
#         res = self.buffer.copy()
#         self.buffer.clear()
#         return ' '.join(res)
#
#     def get_ip(self):
#         """возвращает свой IP-адрес.
#         """
#         return self.ip
#
#
# class Router:
#     """для описания работы роутеров в сети (в данной задаче полагается один роутер).
#     И одно обязательное локальное свойство (могут быть и другие свойства):
#     buffer - список для хранения принятых от серверов пакетов (объектов класса Data).
#     """
#
#     def __init__(self):
#         self.router = super().__new__(Router)
#         self.buffer = []
#         self.connect = None
#
#
#     def link(self, server):
#         """для присоединения сервера server (объекта класса Server) к роутеру
#         """
#         setattr(server, 'connect', self.router)
#         self.connect = server.get_ip()
#
#
#     def unlink(self, server):
#         """для отсоединения сервера server (объекта класса Server) от роутера
#         """
#         setattr(server, 'connect', None)
#         self.connect = None
#         # self.connect.remove({'router': self.router, 'ip': server.ip})
#
#     def send_data(self):
#         """для отправки всех пакетов (объектов класса Data) из буфера роутера
#         соответствующим серверам (после отправки буфер должен очищаться)
#         """
#         self.buffer.clear()
#
#
# class Data:
#     """для описания пакета информации
#     Наконец, объекты класса Data должны содержать, два следующих локальных свойства:
#     data - передаваемые данные (строка);
#     ip - IP-адрес назначения.
#     """
#
#     def __init__(self, data, ip):
#         self.data = data
#         self.ip = ip

# --------------------------------------------------------------------


# class Clock:
#     def __init__(self, times=0):
#         self.__time = times
#
#     def set_time(self, tm):
#         if self.__check_time(tm):
#             self.__time = tm
#
#     def get_time(self):
#         return self.__time
#
#     @classmethod
#     def __check_time(cls, tm):
#         return True if type(tm) is int and 0 <= tm <= 100000 else False

# --------------------------------------------------------------------

# class Money:
#     def __init__(self, money: int):
#         self.__money = money
#
#     def set_money(self, money: int) -> None:
#         if self.check_money(money):
#             self.__money = money
#
#     def get_money(self) -> int:
#         return self.__money
#
#     def add_money(self, mn) -> None:
#         self.set_money(self.__money + mn.get_money())
#
#     @classmethod
#     def check_money(cls, money) -> bool:
#         return True if type(money) is int and money >= 0 else False
# --------------------------------------------------------------------

# class Book:
#
#     def __init__(self, author: str, title: str, price: int):
#         self.__author = author
#         self.__title = title
#         self.__price = price
#
#     def set_title(self, title: str) -> None:
#         self.__title = title
#
#     def set_author(self, author: str) -> None:
#         self.__author = author
#
#     def set_price(self, price: int) -> None:
#         self.__price = price
#
#     def get_title(self) -> str:
#         return self.__title
#
#     def get_author(self) -> str:
#         return self.__author
#
#     def get_price(self) -> int:
#         return self.__price


# --------------------------------------------------------------------

# class Line:
#     def __init__(self, *args):
#         self.__x1, self.__y1, self.__x2, self.__y2 = args
#
#
#     def set_coords(self, x1, y1, x2, y2):
#         self.__x1, self.__y1, self.__x2, self.__y2 = x1, y1, x2, y2
#
#     def get_coords(self):
#         return self.__x1, self.__y1, self.__x2, self.__y2
#
#     def draw(self):
#         return ' '.join(map(str, self.get_coords()))


# --------------------------------------------------------------------

# class Person:
#     def __init__(self):
#         self.__name = property
#         self.__old = property
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.__old = old

class Car:
    def __init__(self):
        self.__model = property

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model if 2 <= len(model) <= 100 else self

# --------------------------------------------------------------------

