import random
var = ['Бесспорно',
       'Мне кажется - да',
       'Пока неясно, попробуй снова',
       'Даже не думай',
       'Предрешено',
       'Вероятнее всего',
       'Спроси позже',
       'Мой ответ - нет',
       'Никаких сомнений',
       'Хорошие перспективы',
       'Лучше не рассказывать',
       'По моим данным - нет',
       'Определённо да',
       'Знаки говорят - да',
       'Сейчас нельзя предсказать',
       'Перспективы не очень хорошие',
       'Можешь быть уверен в этом',
       'Да', 'Сконцентрируйся и спроси опять',
       'Весьма сомнительно'
       ]
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как тебя зовут? ')
print('Привет,', name.title())
def question():
    question = input('Задайте вопрос:')
    print(random.choice(var))
question()
while True:
       new_question = input('Хотите задать еще вопрос? (да или нет) ')
       if new_question.lower() == 'да' or new_question.lower() == 'yes':
              question()
       else:
              print('Возвращайся если возникнут вопросы!')
              break