import os
import sys
import constants
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI
os.environ["OPENAI_API_KEY"] = constants.APIKEY

query = sys.argv[1]

loader = TextLoader('data.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query, llm=ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")))
#Improved Predictive Analytics
#Customized Recommendations and Personalization
#Enhanced Risk Management
#Optimized Operations and Resource Allocation
#Customer Segmentation and Targeting
#Fraud Detection and Security
#Product and Service Innovation