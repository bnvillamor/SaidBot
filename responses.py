import random


def handle_response(message) -> str:
    pmsg = message.lower()
    if pmsg == 'hi':
        return 'Hello friend!'

    if pmsg == 'roll':
        return str(random.randint(1, 6))

    if pmsg == '!help':
        return '`maybe later`'
