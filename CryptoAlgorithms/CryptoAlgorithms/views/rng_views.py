from django.shortcuts import render, redirect
from CryptoAlgorithms.algorithms.RNG import RNG
from django.core.cache import cache
from CryptoAlgorithms.models.ApplicationState import ApplicationState

def index(request):
    state: ApplicationState | None = cache.get("state")
    return render(request, "index.html", context = {"state": state})

def create_generator(request):
    generator = RNG()
    cache.set("state", ApplicationState(generator), timeout=100000)
    return redirect("/")

def generate_number(request):
    state: ApplicationState | None = cache.get("state")
    if not state:
        return redirect("/generator/create")
    state.generate_number()
    cache.set("state", state, timeout=100000)
    return redirect("/")

def get_chart(request):
    pass

# TODO: сверстать главную страницу, добавить график при генерации последовательности, сохранение ключа в файл, сохранение чисел в файл

