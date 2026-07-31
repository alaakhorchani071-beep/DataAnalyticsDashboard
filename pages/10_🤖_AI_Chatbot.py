import streamlit as st
from openai import OpenAI
from src.logo import show_logo
from translations import translations



# ==========================
# LANGUAGE SYSTEM
# ==========================

language = st.session_state.get(
    "language",
    "Français"
)

t = translations[language]



# ==========================
# CONFIGURATION
# ==========================

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)
show_logo()


st.title(
    "🤖 " + t["assistant"]
)



# ==========================
# API KEY
# ==========================

if "GROQ_API_KEY" not in st.secrets:


    st.error(
        "❌ GROQ_API_KEY not found in secrets.toml"
    )


    st.stop()



client = OpenAI(

    api_key=st.secrets["GROQ_API_KEY"],

    base_url="https://api.groq.com/openai/v1"

)



# ==========================
# DATASET CONTEXT
# ==========================

context = ""



if "data" in st.session_state:


    data = st.session_state["data"]



    context += f"""

Dataset Information:

Rows: {data.shape[0]}

Columns: {data.shape[1]}


Column names:

{', '.join(data.columns)}


Missing values:

{data.isnull().sum().sum()}

"""



if "ml_results" in st.session_state:


    ml = st.session_state["ml_results"]



    context += f"""

Machine Learning Results:


Model:

{ml['model_name']}


MAE:

{ml['mae']}


RMSE:

{ml['rmse']}


R² Score:

{ml['r2']}


Features:

{', '.join(ml['features'])}

"""



# ==========================
# CHAT HISTORY
# ==========================

if "messages" not in st.session_state:

    st.session_state.messages = []



for message in st.session_state.messages:


    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )



# ==========================
# USER QUESTION
# ==========================

prompt = st.chat_input(
    t["ask_question"]
)



if prompt:


    st.session_state.messages.append(

        {
            "role": "user",

            "content": prompt
        }

    )



    with st.chat_message(
        "user"
    ):

        st.markdown(
            prompt
        )



    try:


        response = client.chat.completions.create(


            model="llama-3.3-70b-versatile",


            messages=[


                {

                    "role": "system",

                    "content": f"""

You are an expert Data Analyst.

Answer in the same language as the user.

Use ONLY this information:

{context}


If information is missing,
explain that clearly.

"""

                },


                {

                    "role": "user",

                    "content": prompt

                }


            ],


            temperature=0.3

        )



        answer = response.choices[0].message.content



    except Exception as e:


        answer = f"❌ Error:\n\n{e}"



    st.session_state.messages.append(

        {

            "role": "assistant",

            "content": answer

        }

    )



    with st.chat_message(
        "assistant"
    ):

        st.markdown(
            answer
        )