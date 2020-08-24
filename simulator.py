import random
import json
from copy import copy

# カードデータのパス
CARD_LIST_PATH = "./card_list.json"


def get_card_list():
    with open(CARD_LIST_PATH, encoding="utf-8") as f:
        cards = json.load(f)
    for key in cards.keys():
        for card in cards[key]:
            card.setdefault("isFoil", False)
    return cards


def pick_mr(m: list, r: list) -> list:
    # 神話レアのカードはレアの1/8の確率で出現する
    if random.randint(1, 8) == 1:
        return [copy(random.choice(m))]
    else:
        return [copy(random.choice(r))]


def pick(count: int, cards: list) -> list:
    picked = list()
    for i in range(count):
        picked.append(copy(random.choice(cards)))
    return picked


def lot_foil(picked: list) -> list:
    if random.randint(1, 3) == 1:
        random.choice(picked)["isFoil"] = True
    return picked


def print_result(picked: list) -> None:
    for card in picked:
        print(f"{card['rarity']} {card['name_jp']}/{card['name_en']}", end="")
        if card["isFoil"] is True:
            print(" [Foil]")
        else:
            print()


def run(show_result: bool = True) -> list:
    # 全カード情報
    card_list = get_card_list()

    # 取り出したカード
    picked = list()

    # 神話レア または レアのカードは、各パックに合計1枚入っている
    # 神話レアのカードはレアの1/8の確率で出現する
    picked = pick_mr(card_list["M"], card_list["R"])

    # アンコモンのカードは各パックに3枚入っている
    picked += pick(3, card_list["U"])

    # C10枚
    picked += pick(10, card_list["C"])

    # 基本土地 または タップインゲインランド（以下のリストのカード）は各パックに合計1枚入っている
    picked += pick(1, [*card_list["L"], *card_list["tap_in_gain_land"]])

    # foil抽選
    picked = lot_foil(picked)

    if show_result:
        print_result(picked)

    return picked


if __name__ == "__main__":
    run()
