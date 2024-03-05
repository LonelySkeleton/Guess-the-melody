import random
import playsound
from Text import *


def game():  # Функция игры
    # Чтение файлов с названиями песен
    russian_songs, foreign_songs = reading()

    # Выбор режима
    mod = choose_mode()

    songs_done = [78]

    # Счетчик
    score = 0

    game_itself(mod, foreign_songs, russian_songs, score, songs_done)


def generate_answers(mod, song_name, russian_songs, foreign_songs):  # Функция генерации вариантов ответа
    answers = [song_name]
    while len(answers) < 4:
        if mod == 'foreign':
            random_song = random.choice(list(foreign_songs))
            if random_song not in answers:
                answers.append(random_song)
        if mod == 'russian':
            random_song = random.choice(list(russian_songs))
            if random_song not in answers:
                answers.append(random_song)
    random.shuffle(answers)
    return answers


def check(answers, mod, number, song_name):  # Процесс проверки
    while True:
        # Отображение вариантов ответа
        print('Варианты ответов:')
        for i, answer in enumerate(answers):
            print(f"{i + 1}. {answer}")

        # Воспроизведение мелодии
        playsound.playsound(f"{mod}/{number}.wav")

        # Ввод ответа пользователя
        user_answer = int(input('\n' + "Введите номер ответа: "))

        # Проверка ответа
        if answers[user_answer - 1] == song_name:
            return True
        else:
            return False


def song_choice(mod, foreign_songs, russian_songs, songs_done):
    song_name, number = check_song(songs_done, mod, foreign_songs, russian_songs)
    songs_done.append(song_name)
    return song_name, number


def check_song(songs_done, mod, foreign_songs, russian_songs):
    song_name, number = 78, ''
    if mod == 'foreign':
        while song_name in songs_done:
            song_name = random.choice(foreign_songs)
            number = str(foreign_songs.index(song_name) + 1)
    elif mod == 'russian':
        while song_name in songs_done:
            song_name = random.choice(russian_songs)
            number = str(russian_songs.index(song_name) + 1)
    return song_name, number


def exit_(mod, foreign_songs, russian_songs, score, songs_done):
    # Выход из игры
    again = input("Хотите продолжить? (да - 1, нет - 2, смена режима - 3): " + '\n')
    if again == "1":
        game_itself(mod, foreign_songs, russian_songs, score, songs_done)
    elif again == '2':
        quit()
    elif again == "3":
        game()
    else:
        exit_(mod, foreign_songs, russian_songs, score, songs_done)


def game_itself(mod, foreign_songs, russian_songs, score, songs_done):  # Сама игра
    # Выбор песни
    song_name, number = song_choice(mod, foreign_songs, russian_songs, songs_done)

    # Генерация вариантов ответа
    answers = generate_answers(mod, song_name, russian_songs, foreign_songs)

    result = check(answers, mod, number, song_name)
    if result:
        print('\n' + "Угадали!")
        score += 1
    else:
        print('\n' + "Неверно. Правильный ответ:", song_name)

    # Отображение счета
    print(f"Ваш счет: {score}")

    exit_(mod, foreign_songs, russian_songs, score, songs_done)
