from backend import api
import os

def find_prob(model, text):
    output, all_count = model.check_probabilities(text)
    output = output['real_topk']
    count = 0
    for _, prob in output:
        if prob >= 0.1:
            count += 1

    print(count, all_count)
    return count / all_count

def get_text_list():
    texts = []
    base_dir = "../scripts/text/"
    for file_name in os.listdir(base_dir):
        file_name = base_dir + file_name
        file = open(file_name, "r")
        text = file.read()
        texts.append(text)
        file.close()
    
    return texts

if __name__ == '__main__':
    lm = api.LM()

    #text = open("../scripts/text/1.txt", "r").read()
    #text.replace("\n", " ")
    #prob = find_prob(lm, text)

    texts = get_text_list()
    for text in texts:
        prob = find_prob(lm, text)
        print(prob)
