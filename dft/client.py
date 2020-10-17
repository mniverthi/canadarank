from backend import api

lm = api.LM()
text = "this dog is super cool but he's also kind of annoying. by the way I am FAT"
output = lm.check_probabilities(text)['real_topk']

count = 0
all_count = len(text.split(" "))

for _, prob in output:
    if prob > 0.015:
        count += 1

print("sus words:", count, "all words:", all_count)
print(count / all_count)