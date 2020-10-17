from backend import api
import os
import pandas as pd

def find_prob(model, text):
    output, all_count = model.check_probabilities(text)
    output = output['real_topk']
    count = 0
    for _, prob in output:
        if prob >= 0.1:
            count += 1

    return count / all_count

def get_text_list():
    texts = []
    base_dir = "../scripts/fulltext/"
    for i in range(93):
        file_name = "{}{}.txt".format(base_dir, i)
        file = open(file_name, "r")
        text = file.read()
        texts.append(text)
        file.close()

    return texts

if __name__ == '__main__':
    lm = api.LM()
    texts = get_text_list()
    probs = []
    for text in texts:
        prob = find_prob(lm, text)
        print(prob)
        probs.append(prob)

    print(len(probs))
    df = pd.read_csv('../scripts/data/news.csv')
    df['Fake Scores'] = probs
    pd.DataFrame(df).to_csv('../scripts/data/news1.csv', index=False)
