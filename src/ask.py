from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.globals import set_llm_cache
from langchain_community.cache import SQLiteCache

set_llm_cache(SQLiteCache(database_path="./.cache/.langchain.db"))


def load_llm(model="gpt-3.5-turbo-instruct",n=2):
    set_llm_cache(SQLiteCache(database_path="./.cache/.langchain.db"))
    llm = OpenAI(model_name=model, n=n, best_of=n)
    return llm

def ask(llm, question="Tell me a joke",model="gpt-3.5-turbo-instruct",n=2):
    set_llm_cache(SQLiteCache(database_path="./.cache/.langchain.db"))
    answer = llm.invoke(question).strip()
    return answer