class BotMessage:
    START = "Добрый день.\n\n прикрепите AINSYS Вебхук."
    MAIN_INSTRUCTION = f"Инструкция по использованию бота. Вы можете \n\n- Создать сущность /add_entity \n" \
                       f"- Показать все сущности /get_entities \n"
    WEBHOOK = "Ваш вебхук: "
    ADD_ENTITY_INSTRUCTION = f"Введите название вашей сущности в формате, например - \nСущность: New"
    ADD_FIELD_INSTRUCTION = f"Введите название вашего поля и тип данных в формате, например - \n\n" \
                            f"ID_сущности: 2\n" \
                            f"Поле: name\n" \
                            f"Тип: string\n\n"
    ADD_FIELD_INSTRUCTION_SECOND = f"Можете добавить поле или отправить сущность в AINSYS"
    ID_ENTITY = f"ID_сущности:"
    USER = 'Ваш ID:'
    ENTITIES = f"\nВаши Сущности:\n"
    FIELD = 'Поле:'
    TYPE = 'Тип:'
    CHOOSE_ENTITY = 'Выберете ту сущность с которой будете работать'
    HELP = 'Все команды бота:' \
           '\n/start - запуск бота/регистрация пользователя' \
           '\n/add_entity - добавление новой сущности' \
           '\n/get_entities - получение всех текущих сущностей' \
           '\n/update_data - отправка данных' \
           '\n/help - вызов меню с компандами'




class BotCommand:
    START = 'start'
    ADD_ENTITY = 'add_entity'
    GET_ENTITIES = 'get_entities'
    UPDATE_DATA = 'update_data'
    HELP = 'help'


class BotContentTypes:
    TEXT = 'text'


class ParcePhrase:
    FORMAT_URL = 'https'
    ENTITY = "Сущность"
    FIELD = 'Поле'
    CREATE_ENTITY = "Отправить сущность"


class ButtonCommand:
    ADD_ENTITY = "Отправить сущность: "


class NameHandlerRequest:
    ADD_ENTITY = "add_entity"
