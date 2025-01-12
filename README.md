
# Support-Agent-Chatbot-for-CDP

Support-Agent-Chatbot-for-CDP is an intelligent chatbot designed to assist users by providing information and guidance on various Customer Data Platforms (CDPs). The chatbot leverages platform documentation from leading CDPs to help users navigate and understand how to integrate, manage, and utilize customer data across various systems.

This project uses a Flask web framework and includes a scraping feature to gather up-to-date documentation from different CDP platforms like Segment, mParticle, Zeotap, and Lytics.


## Features
  - Web Interface: A simple and interactive UI where users can interact with the chatbot.
  - Documentation Scraping: The app scrapes platform documentation from Segment, mParticle, Lytics, and Zeotap to provide users with the most relevant and up-to-date information.
  - Customer Support: The chatbot helps answer questions related to the usage of different CDPs and offers step-by-step instructions for setting up and managing customer data.
  - Dynamic Responses: Based on the user’s query, the bot responds with context-specific answers pulled from the scraped documentation.
    
```markdown
## Installation Instructions

###  Clone the Repository & Navigate to the Project Directory

Once the repository is cloned, navigate to the project folder:

```bash
git clone https://github.com/your-username/Support-Agent-Chatbot-for-CDP.git
cd Support-Agent-Chatbot-for-CDP
```

###  Set Up a Virtual Environment (Optional but Recommended)

It’s best to use a virtual environment to avoid conflicts with other Python projects on your system. To create a virtual environment, run the following command:

```bash
python -m venv env
```

This will create a directory called `env` in the project folder that contains the virtual environment.

###  Activate the Virtual Environment

Now, activate the virtual environment:

- **Windows:**

```bash
.\env\Scripts\activate
```

- **Linux or Mac:**

```bash
source env/bin/activate
```

When activated, your terminal prompt will change to indicate that you are inside the virtual environment.

###  Install Required Dependencies

With the virtual environment activated, install the required dependencies using `pip` by running the following command:

```bash
pip install -r requirements.txt
```

This will install all the necessary Python libraries needed for the project, including **Flask**, **BeautifulSoup**, and others.

### Run the Application

You’re now ready to run the application! Use the following command to start the Flask app:

```bash
python app.py
```

This will start the application, and you can access the chatbot locally in your browser at:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

###  Reactivating the Virtual Environment (if needed)

If you’ve closed your terminal and need to reactivate your virtual environment, follow these steps again:

- **Windows:**

```bash
.\env\Scripts\activate
```

- **Linux or Mac:**

```bash
source env/bin/activate
```

Then, simply run the app:

```bash
python app.py
```

---

## Screenshots / Demo

Here are some screenshots of the app in action:

![zeotap](https://github.com/user-attachments/assets/771c2f09-ed67-4cc2-af6b-da729fce886c)
![pow-1](https://github.com/user-attachments/assets/cf610d52-49bc-4070-91e2-e3feb3e32f6c)
![seg](https://github.com/user-attachments/assets/b7322824-e000-4fb8-a119-4db02e8046b6)
![pofw](https://github.com/user-attachments/assets/77460df5-6135-4a4b-b23b-ac1b75d9a6e9)


---

## Authors

- [@Er-Sadiq-Ahmed-Killear](https://github.com/Er-Sadiq/)
```

### Key Sections in the README:
1. **Project Overview**: Describes what the project does, its key features, and technologies used.
2. **Installation Instructions**: Detailed steps on how to clone the repo, set up a virtual environment, and run the application.
3. **Screenshots**: Includes demo images of the app's interface.
4. **Author**: Provides the GitHub profile link of the project author.

Feel free to update any sections (like the GitHub link in the clone command) based on your actual repository setup.

Let me know if you need more adjustments or anything else!
