def counter(text_1: str, text_2: str) -> int:
    min_len = min([len(text_1), len(text_2)])
    count_eq_lett: int = 0
    for i in range(min_len):
        if text_1[i] == text_2[i]:
            count_eq_lett += 1
    return count_eq_lett

print(counter('qwerty', 'qwetyu'))
