from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv('API_KEY')

def generate_assets(vectorstore, clos_text, asset_type="quiz"):
    """
    Generates quiz, mid, final, or assignment based on vectorstore and CLOs/PLOs using Gemini LLM.
    Returns formatted Markdown.
    """
    prompt = f"""
You are a university-level exam content generator. Your task is to create a comprehensive **{asset_type}** using:

1. **Lecture Content:** Extracted from a Vector Database (use it for factual accuracy).
2. **CLOs/PLOs:** Use these to align questions with intended learning outcomes.

**Instructions:**
- Return only Markdown-formatted output.
- Use clear sections with bold headers (e.g., **Part A: Multiple Choice Questions**).
- Include a variety of question types (MCQs, short, long, fill-in-the-blanks if applicable).
- Do not explain the formatting or instructions.

---
**CLOs/PLOs:**
{clos_text}

Now begin using the retrieved lecture content.
"""

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GOOGLE_API_KEY
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    response = qa_chain.invoke({"query": prompt})
    return response['result']

