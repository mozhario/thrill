def filter_entities_by_type(entities, type):
    entities = list(filter(
        lambda x: getattr(x, 'type', None) == type,
        entities
    ))
    return entities