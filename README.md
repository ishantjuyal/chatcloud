# Overview

Chatclouds is a wordcloud library which allows you to create and save a wordcloud of your whatsapp chats. The library uses wordcloud library to generate images. The preprocessing of the text from the txt files are already taken care of. The only thing you need to do is to extract your chat from WhatsApp and then using that file in your python code.

Take a look at the library [here](https://pypi.org/project/chatclouds/)

# Installing chatclouds

```
pip install chatclouds
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

3. plot_time()
    Code:

    from chatclouds import common
    plot_time(filename)
    (filename needs to be the name/ path of txt file containing your WhatsApp Chat)

    What it does:
    plot_time() function shows a bar plot of number of messages with respect to 1 hour time slots.  

4. common()
    Code:

    from chatclouds import common
    common(filename)
    (filename needs to be the name/ path of txt file containing your WhatsApp Chat)

    What it does:
    common() function prints the 20 most frequently used word in the chat between two people. 
    
# Example

A sample notebook showing how to use the library could be found [here](https://github.com/ishantjuyal/chatcloud/blob/master/Example/Using%20chatclouds%20library.ipynb)

# Sample output

Sample output of the WordCloud:

![sample](https://github.com/ishantjuyal/chatcloud/blob/master/Example/sample.png)

Sample output of the time analysis plot:

![plot sample](https://github.com/ishantjuyal/chatcloud/blob/master/Example/plot_sample.png)
