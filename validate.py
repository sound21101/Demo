import requests

def test_github_graphql_token(token):
    url = "https://api.github.com/graphql"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    query = """
    query {
      viewer {
        login
      }
    }
    """
    
    response = requests.post(url, json={"query": query}, headers=headers)
    
    if response.status_code == 200:
        print("Token is valid!")
        return True
    else:
        print("Token authentication failed")
        return False

# Use your personal access token
test_github_graphql_token('xyz')