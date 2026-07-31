import streamlit as st
import sqlite3
from src.logo import show_logo
from translations import translations


# ==========================
# CONFIGURATION
# ==========================

st.set_page_config(
    page_title="Profile",
    page_icon="👤",
    layout="wide"
)
show_logo()


# ==========================
# LANGUAGE SYSTEM
# ==========================

language = st.session_state.get(
    "language",
    "Français"
)


t = translations[language]



# ==========================
# TITLE
# ==========================

st.title(
    f"👤 {t['profile']}"
)



# ==========================
# CHECK LOGIN
# ==========================

if "user" not in st.session_state:

    st.warning(
        "⚠️ Please login first."
    )

    st.stop()



username = st.session_state["user"]



# ==========================
# DATABASE CONNECTION
# ==========================

connection = sqlite3.connect(
    "database.db"
)

cursor = connection.cursor()



# ==========================
# GET USER INFORMATION
# ==========================

cursor.execute(
    """
    SELECT username, email, language, created_at
    FROM users
    WHERE username = ?
    """,
    (username,)
)


user = cursor.fetchone()



# ==========================
# NUMBER OF ANALYSIS
# ==========================

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



# ==========================
# DISPLAY PROFILE
# ==========================

if user:


    username, email, language_db, created_at = user


    st.success(
        f"{t['welcome']} {username} 👋"
    )


    st.divider()



    col1, col2 = st.columns(2)



    with col1:


        st.info(
            f"""
👤 {t['username']}

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
🌍 {t['language']}

{language_db}
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



# ==========================
# LANGUAGE SETTINGS
# ==========================

st.divider()


st.subheader(
    "⚙️ Settings"
)



new_language = st.selectbox(
    t["language"],
    [
        "Français",
        "English",
        "العربية"
    ],
    index=[
        "Français",
        "English",
        "العربية"
    ].index(language_db)
)



if new_language != language_db:


    connection = sqlite3.connect(
        "database.db"
    )


    cursor = connection.cursor()


    cursor.execute(
        """
        UPDATE users
        SET language = ?
        WHERE username = ?
        """,
        (
            new_language,
            username
        )
    )


    connection.commit()

    connection.close()



    st.session_state["language"] = new_language


    st.success(
        "✅ Language updated successfully!"
    )


    st.rerun()



# ==========================
# LOGOUT
# ==========================

st.divider()



if st.button(
    t["logout"]
):

    del st.session_state["user"]

    st.rerun()