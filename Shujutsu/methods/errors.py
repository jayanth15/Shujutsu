def format(msg, type, fun):
    data = {
        "detail": [
            {
            "loc": [
                "body",
                fun
            ],
            "msg": msg,
            "type": type
            }
        ]
    }
    return data
