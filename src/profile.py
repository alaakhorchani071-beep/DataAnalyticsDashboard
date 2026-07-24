import streamlit as st

from src.auth import get_user_profile


st.set_page_config(
    page_title="Profile",
    page_icon="👤",
    layout="wide"
)



st.title("👤 Profile")



# Vérifier connexion

if "user" not in st.session_state:

    st.warning(
        "⚠️ Veuillez vous connecter"
    )

    st.stop()



username = st.session_state["user"]



# Récupérer les informations

user = get_user_profile(
    username
)



if user:


    username, email, language, created_at = user



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
📅 Created at

{created_at}
"""
        )



else:

    st.error(
        "Utilisateur introuvable"
    )



st.divider()



st.subheader(
    "📊 Statistics"
)



from src.auth import get_user_statistics


actions, reports = get_user_statistics(username)


col1, col2 = st.columns(2)


with col1:

    st.metric(
        "📂 Analyses réalisées",
        actions
    )


with col2:

    st.metric(
        "📄 Rapports PDF",
        reports
    )



st.divider()



if st.button(
    "🚪 Logout"
):

    del st.session_state["user"]

    st.rerun()
