#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# chatgpt_app.py


# In[ ]:


# Importing required packages
import streamlit as st
import openai


# In[ ]:


st.title("Ask Jack")
st.sidebar.header("Instructions")
st.sidebar.info(
    '''This is a web application that allows you to interact with 
       the OpenAI API's implementation of the ChatGPT model.
       Enter a **query** in the **text box** and **press enter** to receive 
       a **response** from the ChatGPT
       '''
    )


# In[ ]:


# Set the model engine and your OpenAI API key
model_engine = "text-davinci-003"
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# openai.api_key = "your_secret_key" 


# In[ ]:


def main():
    '''
    This function gets the user input, pass it to ChatGPT function and 
    displays the response
    '''
    # Get user input
    user_query = st.text_input("Enter query here, to exit enter :q", "what is Python?")
    if user_query != ":q" or user_query != "":
        # Pass the query to the ChatGPT function
        response = ChatGPT(user_query)
        return st.write(f"{user_query} {response}")


# In[ ]:


def ChatGPT(user_query):
    ''' 
    This function uses the OpenAI API to generate a response to the given 
    user_query using the ChatGPT model
    '''
    # Use the OpenAI API to generate a response
    completion = openai.Completion.create(
                                  engine = model_engine,
                                  prompt = user_query,
                                  max_tokens = 1024,
                                  n = 1,
                                  temperature = 0.5,
                                      )
    response = completion.choices[0].text
    return response


# In[ ]:


# call the main function
main() 

