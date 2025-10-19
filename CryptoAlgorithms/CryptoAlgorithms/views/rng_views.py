import json
import datetime
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from CryptoAlgorithms.algorithms.RNG import RNG
from CryptoAlgorithms.models.ApplicationState import ApplicationState
from CryptoAlgorithms.cache_wrapping_functions import get_state, update_state
from CryptoAlgorithms.algorithms.RNGEncryptor import RNGEncryptor
from CryptoAlgorithms.models.distribution_calculation_functions import get_labels, get_distribution, \
    get_default_distribution


def index(request):
    state: ApplicationState | None = get_state()
    return render(request, "index.html", context = {"state": state})

def create_generator(request):
    generator = RNG()
    update_state(ApplicationState(generator))
    return redirect("/")

def generate_number(request):
    state: ApplicationState | None = get_state()
    if not state:
        return redirect("/generator/create")
    state.generate_number()
    update_state(state)
    return redirect("/")

def load_key(request):
    if request.method != "POST" and "key" not in request.FILES:
        return redirect("/")

    uploaded_file = request.FILES["key"]

    if not uploaded_file.name.endswith(".key"):
        return redirect("/")

    content = uploaded_file.read().decode("utf-8")
    state = json.loads(content)

    loaded_rng = RNG.load_from_params(state["a"], state["b"], state["c_0"])
    update_state(ApplicationState(loaded_rng))
    return redirect("/")

def save_key(request):
    state: ApplicationState | None = get_state()

    if not state:
        return redirect("/")

    values = {"a": state.generator.a, "b": state.generator.b, "c_0": state.generator.c_0}
    response = HttpResponse(json.dumps(values), content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="generator.key"'
    return response

def generate_sequence(request):
    state: ApplicationState | None = get_state()
    if not state:
        return redirect("/")

    numbers_count = int(request.GET.get("count", 10))
    state.generate_sequence(numbers_count)
    update_state(state)

    return redirect("/")

def download_sequence(request):
    state: ApplicationState | None = get_state()
    if not state:
        return redirect("/")

    response = HttpResponse("\n".join(str(num) for num in state.sequence), content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="sequence.txt"'
    return response

def get_chart(request):

    state: ApplicationState | None = get_state()

    if not state or len(state.sequence) == 0:
        return JsonResponse({
            "data": get_default_distribution(),
            "labels": get_labels()
        })

    return JsonResponse({"data": get_distribution(state.sequence), "labels": get_labels()})

def execute_encryption(request):

    if request.method != "POST" or "origin" not in request.FILES:
        return redirect("/")

    uploaded_file = request.FILES["origin"]

    # Read as raw bytes (works for both text and encrypted files)
    content_bytes = uploaded_file.read()
    
    # Try to decode as UTF-8 text, if it fails, it's already encrypted bytes
    try:
        content = content_bytes.decode("utf-8")
    except UnicodeDecodeError:
        # File is already encrypted (binary), use it directly
        content = content_bytes

    state: ApplicationState | None = get_state()

    if not state:
        return redirect("/")

    time_now = datetime.datetime.now()

    encrypted = RNGEncryptor(state.generator).encrypt_text(content)

    spent_time = (datetime.datetime.now() - time_now).total_seconds()

    state.update_time(spent_time)
    state.encrypted_bytes = encrypted

    update_state(state)

    return redirect("/")

def download_encrypted_text(request):
    state: ApplicationState | None = get_state()

    if not state:
        return redirect("/")

    response = HttpResponse(state.encrypted_bytes, content_type='text/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="encrypted.txt"'
    return response