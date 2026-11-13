def count_vowels_and_consonants(text: str) -> dict:
    unli = 0
    undosh = 0

    for harf in text.lower():
        if harf.isalpha():
            if harf in "aeiou":
                unli += 1
            else:
                undosh += 1

    return {"unli": unli, "undosh": undosh}


print(count_vowels_and_consonants("Salom Dunyo!"))