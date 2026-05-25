from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END
from typing import TypedDict
import json

#from tools.product_api import get_products
from tools.product_api import search_products

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

class AgentState(TypedDict):
    user_input: str
    products: list

def extract_filters(user_query):

    prompt = f"""
    Extract ecommerce product filters from user query.

    Return ONLY valid JSON.

    Allowed fields:
    - brand
    - category
    - min_price
    - max_price

    Normalize categories:
    - laptops -> Laptop
    - phones -> Phone
    - headphones -> Headphones

    User Query:
    {user_query}

    Example Output:

    {{
        "brand": "Apple",
        "category": "Laptop",
        "max_price": 1500
    }}
    """

    response = llm.invoke(prompt)

    content = response.content.strip()

    # REMOVE MARKDOWN JSON BLOCKS
    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    print("\n===== GEMINI FILTER RESPONSE =====")
    print(content)
    print("==================================\n")

    try:

        filters = json.loads(content)

    except Exception as e:

        print("JSON ERROR:", e)
        filters = {}

    return filters

def product_agent(state):
    user_query = state["user_input"]
    filters = extract_filters(user_query)
    filtered_products = search_products(filters)
    return {
        "products": filtered_products
    }

graph = StateGraph(AgentState)

graph.add_node(
    "product_agent",
    product_agent
)

graph.set_entry_point(
    "product_agent"
)

graph.add_edge(
    "product_agent",
    END
)

app = graph.compile()
