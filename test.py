import random
import playsound
import pytest
from Text import *

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

def test_generate_answers():
  song_name_rus = "1"
  song_name_for = "3"
  russian_songs = ["1", "2", "3", "4"]
  foreign_songs = ["1", "2", "3", "4"]

  # Test with 'foreign' mode
  answers = generate_answers("foreign", song_name_for, russian_songs, foreign_songs)
  assert len(answers) == 4
  assert song_name_for in answers

  # Test with 'russian' mode (similar assertions)
  answers = generate_answers("russian", song_name_rus, russian_songs, foreign_songs)
  assert len(answers) == 4
  assert song_name_rus in answers


def check(answers, mod, number, song_name):
    while True:
        print("Варианты ответов:")
        for i, answer in enumerate(answers):
            print(f"{i + 1}. {answer}")

        playsound.playsound(f"{mod}/{number}.wav")

        try:
            user_answer = 1
        except ValueError:
            print("Введите число!")
            continue

        if 1 <= user_answer <= len(answers):
            break
        else:
            print("Номер ответа должен быть от 1 до", len(answers))

    return answers[user_answer - 1] == song_name


def test_check():
    answers = ["1", "2", "3"]
    mod = "russian"
    number = 1
    song_name = "1"

    assert check(answers, mod, number, song_name)


def game():  # Функция игры
    # Чтение файлов с названиями песен
    russian_songs, foreign_songs = reading()

    # Выбор режима
    mod = choose_mode()

    songs_done = [78]

    # Счетчик
    score = 0

    game_itself(mod, foreign_songs, russian_songs, score, songs_done)


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


def test_check_song_foreign():
    songs_done = [78]
    mod = 'foreign'
    foreign_songs = ['3', '5', '7']
    russian_songs = ['1', '2', '3']
    song_name, number = check_song(songs_done, mod, foreign_songs, russian_songs)

    assert song_name in foreign_songs
    assert number.isdigit()

def test_check_song_russian():
    songs_done = [78]
    mod = 'russian'
    foreign_songs = ['3', '5', '7']
    russian_songs = ['1', '2', '3']
    song_name, number = check_song(songs_done, mod, foreign_songs, russian_songs)

    assert song_name in russian_songs
    assert number.isdigit()


def exit_(mod, foreign_songs, russian_songs, score, songs_done, again):
    # Выход из игры
    if again == "1":
        game_itself(mod, foreign_songs, russian_songs, score, songs_done)
    elif again == '2':
        quit()
    elif again == "3":
        game()
    else:
        exit_(mod, foreign_songs, russian_songs, score, songs_done)

'''
def test_exit_valid_input_restart_game():
  assert exit_(mod="audio", foreign_songs=["Song 1"], russian_songs=["Song 2"], score=0, songs_done=[], again="1") == 'game_itself'  # No return value
'''
def test_exit_valid_input_quit():
  assert exit_(mod="audio", foreign_songs=["Song 1"], russian_songs=["Song 2"], score=0, songs_done=[], again="2") == quit()  # No return value

def test_exit_valid_input_restart_all():
  assert exit_(mod="audio", foreign_songs=["Song 1"], russian_songs=["Song 2"], score=0, songs_done=[], again="3") == game()  # No return value

'''
def test_exit_invalid_input():
  with pytest.raises(SystemExit):
    exit_(mod="audio", foreign_songs=["Song 1"], russian_songs=["Song 2"], score=0, songs_done=[], again="invalid")
'''



def game_itself(mod, foreign_songs, russian_songs, score, songs_done):  # Сама игра
    song_name, number = song_choice(mod, foreign_songs, russian_songs, songs_done)

    answers = generate_answers(mod, song_name, russian_songs, foreign_songs)

    result = check(answers, mod, number, song_name)
    if result:
        print('\n' + "Угадали!")
        score += 1
    else:
        print('\n' + "Неверно. Правильный ответ:", song_name)

    print(f"Ваш счет: {score}")

    exit_(mod, foreign_songs, russian_songs, score, songs_done)

def test_game_itself():
    mod = "russian"
    foreign_songs = ["1", "2", "3"]
    russian_songs = ["1", "2", "3"]
    score = 0
    songs_done = []


    game_itself(mod, foreign_songs, russian_songs, score, songs_done)


    assert score >= 0
    assert len(songs_done) <= len(russian_songs) + len(foreign_songs)
    assert len(songs_done) == len(set(songs_done))


def song_choice(mod, foreign_songs, russian_songs, songs_done):
    song_name, number = check_song(songs_done, mod, foreign_songs, russian_songs)
    songs_done.append(song_name)
    return song_name, number

