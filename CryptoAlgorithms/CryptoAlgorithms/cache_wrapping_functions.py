from django.core.cache import cache
from CryptoAlgorithms.models.ApplicationState import ApplicationState

# Функция для сохранения состояния в кэш
def get_state() -> ApplicationState | None:
    return cache.get("state")

# Функция для обновления состояния в кэше
def update_state(state: ApplicationState):
    cache.set("state", state, timeout=100000)