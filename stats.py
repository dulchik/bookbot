def count_words(text):
    return len(text.split())

def count_char(text):
    d = {}
    for i in text.lower():
        if i in d: 
            d[i] += 1
        else: 
            d[i] = 1
    return d

def sort_dict(d):
    l = []

    for k, v in d.items():
        l.append({"char": k, "num": v})

    l.sort(key=lambda x: x["num"], reverse=True)

    return l
