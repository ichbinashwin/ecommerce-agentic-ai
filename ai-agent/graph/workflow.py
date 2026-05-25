from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END
from typing import TypedDict
import json

from tools.product_api import get_products


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


class AgentState(TypedDict):
    user_input: str
    products: list


def extract_filters(user_query):

    prompt = f"""
    Extract product search filters from user query.

    Return ONLY valid JSON.

    Possible fields:
    - brand
    - category
    - min_price
    - max_price

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

    try:
        filters = json.loads(response.content)
    except:
        filters = {}

    return filters


def apply_filters(products, filters):

    filtered = products

    if "brand" in filters:

        filtered = [
            p for p in filtered
            if filters["brand"].lower()
            in p["brand"].lower()
        ]

    if "category" in filters:

        filtered = [
            p for p in filtered
            if filters["category"].lower()
            in p["category"].lower()
        ]

    if "max_price" in filters:

        filtered = [
            p for p in filtered
            if p["price"] <= filters["max_price"]
        ]

    if "min_price" in filters:

        filtered = [
            p for p in filtered
            if p["price"] >= filters["min_price"]
        ]

    return filtered


def product_agent(state):

    products = get_products()

    user_query = state["user_input"]

    filters = extract_filters(user_query)

    filtered_products = apply_filters(
        products,
        filters
    )

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