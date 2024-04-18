!pip install -q --upgrade google-generativeai langchain-google-genai python-dotenv
!pip install langchain
!pip install pypdf
!pip install chromadb

import pathlib
import textwrap
#from IPython.display import display, Markdown
from google.colab import userdata
import google.generativeai as genai

# Retrieve the API key
GOOGLE_API_KEY = userdata.get('Googler')

# Configure generative AI with the API key
genai.configure(api_key=GOOGLE_API_KEY)
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3, google_api_key=GOOGLE_API_KEY)
import urllib
import warnings
from pathlib import Path as p
from pprint import pprint

import pandas as pd

from langchain_community.document_loaders import PyPDFLoader

# Define the path to the data folder
data_folder = p.Path.cwd() / "data"

# Create the data folder if it doesn't exist
data_folder.mkdir(parents=True, exist_ok=True)

# Path to the local PDF file
local_pdf_file = "/content/MCCR_1229_18.pdf"

# Destination path for the PDF file within the data folder
pdf_file = data_folder / local_pdf_file.split("/")[-1]

# Copy the local PDF file to the data folder
p.Path(local_pdf_file).replace(pdf_file)
# Initialize the RecursiveCharacterTextSplitter with specified parameters
text_splitter = RecursiveCharacterTextSplitter(chunk_size=50000, chunk_overlap=0)

# Concatenate page contents into a single string with double line breaks between each page's content
context = "\n\n".join(str(p.page_content) for p in pages)

# Split the concatenated text into chunks using the initialized text splitter
texts = text_splitter.split_text(context)
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import Chroma, FAISS, Pinecone

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)

# Convert the texts into vectors using the provided embeddings
vector_index = Chroma.from_texts(texts, embeddings)

# Convert the vector index into a retriever
vector_index = vector_index.as_retriever()
prompt_template = """
  Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
  provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
  Context:\n {context}?\n
  Question: \n{question}\n

  Answer:
"""

prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

question = "What was the Scheduled Case Activity"

# Set up question-answering chain
chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

# Retrieve relevant documents
docs = vector_index.get_relevant_documents(question)

# Execute the question-answering chain
response = chain({"input_documents": docs, "question": question}, return_only_outputs=True)

# Obtain the answer
answer = response

