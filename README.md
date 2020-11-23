# Overview

Chatclouds is a wordcloud library which allows you to create and save a wordcloud of your whatsapp chats. The library uses wordcloud library to generate images. The preprocessing of the text from the txt files are already taken care of. The only thing you need to do is to extract your chat from WhatsApp and then using that file in your python code.

Take a look at the library [here](https://test.pypi.org/project/chatclouds/0.0.4/).

# Installing chatclouds

pip install -i https://test.pypi.org/simple/ chatclouds==0.0.4

```
pip install -i https://test.pypi.org/simple/ chatclouds==0.0.4
```

# Importing chatclouds

import chatclouds

# Functions

1. show()
    Code:
    
    from chatclouds import show
    show(filename) 
    (filename needs to be the name/ path of txt file containing your WhatsApp Chat)

    What it does:
    show() function returns an image of the WordCloud that has been formed from the chat after preprocessing the text and removing all the stopwords. 

2. save()
    Code:

    from chatclouds import save
    save(filename)
    (filename needs to be the name/ path of txt file containing your WhatsApp Chat)

    What it does:
    show() function saves a .png image of the WordCloud that has been formed from the chat after preprocessing the text and removing all the stopwords.

3. common()
    Code:

    from chatclouds import common
    common(filename)
    (filename needs to be the name/ path of txt file containing your WhatsApp Chat)

    What it does:
    common() function prints the 20 most frequently used word in the chat between two people. 
    
# Sample output

![sample](https://github.com/ishantjuyal/chatcloud/blob/master/Example/sample.png)
