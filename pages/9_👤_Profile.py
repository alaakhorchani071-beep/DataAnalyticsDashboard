import streamlit as st
import sqlite3


st.set_page_config(
    page_title="Profile",
    page_icon="👤",
    layout="wide"
)


st.title(
    "👤 User Profile"
)


# Vérification connexion

if "user" not in st.session_state:

    st.warning(
        "⚠️ Please login first."
    )

    st.stop()



username = st.session_state["user"]



# Connexion base de données

connection = sqlite3.connect(
    "database.db"
)

cursor = connection.cursor()



# Récupérer les informations utilisateur

cursor.execute(
    """
    SELECT username, email, language, created_at
    FROM users
    WHERE username = ?
    """,
    (username,)
)


user = cursor.fetchone()



# Nombre d'analyses

cursor.execute(
    """
    SELECT COUNT(*)
    FROM history
    WHERE username = ?
    """,
    (username,)
)


total_analysis = cursor.fetchone()[0]


connection.close()



# Affichage

if user:


    username, email, language, created_at = user


    st.success(
        f"Welcome {username} 👋"
    )


    st.divider()


    col1, col2 = st.columns(2)



    with col1:

        st.info(
            f"""
👤 Username

{username}
"""
        )


        st.info(
            f"""
📧 Email

{email}
"""
        )



    with col2:


        st.info(
            f"""
🌍 Language

{language}
"""
        )


        st.info(
            f"""
📅 Account created

{created_at}
"""
        )



    st.divider()



    st.subheader(
        "📊 Statistics"
    )


    st.metric(
        "📂 Analyses performed",
        total_analysis
    )



else:

    st.error(
        "User not found"
    )



st.divider()



st.subheader(
    "⚙️ Settings"
)



new_language = st.selectbox(
    "🌍 Language",
    [
        "Français",
        "English",
        "العربية"
    ],
    index=[
        "Français",
        "English",
        "العربية"
    ].index(language)
)



if new_language != language:

    st.info(
        "Language update will be added next."
    )



st.divider()



if st.button(
    "🚪 Logout"
):

    del st.session_state["user"]

    st.rerun()