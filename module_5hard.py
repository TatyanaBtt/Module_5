class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

    def __str__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f'Вы успешно вошли с систему')
                break
        else:
            print(f'Пользователь не найден, зарегистрируйтесь')

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                break
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user


    def log_out(self):
        self.current_user = None

    def add(self, *videos: Video):
        for video in videos:
            for video_1 in self.videos:
                if video.title == video_1.title:
                    print(f'Видео с таким названием уже существует')
                    break
            else:
                self.videos.append(video)


    def get_videos(self, word: str):
        video_word = []
        for video in self.videos:
            if word.lower() in video.title.lower():
                video_word.append(video.title)
        return video_word

    def watch_video(self, title: str):
        import time
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if video.title.lower() == title.lower():
                if self.current_user.age < 18 and video.adult_mode:
                    print(f'Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for i in range(1, video.duration+1):
                        print(i, end=' ')
                        time.sleep(1)
                        video.time_now = i
                    video.time_now = 0
                    print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

