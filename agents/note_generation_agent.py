from langchain_google_genai import ChatGoogleGenerativeAI
import pycountry
import os
from dotenv import load_dotenv
import os

load_dotenv()


def get_language_name(lang_code):
    # Try to get the full language name from the code
    lang = pycountry.languages.get(alpha_2=lang_code)
    return lang.name if lang else lang_code


GOOGLE_API_KEY = os.getenv('API_KEY')
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GOOGLE_API_KEY)


def generate_notes_agent(text: str, lang_code: str):
    language_name = get_language_name(lang_code)
    prompt = f"""
You are an expert multilingual AI assistant that processes lecture transcriptions and creates structured, detailed academic notes.

The lecture transcription is in: **{language_name}** (code: {lang_code})

Instructions:

1. **If the language is English**: Generate a single set of detailed lecture notes and a brief English summary.
2. **If the language is Hindi or Urdu (native script)**:
   - Convert to Roman Hindi or Roman Urdu.
   - Generate detailed lecture notes in Romanized script.
   - Also generate equally detailed notes in English.
3. **If the language is any other**:
   - Generate detailed notes in the original language.
   - Also generate equally detailed notes in English.

**In all cases, provide a brief English summary (3–5 sentences).**

**Format**:
- Use valid Markdown with bold headers (with **), numbered lists, and bullet points.
- Do not explain the formatting.
- Use clear, academic language.

Output Format:

Detected Language:
{language_name}

Lecture Notes (Original or Romanized Language):
1. [Detailed point or paragraph]
2. [Detailed point or paragraph]
...

Lecture Notes in English:
1. [Detailed point or paragraph]
2. [Detailed point or paragraph]
...

Brief English Summary:
[3–5 sentence summary]

Input Text:
{text}
"""
    response = llm.invoke(prompt)
    raw_output = response.content

    # Manual parsing (you can improve with regex later)
    result = {
        "language": language_name,
        "converted_text": "",  # default
        "notes_local": "",
        "notes_english": "",
        "summary": ""
    }

    if "Lecture Notes (Original or Romanized Language):" in raw_output:
        parts = raw_output.split("Lecture Notes (Original or Romanized Language):")[1]
        local, english_and_summary = parts.split("Lecture Notes in English:")
        result["notes_local"] = local.strip()

        if "Brief English Summary:" in english_and_summary:
            english, summary = english_and_summary.split("Brief English Summary:")
            result["notes_english"] = english.strip()
            result["summary"] = summary.strip()
        else:
            result["notes_english"] = english_and_summary.strip()

    return result
    # return response.content


# print(generate_notes_agent(" In this video, I will tell you what deep learning is, why popular is happening and how many years have you been deep learning? You guys have heard about AI that you have heard about data science, but many people have also been deep learning about this. What is going to happen? How is the option of this? In this video, we will talk about this in detail. Let's get started. So, here deep learning is a subset of AI and artificial intelligence. When we talk about machine learning, and when we talk about deep learning, then there are different mentaly, little differences. In this, I will tell you about it. When we talk about machine learning, we talk about mathematical algorithms, which are data that the machine is using. That data is used in the future in the future. For example, if you are a doctor, and a cat, if you are a algorithm, then you can tell us what is a doctor or a cat. So, you can apply a vast classification, you can do a regression, for example, house price prediction. If you have a lot of data, like this, how many rooms are in the room, how many rooms are in the size of the space. And after that, you can get a new set of features. So, you can train this data, and your model, which is not the new features of the new features. Deep learning is a different comparator. Deep learning is inspired by human brains. Our brain is a new rons. This new rons information process and the new impulses are in a cell cell for a long time. Manloha, our brain is a very complex pattern. Whenever we talk about learning algorithm, we will assume that our data is using one function, which we can see in the features of the function, we can get the label output. For example, if you are a house price prediction, then you can get a feature in a house, which is in the output and you can get the output. So, we have to trap that function, which we can get the features and output in the output. Deep learning is about target, that we can approximate this complex function. And we can approximate this function, so we use series of layers. Every layer is in our neurons, every neuron is corresponding to the corresponding value. One layer can be a neuron in one layer, and our path can be completely layers. So, we take a multi layer neural network, which we can calculate all these things in this manner. This neural network can be built, and we feed it into the data feed. And we create our weights in feedback. As we update our weights, our function is actually ideal function, which is present in the data that we present in the data. And our target is in our deep learning, which we can create a function in the correct way. Which we give our neural networks in our neural networks, which are our weights, which we adjust properly, and our function can be represented accurately. We create all weights in this manner, which we get a function, which will be input in the data input in the data input layer, and finally, we will get the labels out of the data. And for us, we have to progress in a very long time. Now, this video I want to make a quick review of its feed for neural network and back provision. I will discuss some more videos on this video. But there are high level areas here. Now, let's talk about why this is popular in today's video. This is a very poor technique. So, why is this popular in today's video? I will tell you that today's video is good for us in a good way. It is good for us to make a good GPU. One time, it was very good for us to make a good GPU. And the good GPU that was used today was which was the only option of the average person in today's video. So, the high computer that was used today was in a very long time. When I compute I mean CPU, RAM and GPUs, in today's video, GPU CPUs, CPUs, CPUs, this technology is going to be very good in this technology. This technology is going to be very good in this technology. It is going to be very good in this technology. It is going to be very good in this technology. And it is going to be very good in this technology. It is going to be a time for us to make a good run. Because it is going to be hard for us to support that experiment. And today, we are going to discuss some of the things that we have to start our daily lives in the future. Now, I am very pleased with you guys. It is a very high level. What you have to do is to create a very variable variable. You have to start a new life in this country. Our boss is very happy in this country. We will discuss all the new lives in this country. For example, TensorFlow, PyTorch, Cafes1, Microsoft's cognitive toolkit. And it is a default JS. And our boss is very happy in this country. And we are going to start this new life in this country. So today, I have been very happy with the new network. So I will share with you all the libraries. You start your journey and start coding. If you do this, you will be interested. Now, let us talk about its average salary. So, an entry level, deep learning engineer, India's India-Kamsekam is in India. And I am talking about this fresher. We are talking about this salary on paras. If we talk about non-tech giant companies, and when you are taking tech giant companies, there are some experience taking tech. Now, this salary is a crore per annum. I am very pleased with the deep learning job. So, that is all about deep learning. You have to enjoy this video. You have enjoyed this video. Now, let us watch this video. Thank you so much. You guys watching this video. And I will see you next time.","hi"))
