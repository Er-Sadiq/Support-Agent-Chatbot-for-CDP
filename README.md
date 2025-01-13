
# Support-Agent-Chatbot-for-CDP

Support-Agent-Chatbot-for-CDP is an intelligent chatbot designed to assist users by providing information and guidance on various Customer Data Platforms (CDPs). The chatbot leverages platform documentation from leading CDPs to help users navigate and understand how to integrate, manage, and utilize customer data across various systems.

This project uses a Flask web framework and includes a scraping feature to gather up-to-date documentation from different CDP platforms like Segment, mParticle, Zeotap, and Lytics.


## Features
  - Web Interface: A simple and interactive UI where users can interact with the chatbot.
  - Documentation Scraping: The app scrapes platform documentation from Segment, mParticle, Lytics, and Zeotap to provide users with the most relevant and up-to-date information.
  - Customer Support: The chatbot helps answer questions related to the usage of different CDPs and offers step-by-step instructions for setting up and managing customer data.
  - Dynamic Responses: Based on the user’s query, the bot responds with context-specific answers pulled from the scraped documentation.
    


###  Setting up manually 

```bash
git clone https://github.com/your-username/Support-Agent-Chatbot-for-CDP.git
cd Support-Agent-Chatbot-for-CDP
window :- python -m venv env
         .\env\Scripts\activate
```

or 

```bash
Linux :- python3 -m venv env
source env/bin/activate
```

```bash
 windows :- pip install flask beautifulsoup4 requests  -q -U google-generativeai
 linux :- pip3 install flask beautifulsoup4 requests  -q -U google-generativeai
```


### Run the Application

You’re now ready to run the application! Use the following command to start the Flask app:

```bash
python app.py
```

This will start the application, and you can access the chatbot locally in your browser at:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

## Run with Docker, install docker then build and run 

```bash
   docker build -t supportagent-cpd .
   docker run -p 5000:5000 supportagent-cpd
```

## Screenshots / Demo

Here are some screenshots of the app in action:

![zeotap](https://github.com/user-attachments/assets/771c2f09-ed67-4cc2-af6b-da729fce886c)
![pow-1](https://github.com/user-attachments/assets/cf610d52-49bc-4070-91e2-e3feb3e32f6c)
![seg](https://github.com/user-attachments/assets/b7322824-e000-4fb8-a119-4db02e8046b6)
![pofw](https://github.com/user-attachments/assets/77460df5-6135-4a4b-b23b-ac1b75d9a6e9)


---

## Authors

- [@Er-Sadiq-Ahmed-Killear](https://github.com/Er-Sadiq/)
