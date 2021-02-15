import services
import exceptions


def get_or_create_state(game_ID: str):
    try:
        return services.get_state(game_ID)
    except exceptions.GameNotFoundError:
        return services.create_game(game_ID)


def check_turn(game_ID, team, action, payload):
    state = services.get_state(game_ID)
    if state["playerState"]["winner"] != "none":
        raise exceptions.WrongTurnError("Game Over!")
    if f"{team}-{action}" != state["playerState"]["turn"]:
        raise exceptions.WrongTurnError("Wrong Action!")

    return services.handle_turn(game_ID, team, action, payload)
