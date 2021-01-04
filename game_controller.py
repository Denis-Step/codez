import redis_services as services
import exceptions


def get_or_create_state(game_ID: str):
    try:
        services.get_state(game_ID)
    except exceptions.GameNotFoundError:
        return services.create_game(game_ID)


def handle_turn(game_ID, team, action, payload):
    pass