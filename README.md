# Retail Inventory RAG Project

This project demonstrates the use of Retrieval-Augmented Generation (RAG) with a SQL database to interact with a retail inventory of T-shirts. The system leverages various technologies to provide natural language interaction with the database.

## Project Overview

The system is designed to enable users to query and interact with a SQL database containing information about T-shirts and discounts. It utilizes advanced language models and vector databases to provide insightful and context-aware responses.

### Technologies Used

- **Gemini 1.5 Flash**: For advanced language model capabilities.
- **LangChain**: To manage the interaction between the language model and the SQL database.
- **Hugging Face Embeddings**: For semantic understanding of text queries.
- **ChromaDB**: As the vector database for storing and retrieving embeddings.
- **SQLDatabase Chain**: From LangChain, to handle SQL queries and integrate with the language model.
- **Streamlit**: For creating the web interface.

### Database Schema

The SQL database used in this project contains the following tables:

- **`t_shirts`**: Contains details about T-shirts.
- **`discounts`**: Contains discount information related to T-shirts.



**Clone the Repository**

   ```bash
   git clone https://github.com/YourUsername/your-repo-name.git
   cd your-repo-name
