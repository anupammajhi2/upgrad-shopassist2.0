# ShopAssist 2.0
ShopAssist with function calling

## 1. Background
With the rapid rise of e-commerce, online shopping has become the preferred choice for many. However, the abundance of options and lack of tailored guidance often make the experience overwhelming. To tackle this, we created **ShopAssist AI**, a chatbot that combines large language models with rule-based methods to deliver accurate and dependable product information.

## 2. Problem Statement
Given a dataset of laptops containing product names, specifications, and descriptions, the goal is to design a chatbot that can parse this dataset and provide reliable laptop recommendations tailored to user needs.

## 3. Approach
1. **Conversation & Requirement Gathering:**  
   The chatbot employs language models to generate natural, human-like responses. It guides the user through a conversation to collect details about their laptop requirements.  
   
2. **Information Extraction:**  
   Once the key requirements are identified, rule-based logic is applied to filter and select the top 3 laptops that best fit the criteria.  

3. **Personalized Recommendation:**  
   The chatbot then engages further with the user, clarifying doubts and refining suggestions to help them choose the most suitable laptop.

## 4. System Functionalities

- **User Interface:** A simple, interactive web interface where users communicate with the assistant.  
- **Conversational AI:** Powered by OpenAI’s chat model, the assistant asks relevant questions, understands preferences, and guides users.  
- **Input Moderation:** OpenAI’s moderation API ensures safe and secure conversations.  
- **User Profile Extraction:** Key preferences (budget, screen size, performance, etc.) are extracted from dialogue and structured into a JSON object using OpenAI’s function calling feature.  

The dataset `laptop_data.csv` includes detailed laptop features with descriptions. The chatbot leverages LLMs to parse the `Description` field and generate meaningful recommendations.

## 5. System Architecture

ShopAssistAI is built on a client-server model. Users interact through a web interface hosted on a server running a Flask application. The Flask app connects with OpenAI’s APIs for conversation and moderation, while also retrieving and comparing laptop details from an external database.

![stages](https://github.com/user-attachments/assets/e6e690f5-8bb2-4cf6-9b13-08b7eaee14f9)  
![systemdesign](https://github.com/user-attachments/assets/001e9fff-763e-4a54-9cc0-6633021f7ea0)  

## 6. Implementation Details

The Flask application incorporates multiple components:

- **Routing:** Maps user requests to the correct functions via URL endpoints.  
- **Conversation Management:** Initiates, manages, and stores conversation history while generating responses through OpenAI’s chat model.  
- **Input Processing:** Captures user messages, applies moderation checks, and extracts structured user profiles (converts input strings to JSON via OpenAI Function Calling).  
- **Recommendation Logic:** Matches the extracted profile against laptop data, validates the results, and generates recommendation responses.  

### Key Functions
- `initialize_conversation()`: Starts a new conversation with the system prompt.  
- `get_chat_completions()`: Processes the ongoing dialogue and returns the assistant’s reply.  
- `moderation_check()`: Evaluates user and assistant messages for inappropriate content, ending the session if necessary.  
- `intent_confirmation_layer()`: Ensures the chatbot has correctly captured the user’s requirements.  
- `dictionary_present()`: Confirms that the chatbot outputs the user profile as a Python dictionary.  
- `compare_laptops_with_user()`: Matches the user’s profile with available laptops and returns the top 3 recommendations.  
- `initialize_conv_reco()`: Starts the recommendation conversation.  

### Prerequisites
- Python 3.9 and above
- venv (optional)
- OpenAI API Key
    - IMPORTANT! Create a text file named 'OpenAI_API_Key.txt' and add your OpenAI API key to it OR save it as an environment variable OPENAI_API_KEY

### Getting Started

#### 1. Clone the repository:

```
git clone https://github.com/anupammajhi2/upgrad-shopassist2.0.git

cd upgrad-shopassist2.0
```

#### 2. Create a virtual environment **(optional)**:

```
python -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

#### 3. Install the required dependencies:
```
pip install -r requirements.txt
```

#### 4. Run the application:
```
python app.py
```