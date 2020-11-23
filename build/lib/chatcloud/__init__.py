from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import contractions
import re


def read_chat(url):
    # Change the name of the file and run the whole code
    chat_file = open('chat_vanshika.txt', encoding = "utf8")
    chat_text = chat_file.read()
    chat_list = chat_text.split('\n')
    
    for i in range(len(chat_list)):
        chat_list[i] = chat_list[i][20:]
        if ':' in chat_list[i]:
            ind  = chat_list[i].index(':') + 1
            chat_list[i] = chat_list[i][ind:]
    return(chat_list)



def get_sentence(url):
    chat_list = read_chat(url)
    stopwords = pd.read_csv("stopwords_hindi_english.csv")
    stop_words = list(stopwords['hinglish'])
    
    new_sentence = ''
    for i in range(len(chat_list)):
        sentence = chat_list[i]
        sentence = contractions.fix(sentence)
        sentence = re.sub(r'[^\w\s]', '', sentence).lower()
        sentence = re.sub(r"(^|\W)\d+", '', sentence)
        if sentence != '':
            chat_list[i] = sentence
        words = sentence.split()
        for i in words:
            if i not in stop_words:
                new_sentence = new_sentence + i + ' '
    return(new_sentence, stop_words)


def get_common_words(url):
    new_sentence, stop_words = get_sentence(url)
    word_dict = {}
    words = new_sentence.split()
    for word in words:
        if word not in stop_words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    common = []
    for w in sorted(word_dict, key=word_dict.get, reverse=True):
        common.append(w)
    return(common)



def make_wordcloud(url):
    new_sentence, stop_words = get_sentence(url)
    wordcloud = WordCloud(width = 800, height = 800,
                      background_color = 'white',
                      stopwords = stop_words,
                      min_font_size = 10).generate(new_sentence)
    return(wordcloud)


# Useful functions
def show(url):
    wordcloud = make_wordcloud(url)

    plt.figure(figsize = (8,8), facecolor= None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()


def save(url):
    wordcloud = make_wordcloud(url)
    file_name = url[:-4] + '.png'
    wordcloud.to_file(file_name)

def common(url):
    common_words = get_common_words(url)
    common_20 = common_words[:20]
    print("20 most frequent used word in the chat are:")
    for i in range(len(common_20)):
        print(str(i+1) + '. ' + common_20[i])