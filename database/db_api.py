from database.models import Users, BaseModel, Entities, Fields
from database import session


def get_users(name): return session.query(Users).filter_by(name=name).first()


def add_user(user_id, chat_id, ainsys_webhook):
    obj = Users(
        user_id=user_id,
        chat_id=chat_id,
        ainsys_webhook=ainsys_webhook,
    )
    session.add(obj)
    session.commit()
    return obj


def add_entity(entity, user_id, chat_id):
    obj = Entities(
        entity=entity,
        user_id=user_id,
        chat_id=chat_id,
    )
    session.add(obj)
    session.commit()
    return obj


def add_field(entity_id, field, type_field, chat_id, user_id):
    obj = Fields(
        field=field,
        entity_id=entity_id,
        user_id=user_id,
        chat_id=chat_id,
        type_field=type_field,
    )
    session.add(obj)
    session.commit()
    return obj


def get_entity_id(entity_name):
    entities_info = session.query(Entities.id, Entities.entity).all()

    for entity in entities_info:
        if entity.entity == entity_name:
            return entity.id


def get_entities(user_id):
    entities_info = session.query(Entities).filter(Entities.user_id == str(user_id)).all()
    entities = [entity.entity for entity in entities_info]

    return entities


def get_fields(entity_id):
    fields_info = session.query(Fields).filter(Fields.entity_id == str(entity_id)).all()

    fields = {}
    for field in fields_info:
        fields[field.field] = field.field

    return fields


def get_webhook(entity_id):
    entities_info = session.query(Entities).filter(Entities.id == entity_id)
    user_id = entities_info[0].user_id

    users_info = session.query(Users).filter(Users.user_id == user_id)
    webhook = users_info[0].ainsys_webhook

    return webhook


def get_entity_name(entity_id):
    entities_info = session.query(Entities).filter(Entities.id == entity_id)
    name_entity = entities_info[0].entity

    return name_entity
