def monoanalysis(message, alphabet, max_n_letter=3, top_k=5):
    text = message.replace('\n', ' ').strip()
    text = ''.join([char for char in text if char in alphabet])
    result = ""
    for n in range(1, max_n_letter + 1):
        result += f"\n------------------------------------------\n"
        result += f"Most repeated {n} letters / Top {top_k}:\n"
        nletter_counts = {}

        for i in range(len(text) - n + 1):
            nletter = text[i:i + n]

            if nletter in nletter_counts:
                nletter_counts[nletter] += 1
            else:
                nletter_counts[nletter] = 1

        sorted_nletters = sorted(nletter_counts.items(), key=lambda x: x[1], reverse=True)[:top_k]

        for nletter, count in sorted_nletters:
            result += f"{nletter}: {count}\n"
    return result

