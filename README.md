
# Планировщик мероприятий

Для организации учебного мероприятия/встречи необходимо найти время и место, которое будет удобно
всем (или, в определенных случаях, некоторым из списка) заинтересованным участникам. Для
этого нужно учитывать расписание (или несколько расписаний) каждого участника, желаемое место
встречи, требования нормативных актов. Приходится одновременно открывать несколько расписаний и искать там совпадающие свободные окна, держать в голове разного рода ограничения. 

Цель данного тула упростить планирование встреч. Идея в том, чтобы сделать приложение, в котором можно будет выбрать участников (преподавателей, групп), желаемое место встречи (факультет, аудитории), тип мероприятия и посмотреть на одной странице все необходимые данные.

На данный момент реализовано ядро приложения, куда можно добавить реализации всех необходимых мероприятий с их особенностями.

## Структура репозитория
```bash
.
├── README.md - основная информация о проекте
├── pyproject.toml - конфигурационный файл
├── .pre-commit-config.yaml - настройки линтера
├── example.env - пример файла с переменными окружения
├── requirements.txt - зависимости приложения
├── config.py - получение и валидация переменных окружения
└── src
    └── core
        ├── events - реализации разных типов мероприятий (разовая встреча, регулярная встреча, ...)
        ├── event_options - опции мероприятий (очно/онлайн, ...)
        ├── members - участники мероприятий (преподаватель, группа, ...)
        ├── schedules - представления календарей (timetable, ...) и реализация их получения с внешних ресурсов
        └── types - типы используемых объектов (участников, календарей, событий, ...)
```

## Установка и запуск

#### Timetable API
Предварительно нужно запустить [приложение для скрейпинга timetable](https://github.com/Anton-Kraev/timetable-database).

#### Требования
Python 3.12+

#### Переменные окружения
Необходимо создать файл .env в корне проекта, опираясь на [example.env](example.env).

#### Установка зависимостей
```
pip install -r requirements.txt
```

#### Установка и запуск линтера
```
pip install pre-commit
pre-commit install
pre-commit run --all-files
```
