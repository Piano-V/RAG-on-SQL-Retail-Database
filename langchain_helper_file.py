import logging
from transformers import pipeline
import mysql.connector
import chromadb
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate
import os
from few_shots import few_shots
from my_sql_prompt import mysql_prompt
from dotenv import load_dotenv

load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_chain():
    try:
        api_key = os.environ["GOOGLE_API_KEY"]
        llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key)
        logger.info("Loaded GoogleGenerativeAI with provided API key")

        db_user = "root"
        db_password = "root"
        db_host = "localhost"
        db_name = "atliq_tshirts"

        db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", sample_rows_in_table_info=3)
        logger.info("Connected to the SQL database")

        embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
        logger.info("Loaded HuggingFace embeddings")

        to_vectorize = [" ".join(example.values()) for example in few_shots]
        vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=few_shots)
        logger.info("Created vectorstore from few shots examples")

        example_selector = SemanticSimilarityExampleSelector(
            vectorstore=vectorstore,
            k=2,
        )
        example_selector.select_examples({"Question": "How many black color NIKE shirts do we have that are bigger than Large?"})
        logger.info("Example selector initialized")

        example_prompt = PromptTemplate(
            input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
            template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
        )

        few_shot_prompt = FewShotPromptTemplate(
            example_selector=example_selector,
            example_prompt=example_prompt,
            prefix=mysql_prompt,
            suffix=PROMPT_SUFFIX,
            input_variables=["input", "table_info", "top_k"],
        )
        logger.info("FewShotPromptTemplate created")
        chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt, use_query_checker=True)
        logger.info("SQLDatabaseChain created")
        return chain
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    chain = get_chain()
    print(chain.invoke("How many total t shirts are left in total in stock")['result'])
