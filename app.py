import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# Page Configuration
st.set_page_config(page_title="Professional Email Writing Assistant", page_icon="📧", layout="centered")

st.title("📧 Professional Email Writing Assistant")
st.write("Generate professional cold emails, job applications, and business messages instantly using GenAI!")

# Initialize Groq LLM using Streamlit Secrets for the API key
api_key = st.secrets["GROQ_API_KEY"]
llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=api_key)

# Input fields for user customization
sender_name = st.text_input("Your Name (e.g., Alex Smith):")
recipient = st.text_input("Recipient / Company Name (e.g., HR Team at Google, John Doe):")
email_type = st.selectbox("Email Type / Purpose:", ["Job Application", "Sales / Business Pitch", "Networking Connection", "Follow-up", "General Professional Inquiry"])
key_details = st.text_area("Key Details / Context to Include:", placeholder="Mention your 3 years of Python experience, attach portfolio link, etc.")
tone = st.selectbox("Select Tone:", ["Professional & Formal", "Friendly & Conversational", "Direct & Concise"])

# Prompt Template
prompt_template = PromptTemplate(
    input_variables=["sender_name", "recipient", "email_type", "key_details", "tone"],
    template="""
    You are an expert professional copywriter and communication assistant. Write a high-quality, compelling, and professional email based on the following parameters:
    
    - Sender Name: {sender_name}
    - Recipient: {recipient}
    - Email Type: {email_type}
    - Key Details / Context: {key_details}
    - Desired Tone: {tone}
    
    Ensure the email includes a strong subject line, a personalized opening, a clear and engaging body highlighting the key details, and sign off professionally using the exact Sender Name provided ({sender_name}).
    """
)

chain = prompt_template | llm

# Generate button
if st.button("Generate Email"):
    if not sender_name or not recipient or not key_details:
        st.warning("Please fill in your name, recipient name, and key details.")
    else:
        with st.spinner("Writing your professional email..."):
            response = chain.invoke({
                "sender_name": sender_name,
                "recipient": recipient,
                "email_type": email_type,
                "key_details": key_details,
                "tone": tone
            })
            st.success("Here is your generated email:")
            st.write(response.content)