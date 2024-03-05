def instructions():  # Инструкции
    print('=========================', 'Добро пожаловать в игру "Угадай мелодию"!',
          "Вам необходимо выбрать режим: русские песни или иностранные песни",
          "После начнется игра",
          "Песня играет 10 секунд, затем вам неодходимо выбрать вариант ответа, когда появится поле для ответа",
          "Если вы ответите правильно - получите 1 балл",
          "\nУдачной игры!", '=========================', "\n", sep='\n')


def reading():  # Чтение песен
    # Чтение названий русских песен
    russian_songs = []
    with open("russian songs.txt", "r", encoding='UTF-8') as f:
        for line in f:
            russian_songs.append(line.strip())

    # Чтение названий иностранных песен
    foreign_songs = []
    with open("foreign songs.txt", "r", encoding='UTF-8') as f:
        for line in f:
            foreign_songs.append(line.strip())

    return russian_songs, foreign_songs


def choose_mode():  # Выбор режима
    print("Выберите режим  (напишите цифру):",  "русские песни - 1", "иностранные песни - 2", sep='\n')
    mod = input()
    if mod != '1' and mod != '2':
        print("Неверный ввод")
        choose_mode()
    if mod == '1':
        mod = 'russian'
    else:
        mod = 'foreign'

    return mod
