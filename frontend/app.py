import streamlit as st
import requests

st.title("Mini SaaS Multi-Tenant")

api_url = "http://localhost:8000/query"

tenant_choice = st.selectbox(
    "Choisissez le client",
    ["tenantA", "tenantB"]
)

api_keys = {
    "tenantA": "tenantA_key",
    "tenantB": "tenantB_key"
}

question = st.text_input("Posez votre question")

if st.button("Envoyer"):
    headers = {
        "X-API-KEY": api_keys[tenant_choice]
    }

    response = requests.post(
        api_url,
        json={"question": question},
        headers=headers
    )

    data = response.json()

    st.subheader("Réponse")
    st.write(data["answer"])

    st.subheader("Sources")
    st.write(data["sources"])
