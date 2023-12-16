import random


def random_string():
    random_list = [
        "Por favor, descreva sua pergunta um pouco mais.",
        "Desculpa, não entendi. poderia repetir, por favor?",
        "Acho que ainda não sei responder isso..."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
