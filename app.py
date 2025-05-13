# Simple UI
# import streamlit as st
# import requests
# import os

# # Load DeepSeek API Key
# DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "sk-0d87f9cd12a34851adb3de02ad3b9ff0")

# # Function to call DeepSeek API with custom system context
# def call_deepseek(messages):
#     url = "https://api.deepseek.com/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "model": "deepseek-chat",
#         "messages": messages,
#         "temperature": 0.7,
#         "max_tokens": 800
#     }
#     response = requests.post(url, json=payload, headers=headers)
#     if response.status_code != 200:
#         return f"❌ Error: {response.status_code} - {response.text}"
#     return response.json()["choices"][0]["message"]["content"]

# # Streamlit setup
# st.set_page_config(page_title="SMILE Relationship Chatbot", page_icon="🤖")
# st.title("🤖 SMILE AI Chatbot")
# st.subheader("Mood & Task Suggestion Assistant for Your Partner Type")

# # Dropdown for selecting relationship type
# partner_type = st.selectbox("What type of partner are you interacting with?", [
#     "Romantic Partner (Husband, Wife, Boyfriend, Girlfriend)",
#     "Family / Parental (Parent, Child, Co-Parent)",
#     "Colleague / Mentor / Manager",
#     "Best Friend / Close Friend / Roommate",
#     "Sibling (Brother, Sister, Twin, Step-sibling)"
# ])

# # Custom system prompt for domain restriction
# if "chat_history" not in st.session_state:
#     system_prompt = {
#         "role": "system",
#         "content": (
#             "You are SMILE's relationship support assistant. Only answer questions "
#             "related to relationship types: romantic, parental, colleague, friend, or sibling. "
#             "You help users suggest task ideas to improve moods, respond to emotional logs, "
#             "and support streaks in their partner interactions. Do not answer general knowledge, "
#             "unrelated tech, medical, or off-topic queries."
#         )
#     }
#     st.session_state.chat_history = [system_prompt]

# # Input field
# user_input = st.text_input("Type your message:", key="chat_input")

# # Handle input
# if st.button("Send") and user_input:
#     st.session_state.chat_history.append({"role": "user", "content": user_input})
#     with st.spinner("Thinking..."):
#         reply = call_deepseek(st.session_state.chat_history)
#     st.session_state.chat_history.append({"role": "assistant", "content": reply})
#     st.rerun()

# # Display conversation
# st.markdown("### 💬 Conversation History")
# for msg in st.session_state.chat_history[1:]:  # Skip system prompt
#     role = "🧍 **You:**" if msg["role"] == "user" else "🤖 **SMILE:**"
#     st.markdown(f"{role} {msg['content']}")

# Advanced UI 1

# import streamlit as st
# import requests
# import os

# # Load DeepSeek API Key
# DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "sk-0d87f9cd12a34851adb3de02ad3b9ff0")

# # Call DeepSeek API
# def call_deepseek(messages):
#     url = "https://api.deepseek.com/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "model": "deepseek-chat",
#         "messages": messages,
#         "temperature": 0.7,
#         "max_tokens": 800
#     }
#     response = requests.post(url, json=payload, headers=headers)
#     if response.status_code != 200:
#         return "❌ Error: Could not fetch reply from DeepSeek."
#     return response.json()["choices"][0]["message"]["content"]

# # Page settings
# st.set_page_config(page_title="SMILE Chatbot", page_icon="💬", layout="centered")
# st.markdown("<h1 style='text-align:center;'>💬 SMILE Mood & Task Chat Assistant</h1>", unsafe_allow_html=True)

# # Relationship dropdown
# partner_type = st.selectbox("💡 What type of partner are you interacting with?", [
#     "Romantic Partner (Husband, Wife, Boyfriend, Girlfriend)",
#     "Family / Parental (Parent, Child, Co-Parent)",
#     "Colleague / Mentor / Manager",
#     "Best Friend / Close Friend / Roommate",
#     "Sibling (Brother, Sister, Twin, Step-sibling)"
# ])

# # System message (only once)
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = [
#         {
#             "role": "system",
#             "content": (
#                 "You are SMILE's relationship support assistant. Only respond to relationship-related queries "
#                 "(romantic, parental, sibling, colleague, friend). Suggest mood-based tasks, streak strategies, and emotional advice. "
#                 "Do NOT answer general knowledge or unrelated questions."
#             )
#         }
#     ]

# # Chat input
# user_input = st.text_input("💬 Type your message here:", key="chat_input")

# # Submit
# if st.button("Send") and user_input:
#     st.session_state.chat_history.append({"role": "user", "content": user_input})
#     with st.spinner("🤖 Thinking..."):
#         reply = call_deepseek(st.session_state.chat_history)
#     st.session_state.chat_history.append({"role": "assistant", "content": reply})
#     st.rerun()

# # Style messages
# def render_chat_bubble(role, message):
#     if role == "user":
#         st.markdown(
#             f"<div style='text-align:right; background-color:#dcf8c6; padding:10px; border-radius:10px; margin:5px 0 5px 100px;'>"
#             f"<strong>You:</strong><br>{message}</div>", unsafe_allow_html=True
#         )
#     elif role == "assistant":
#         st.markdown(
#             f"<div style='text-align:left; background-color:#f1f0f0; padding:10px; border-radius:10px; margin:5px 100px 5px 0;'>"
#             f"<strong>SMILE:</strong><br>{message}</div>", unsafe_allow_html=True
#         )

# # Display history
# st.markdown("### 🗨️ Conversation")
# for chat in st.session_state.chat_history[1:]:  # skip system message
#     render_chat_bubble(chat["role"], chat["content"])

# advanced ui2 sk-0d87f9cd12a34851adb3de02ad3b9ff0
# import streamlit as st
# import requests
# import os

# # SET YOUR DEEPSEEK API KEY
# DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "sk-0d87f9cd12a34851adb3de02ad3b9ff0")

# def call_deepseek(messages):
#     url = "https://api.deepseek.com/v1/chat/completions"
#     headers = {
#         "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "model": "deepseek-chat",
#         "messages": messages,
#         "temperature": 0.7,
#         "max_tokens": 800
#     }
#     response = requests.post(url, json=payload, headers=headers)
#     if response.status_code != 200:
#         return "❌ Error: Could not fetch reply from DeepSeek."
#     return response.json()["choices"][0]["message"]["content"]

# # ✅ PAGE CONFIG
# st.set_page_config(page_title="SMILE Chatbot", page_icon="💬", layout="centered")

# # ✅ CUSTOM STYLING
# st.markdown("""
#     <style>
#     html, body, [class*="css"] {
#         font-family: 'Segoe UI', sans-serif;
#     }
#     .chat-container {
#         background-color: var(--background-color);
#         border: 2px solid #444;
#         padding: 20px 25px;
#         border-radius: 16px;
#         max-width: 720px;
#         margin: auto;
#         box-shadow: 0 4px 10px rgba(0,0,0,0.1);
#     }
#     .chat-title {
#         text-align: center;
#         font-size: 26px;
#         font-weight: bold;
#         margin-bottom: 5px;
#     }
#     .chat-subtitle {
#         text-align: center;
#         font-size: 14px;
#         color: gray;
#         margin-bottom: 20px;
#     }
#     .bubble {
#         padding: 12px 16px;
#         border-radius: 16px;
#         margin-bottom: 10px;
#         max-width: 85%;
#         font-size: 15px;
#         line-height: 1.5;
#     }
#     .user {
#         background-color: #d2f8d2;
#         margin-left: auto;
#         text-align: right;
#     }
#     .bot-light {
#         background-color: #e3f0ff;
#         border: 1px solid #c7dcf2;
#         margin-right: auto;
#         text-align: left;
#     }
#     .bot-dark {
#         background-color: #2a2d3e;
#         color: #f1f1f1;
#         border: 1px solid #555;
#         margin-right: auto;
#         text-align: left;
#     }
#     .pair {
#         margin-bottom: 18px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # ✅ INIT STATE
# if "chat_pairs" not in st.session_state:
#     st.session_state.chat_pairs = []
#     st.session_state.chat_history = [{
#         "role": "system",
#         "content": (
#             "You are SMILE's relationship support assistant. Only respond to mood, task, and streak suggestions "
#             "related to romantic, sibling, parental, friend, or colleague relationships."
#         )
#     }]

# # ✅ CHAT CONTAINER
# st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
# st.markdown("<div class='chat-title'>🤖 SMILE AI Chatbot</div>", unsafe_allow_html=True)
# st.markdown("<div class='chat-subtitle'>Mood & Task Suggestion Assistant for Your Partner Type</div>", unsafe_allow_html=True)

# # ✅ SELECT RELATIONSHIP TYPE
# partner_type = st.selectbox("Select your partner type:", [
#     "Romantic Partner (Husband, Wife, Boyfriend, Girlfriend)",
#     "Family / Parental (Parent, Child, Co-Parent)",
#     "Colleague / Mentor / Manager",
#     "Best Friend / Close Friend / Roommate",
#     "Sibling (Brother, Sister, Twin, Step-sibling)"
# ])

# # ✅ INPUT INSIDE CONTAINER (no rogue inputs outside this block!)
# user_input = st.text_input("💬 Type your message here")

# if st.button("🚀 Send") and user_input.strip():
#     st.session_state.chat_history.append({"role": "user", "content": user_input})
#     with st.spinner("Thinking..."):
#         reply = call_deepseek(st.session_state.chat_history)
#     st.session_state.chat_history.append({"role": "assistant", "content": reply})
#     st.session_state.chat_pairs.append((user_input, reply))
#     st.rerun()

# # ✅ CONVERSATION DISPLAY
# st.markdown("### 🗨️ Latest Conversation", unsafe_allow_html=True)
# bot_class = "bot-dark" if st.get_option("theme.base") == "dark" else "bot-light"

# for user_msg, bot_msg in reversed(st.session_state.chat_pairs):
#     st.markdown(f"<div class='pair'><div class='bubble user'><strong>You:</strong> {user_msg}</div>", unsafe_allow_html=True)
#     st.markdown(f"<div class='bubble {bot_class}'><strong>SMILE:</strong> {bot_msg}</div></div>", unsafe_allow_html=True)

# st.markdown("</div>", unsafe_allow_html=True)  # Close chat-container


import streamlit as st
import requests
import os

# SET YOUR DEEPSEEK API KEY
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "sk-0d87f9cd12a34851adb3de02ad3b9ff0")

def call_deepseek(messages):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 800
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        return "❌ Error: Could not fetch reply from DeepSeek."
    return response.json()["choices"][0]["message"]["content"]

# ✅ PAGE CONFIG
st.set_page_config(page_title="SMILE Chatbot", page_icon="💬", layout="centered")

# ✅ CUSTOM STYLING
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
    }
    .bubble {
        padding: 12px 16px;
        border-radius: 16px;
        margin-bottom: 10px;
        max-width: 85%;
        font-size: 15px;
        line-height: 1.5;
    }
    .user {
        background-color: #d2f8d2;
        margin-left: auto;
        text-align: right;
    }
    .bot {
        background-color: #e3f0ff;
        margin-right: auto;
        text-align: left;
    }
    .pair {
        margin-bottom: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ INIT STATE
if "chat_pairs" not in st.session_state:
    st.session_state.chat_pairs = []
    st.session_state.chat_history = [{
        "role": "system",
        "content": (
            "You are SMILE's relationship support assistant. Only respond to mood, task, and streak suggestions "
            "related to romantic, sibling, parental, friend, or colleague relationships."
        )
    }]

# ✅ HEADER
st.markdown("## 🤖 SMILE AI Chatbot")
st.markdown("Mood & Task Suggestion Assistant for Your Partner Type")

# ✅ SELECT RELATIONSHIP TYPE
partner_type = st.selectbox("Select your partner type:", [
    "Romantic Partner (Husband, Wife, Boyfriend, Girlfriend)",
    "Family / Parental (Parent, Child, Co-Parent)",
    "Colleague / Mentor / Manager",
    "Best Friend / Close Friend / Roommate",
    "Sibling (Brother, Sister, Twin, Step-sibling)"
])

# ✅ INPUT
user_input = st.text_input("💬 Type your message here")

if st.button("🚀 Send") and user_input.strip():
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        reply = call_deepseek(st.session_state.chat_history)
    st.session_state.chat_history.append({"role": "assistant", "content": reply})
    st.session_state.chat_pairs.append((user_input, reply))
    st.rerun()

# ✅ CONVERSATION DISPLAY
st.markdown("### 🗨️ Latest Conversation")
for user_msg, bot_msg in reversed(st.session_state.chat_pairs):
    st.markdown(f"<div class='pair'><div class='bubble user'><strong>You:</strong> {user_msg}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='bubble bot'><strong>SMILE:</strong> {bot_msg}</div></div>", unsafe_allow_html=True)