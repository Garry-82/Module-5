import time

class User:
    """
    класс Пользователь, содержит атрибуты: Имя, пароль, возраст
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self. password = password
        self.age = age

    def print(self, users): # - метод для вывода информации о пользователях, в виде списка, на экран!
        str1 = []
        for i in users:
            str1.append({i.nickname: [i.password, i.age]})
        print(str1)
class Video:
    time_now = 0
    adult_mode = False
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
class UrTube:
    """
    класс UrTube содержит атрибуты: список объектов User, список объектов Video, текущий пользователь current_user
    """
    current_user = None
    def __init__(self, users, videos):
        self.users = users
        self.videos = videos
    def log_in(self, login, password):  #  -  вход в учетную запись

        for i in range(len(self.users)):
            if login not in self.users[i].nickname:
                continue
            else:
                if hash(password) == hash(self.users[i].password):  # - сравниваем пароли по Hash!!!
                    UrTube.current_user = self.users[i]
                    return True  # - полное совпадение по имени и паролю!!!

    def register(self, nickname, password, age):  #  -  регистрация нового пользователя
        while True:
            for i in range(len(self.users)):
                if nickname in self.users[i].nickname:
                    print(f"Имя пользователя __{nickname}__ уже занято!!!")
                    return False
            U = User(nickname, password, age)
            users.append(U)
            UrTube.current_user = self.users[i+1]
            print("!!! Добавляем нового пользователя!!!")
            return
    def log_out(self):  #  -  выход из текущей учетной записи
        UrTube.current_user = None

    def print_users(self): # - вывод информации о пользователях, в виде списка, на экран!
        str1 = []
        for i in self.users:
            str1.append({i.nickname: [i.password, i.age]})
        print(*str1)

    def print_videos(self):  # - вывод информации о видео, в виде списка, на экран!
        str2 = []
        for i in self.videos:
            str2.append({i.title: i.duration})
        print(*str2)
    def add_video(self, *Video):  #  -  добавление новых видео в список
        for j in Video:
            for i in range(len(self.videos)):
                if j.title in self.videos[i].title:
                    print("Такой фильм уже есть!!")
                    return
            videos.append(j)

    def get_videos(self, find_name):  #  - поиск всех видео по заданным фрагментам
        j = 0  # - счетчик совпадений фрагмента в названиях фильмов
        find_videos = []  # - список всех видео, где содержится искомый фрагмент текста
        while True:
            for i in range(len(self.videos)):
                if find_name.upper() in str(self.videos[i].title).upper():
                    find_videos.append(self.videos[i].title)
                    j += 1
            if j == 0:
                print("Фильмы с подобными названиями отсутствуют!!")
            else:
                print(f"список фильмов, где встречается искомый фрагмент: \n{find_videos}")
            return
    def watch_video(self, name_film):  #  -  поиск нужного фильма для просмотра
        for i in videos:
            if name_film.upper() in i.title.upper():
                if ur.current_user == None:
                    print("Вы не вошли в аккаунт")
                else:
                    if int(ur.current_user.age) < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        print(f"Запускаем просмотр фильма: {i.title}")
                        for i in range(int(i.duration)):
                            time.sleep(1)
                            print(i+1)
                        print("---!!!Конец видео!!!---")





videos = []  # - список объектов видео
users = []  # - список объектов пользователей


U1 = User("Игорь", "1234", "35")
users.append(U1)
U2 = User("Макс", "234", "15")
users.append(U2)

ur = UrTube(users, videos)
V1 = Video("Лучший язык програмирования 2024 года", 30)
V2 = Video("Для чего девушкам парень программист?",10)
V3 = Video("Матрица", 15)
V4 = Video("XXX", 20)
V5 = Video("Для чего девушкам парень программист?",40)
V4.adult_mode = True
V2.adult_mode = True
videos.append(V1)
videos.append(V2)

if __name__ == "__main__":
    print('Добро пожаловать на платформу "Свой YouTube"!!! ')
    print(f"---текущий список пользователей: ---")
#    U1.print(users)
    ur.print_users()
    print(f"---Текущий список видео: ---")
    ur.print_videos()
    while True:
        print("\n-------------- ГЛАВНОЕ МЕНЮ -------------------- \n1 - Войти в учетную запись \n2 - Зарегистрироваться\n"
                           "3 - Найти фильмы по фрагменту названия \n4 - выйти из приложения")
        choice = int(input("Введите номер действия: "))
        if choice == 1:  #  -  попытка входа в учетную запить
            print(nickname1 := input("Введите Имя: "), password1 := input("Введите пароль: "))
            if ur.log_in(nickname1, password1) == True:
                print("\n---Текущий пользователь: ___", ur.current_user.nickname,"___!!!---")
                while ur.current_user != None:
                    print("\n1 - добавить новый фильм в список \n2 "
                                       "- найти фильм по названию (для просмотра) \n3 - Найти фильмы по фрагменту "
                                        "названия\n4 - Выйти из текущего аккаунта\n5 - выйти из приложения\n")
                    choice2 = int(input("Выбери, что нужно сделать: "))
                    if choice2 == 1:
                        ur.add_video(V3, V4, V5)
                        print(f"Текущий список видео: ")
                        ur.print_videos()
                    elif choice2 == 2:
                        ur.watch_video(input("введите точное название фильма для просмотра: "))
                    elif choice2 == 3:
                        ur.get_videos(input("Напишите фрагмент названия для поиска подходящих фильмов в нашем списке:"))
                    elif choice2 == 4:
                        ur.log_out()
                    else:
                        exit()
            else:
                print("Такой пользователь не найден!!")
        elif choice == 2:  # - регистрация нового пользователя!
            user = User(input("Введите Имя: "), input("Введите пароль: "), input("введите ваш возраст: "))
            ur.register(user.nickname, user.password, user.age)
            print("текущий список пользователей:")
            ur.print_users()
            print("\n---Текущий пользователь: !!!___", ur.current_user.nickname,"___!!!---")
            while ur.current_user != None:
                print("1 - добавить новый фильм в список \n2 "
                                       "- найти фильм по названию (для просмотра) \n3 - Найти фильмы по фрагменту "
                                        "названия\n4 - Выйти из текущего аккаунта\n5 - выйти из приложения")
                choice2 = int(input("Выбери, что нужно сделать: "))
                if choice2 == 1:
                    ur.add_video(V3, V4, V5)
                    print("Текущий список видео: ")
                    ur.print_videos()
                elif choice2 == 2:
                    ur.watch_video(name_film=input("введите точное название фильма для просмотра: "))
                elif choice2 == 3:
                    ur.get_videos(input("Напишите фрагмент названия для поиска подходящих фильмов в нашем списке: "))
                elif choice2 == 4:
                    ur.log_out()
                else:
                    exit()
        elif choice == 3:
            ur.get_videos(input("Напишите фрагмент названия для поиска подходящих фильмов в нашем списке: "))
        elif choice == 4:
            print("До новых встреч!!!")
            exit()
