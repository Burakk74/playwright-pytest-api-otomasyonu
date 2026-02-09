USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "address": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            }
        }
    },
    "required": ["id", "name", "email"]
}

CREATE_POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "number"}
    },
    "required": ["id", "title", "body", "userId"]
}