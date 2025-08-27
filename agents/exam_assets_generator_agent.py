from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv('API_KEY')

def generate_assets(vectorstore, combined_text, asset_type="quiz"):
    # Map asset type to total marks
    marks_map = {
        "quiz": 10,
        "mid": 30,
        "final": 40
    }
    total_marks = marks_map.get(asset_type.lower(), 10)

    prompt = rf"""
You are a university-level exam content generator. Your task is to create a comprehensive **{asset_type}** exam paper totaling {total_marks} marks using the following inputs:

1. **Lecture Transcript and Supplementary Materials:** Use the provided transcript and the uploaded materials for factual accuracy and question generation.
2. **CLOs/PLOs:** Align each question explicitly with the relevant Course Learning Outcomes (CLOs) and Program Learning Outcomes (PLOs).

**Instructions:**
- Return only clean Markdown output.
- Distribute the {total_marks} marks appropriately over the questions.
- Clearly state the points allocated for each question.
- Use single-level numbering for questions starting at 1.
- Use bullet points for multiple choice options.
- Provide a variety of question types (MCQs, short answer, long answer).
- Each question must reference the specific CLO it is testing, e.g., "(CLO 1)".
- Use consistent bold headers for sections (e.g., **Part A: Multiple Choice Questions**).
- You may include LaTeX math expressions only if the output format supports it.
- If output format does NOT support LaTeX, convert math formulas into clear, concise plain English explanations.
- Do not include any explanations about formatting or instructions in the output.

---
{combined_text}

Now begin generating the exam asset.
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
