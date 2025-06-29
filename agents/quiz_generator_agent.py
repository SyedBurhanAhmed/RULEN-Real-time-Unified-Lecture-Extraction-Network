from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv('API_KEY')

def generate_quiz(vectorstore, question_type="all"):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",  # or gemini-1.5-pro for better quality
        google_api_key=GOOGLE_API_KEY
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    if question_type == "mcq":
        prompt = (
            "Based on the following lecture content, generate **10 multiple choice questions** with correct answers.\n"
            "- Use valid **Markdown formatting**.\n"
            "- Format each question with a numbered list.\n"
            "- Present answer options as bullet points (a), b), c), d)).\n"
            "- Highlight the correct answer below each question using '**Answer:**'.\n"
            "- Do not include any formatting explanation."
        )
    elif question_type == "short":
        prompt = (
            "Based on the following lecture content, generate **10 short answer questions** with answers.\n"
            "- Use valid **Markdown formatting**.\n"
            "- Use a numbered list for questions.\n"
            "- Place the answer right after each question as '**Answer:**'.\n"
            "- Do not include any formatting explanation."
        )
    elif question_type == "long":
        prompt = (
            "Based on the following lecture content, generate **3 long answer questions** with detailed answers.\n"
            "- Use valid **Markdown formatting**.\n"
            "- Number the questions.\n"
            "- Put '**Answer:**' before the answer paragraph.\n"
            "- Do not include any formatting explanation."
        )
    else:
        prompt = (
            "You are a helpful AI assistant. Based on the following lecture content, generate quiz questions as follows:\n"
            "### **1. Multiple Choice Questions**\n"
            "- Create 10 questions.\n"
            "- Use numbered format for questions.\n"
            "- Each option should be a bullet (a), b), c), d)).\n"
            "- Clearly mark the correct answer below using '**Answer:**'.\n\n"
            "### **2. Short Answer Questions**\n"
            "- Create 5 questions.\n"
            "- Use a numbered list.\n"
            "- Include '**Answer:**' directly after each question.\n\n"
            "### **3. Long Answer Questions**\n"
            "- Create 2 questions.\n"
            "- Number them and place '**Answer:**' before the answer paragraph.\n\n"
            "Use valid **Markdown** for formatting throughout. Do not include any explanation of the formatting."
        )

    try:
        response = qa_chain.invoke({"query": prompt})
    except Exception as e:
        return f"Quiz generation failed: {e}", 500

    return response['result']
