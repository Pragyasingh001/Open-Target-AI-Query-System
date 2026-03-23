import requests
import json
import re

OPEN_TARGETS_URL = "https://api.platform.opentargets.org/api/v4/graphql"


def execute(query: str) -> str:
    """
    Clean GraphQL query, send it to Open Targets API,
    and return JSON response as string.
    """

    #clean query 
    if not query:
        return json.dumps({"error": "Empty query"}, indent=2)

    # Remove markdown ```graphql ```
    query = re.sub(r"```.*?\n", "", query)
    query = query.replace("```", "").strip()

    # -------- Call API --------

    try:
        response = requests.post(
            OPEN_TARGETS_URL,
            json={"query": query},
            timeout=30
        )
        print("Status Code:", response.status_code)
        if response.status_code == 200:
            print("-----------------API call successful-----------------")
            print(response.json())   # actual data
        else:
            print("API failed")

        response.raise_for_status()

        return json.dumps(response.json(), indent=2)

    except Exception as e:
        return json.dumps({"error": str(e)}, indent=2)