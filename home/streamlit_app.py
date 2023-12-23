import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI


def get_pdf_text(pdf_docs):
    text = ''
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def split_text(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
        )
    chunks = text_splitter.split_text(raw_text)
    return chunks


def get_vectorstore(text_chunks, api_key):
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    vectorstore = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore, api_key):
    llm = ChatOpenAI(openai_api_key=api_key)
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever = vectorstore.as_retriever(),
        memory = memory
    )
    return conversation_chain


def handle_userinput(question):
    response = st.session_state.information({'question': f"According to the provided context, {question}"})
    st.session_state.chat_history = response['chat_history']
    return st.session_state.chat_history


def disable_chat():
    st.session_state["chat_box"] = True


def enable_chat():
    st.session_state["chat_box"] = False


def main():

    
    st.set_page_config(page_title="Chatbot", page_icon=":robot_face:")

    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if "information" not in st.session_state:
        st.session_state.information = None
    if "conversations" not in st.session_state:
        st.session_state["conversations"] = [{"role": "assistant", "content": "What questions do you have regarding your PDF documents?"}]
    if "chat_box" not in st.session_state:
        st.session_state["chat_box"] = True

    
    with st.sidebar:
        
        space = st.container()
        
        
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        
        
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload PDF", type="pdf", accept_multiple_files=True)

        if st.button("Process"):
            if not openai_api_key:
                st.warning(' add  API key to continue.', icon="⚠️")
                st.stop()
            elif not pdf_docs:
                st.warning(' Upload the PDF document to continue.', icon="⚠️")
                st.stop()
            else:
                with st.spinner("Processing"):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = split_text(raw_text)
                    vectorstore = get_vectorstore(text_chunks, openai_api_key)
                    st.session_state.information = get_conversation_chain(vectorstore, openai_api_key) 
                    enable_chat()

    
    st.title("Chatbot")
    
    
    for msg in st.session_state.conversations:
        st.chat_message(msg["role"]).write(msg["content"])
    
    
    if question := st.chat_input("Write your question or comments here", disabled=st.session_state.chat_box, on_submit=disable_chat):
        
        
        if not openai_api_key:
            st.warning('Please add your OpenAI API key to continue.', icon="⚠️")
            st.stop()
        
        
        if st.session_state.information is None:
            st.warning('Please process the PDF file to continue.', icon="⚠️")
            st.stop()
        
        
        st.session_state.conversations.append({"role": "user", "content": question})
        
        st.chat_message("user").write(question)
        
        with st.spinner("Processing"):
            response = handle_userinput(question)
            msg = response[-1].content
            st.session_state.conversations.append({"role": "assistant", "content": msg})
            st.chat_message("assistant").write(msg)
        

        enable_chat()
        st.experimental_rerun()
    
if __name__ == '__main__':
    main()