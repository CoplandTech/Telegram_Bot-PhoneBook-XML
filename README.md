# Телефонная книга организации

Этот проект предназначен для организации телефонной книги организации/учреждения.
Он включает в себя:
1. Чтение XML файла из GOOGLE CONTACT. [Проект](https://github.com/CoplandTech/GoogleCon)
2. Cоздания .xlsx файла
3. Передача данных в Telegram бота.

## Оглавление

- [Описание](#описание)
- [Требования](#требования)
- [Установка](#установка)
- [Использование](#использование)
- [Доработка](#доработка)

## Описание

Проект состоит из следующих основных компонентов:

1. **Чтенеи XML файла**: Чтение XML файла в соответствии с разметкой телефонной книги Yealink из [GOOGLE CONTACT](https://github.com/CoplandTech/GoogleCon).
2. **Генерация .xlsx файла**: Извлечение данных из XML файла и создание .xlsx файла в соответствии со структурой подразделений.
3. **Интеграция с Telegram ботом**: Передача данных из XML файла в Telegram бот для удобного и быстрого доступа.
   
**О боте**: В Telegram боте реализован функционал:
1. Модерация пользователей Telegram.
2. Функциональные кнопки: "Открыть чат", "Телефонная книга".

## Требования

- Разработка и тестирование проводилось только на Python 3.10
- Библиотеки: Указаны в файле [requirements.txt](https://github.com/CoplandTech/phonebook_tg_bot/blob/main/requirements.txt)

## Установка

1. Клонируйте/скачайте репозиторий:

    ```sh
    git clone https://github.com/CoplandTech/phonebook_tg_bot.git
    ```

2. (ОПЦИОНАЛЬНО) Воспользуйтесь [небольшой инструкцией](https://github.com/CoplandTech/python_bots_service) для установки ботов в качестве сервиса. [Инструкция](https://github.com/CoplandTech/python_bots_service) так же будет полезна для установки нескольких ботов на одной машине. 

3. Установите необходимые зависимости и запустите скрипт:

    ```sh
    pip install -r requirements.txt
    ```
    ```sh
    python3 main.py
    ```

## Использование

1. **Формирование/создание XML файла**:
   Вручную создайте, воспользуйтесь формированием XML файла из [GOOGLE CONTACT](https://github.com/CoplandTech/GoogleCon) или воспользуйтесь XML файлом [из репозитория](https://github.com/CoplandTech/phonebook_tg_bot/blob/main/contacts.xml).
**Структура файла**:

  ```XML
  <?xml version='1.0' encoding='utf-8'?>
  <YealinkIPPhoneBook>
    <Title>Yealink</Title>
    <Menu Name="DEP_1" Number="+7 (9999) 999-999">
    <Unit Name="John Doe" Middle="A" Phone1="111" Phone2="+7 (999) 234-5678" Phone3="+7 (999) 345-6789" Email="john.doe@example.com" JobTitle="Manager" default_photo="Resource:"/>
    <Unit Name="Jane Smith" Middle="B" Phone1="123" Phone2="+7 (999) 876-5432" Phone3="" Email="jane.smith@example.com" JobTitle="Developer" default_photo="Resource:"/>
    <Unit Name="Alice Johnson" Middle="C" Phone1="134" Phone2="+7 (999) 567-8901" Phone3="+7 (999) 678-9012" Email="alice.johnson@example.com" JobTitle="Designer" default_photo="Resource:"/>
    </Menu>
    <Menu Name="DEP_2" Number="+7 (0000) 000-000">
    <Unit Name="Bob Brown" Middle="D" Phone1="001" Phone2="+7 (000) 234-5678" Phone3="+7 (000) 345-6789" Email="bob.brown@example.com" JobTitle="Analyst" default_photo="Resource:"/>
    <Unit Name="Charlie Davis" Middle="E" Phone1="002" Phone2="+7 (000) 876-5432" Phone3="+7 (000) 765-4321" Email="charlie.davis@example.com" JobTitle="Consultant" default_photo="Resource:"/>
    <Unit Name="Diana Evans" Middle="F" Phone1="003" Phone2="+7 (000) 567-8901" Phone3="+7 (000) 678-9012" Email="diana.evans@example.com" JobTitle="HR" default_photo="Resource:"/>
    <Unit Name="Evan Foster" Middle="G" Phone1="004" Phone2="+7 (000) 432-7658" Phone3="+7 (000) 543-8769" Email="evan.foster@example.com" JobTitle="Support" default_photo="Resource:"/>
    <Unit Name="Fiona Green" Middle="H" Phone1="005" Phone2="+7 (000) 765-4321" Phone3="+7 (000) 876-5432" Email="fiona.green@example.com" JobTitle="Marketing" default_photo="Resource:"/>
    <Unit Name="George Harris" Middle="I" Phone1="006" Phone2="+7 (000) 890-1234" Phone3="+7 (000) 901-2345" Email="george.harris@example.com" JobTitle="Sales" default_photo="Resource:"/>
    </Menu>
  </YealinkIPPhoneBook>
  ```
После получения готового файла, опубликуйте его или загрузите на сервер. Далее путь к файлу требуется указать в [config.py](https://github.com/CoplandTech/phonebook_tg_bot/blob/main/bot/inc/config.py)

2. **Конфигурация скрипта**:
  Укажите необходимые данные в в [config.py](https://github.com/CoplandTech/phonebook_tg_bot/blob/main/bot/inc/config.py)
    ```python
    TOKEN_API = "TOKEN" # API бота
    LIST_ADMIN_ID = ['ID_1','ID_1']  # ID администратора
    OUTPUT_CHAT = 'URL' # ссылка на чат, куда пойдут пользователи
    RETRY_INTERVAL_DAYS = 7
    
    URL_XML = 'URL.xml'
    PATH_XLSX_FILE = 'bot/inc/phonebook.xlsx'
    
    PHRASES = {
        'start': 'Начать работу или вернуться к началу',
        'admin_panel': 'Администрирование',
        'login_admin': 'Вы авторизованы как администратор',
        'access_error': 'У вас нет доступа!',
        'access_approved': 'Проснись уже, самурай. Время сжечь этот город...',
        'request_processing': 'Ваша заявка ещё в обработке.\nОжидайте или поторопите нас!',
        'select_next': 'Выберите действие:',
        'enter_full_name': 'Введите своё полное ФИО',
        'hello_message': 'Телеграм бот компании.\nПройдите модерацию для продолжения...',
        'oops': 'Кажется вы забыли отчество...или ещё чего хуже...',
        'dooble_fisrt_name': 'Двойную фамилию укажите через "-", и не пишите автобиографию, ради бога...',
        'min_words': 'Каждое слово должно содержать минимум 2 буквы.'
    }
    ```
- TOKEN_API - Токен телеграм бота полученный в [BotFather](https://t.me/BotFather).
- LIST_ADMIN_ID - Список ID администраторов телеграм бота.
- OUTPUT_CHAT - Ссылка на чат.
- RETRY_INTERVAL_DAYS - Задержка в днях для возможности подать повторную заявку для отклонённого пользователя при модерации.
- URL_XML - Ссылка или путь к файлу XML с разметкой телефонной книги Yealink.
- PATH_XLSX_FILE - Путь для сохранения сгенерированного .xlsx файла.
- PHRASES - Список фраз. (В ДОРАБОТКЕ)

## Доработка

- [ ] Скрыть для простых юзеров функции админа
- [ ] Написать перемодерацию заявок и их удаление
- [ ] Написать функционал для репортов об ошибках.
