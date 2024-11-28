strings = input().split(", ")
target_string = input()

words_by_idx = {}
words_count = {}

for word in strings:
    if word in words_count:
        words_count[word] += 1
        continue

    words_count[word] = 1

    try:
        idx = 0
        while True:
            idx = target_string.index(word, idx)
            if idx not in words_by_idx:
                words_by_idx[idx] = []
            words_by_idx[idx].append(word)
            idx += len(word)
    except ValueError:
        pass


def word_cruncher(target, words_by_idx, words_count, idx=0, used=None):
    if used is None:
        used = []
    if idx >= len(target):
        print(" ".join(used))
    if idx not in words_by_idx:
        return
    for w in words_by_idx[idx]:
        if words_count[w] > 0:
            used.append(w)
            words_count[w] -= 1

            word_cruncher(target, words_by_idx, words_count, idx + len(w), used)

            used.pop()
            words_count[w] += 1


word_cruncher(target_string, words_by_idx, words_count)
