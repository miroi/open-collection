import requests
import urllib.parse

# 1. Define project specifics
PROJECT_PATH = "dirac/dirac"
DEFAULT_BRANCH = "master"  # Change to "main" or a specific branch/tag if needed
encoded_path = urllib.parse.quote_plus(PROJECT_PATH)

# 2. Build the initial GitLab API URL (fetching 100 items per page recursively)
url = f"https://gitlab.com/api/v4/projects/{encoded_path}/repository/tree"
params = {
    "recursive": "true",
    "per_page": 100,
    "page": 1
}

file_links = []

print("Fetching file tree from GitLab...")
while url:
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    items = response.json()
    if not items:
        break
        
    for item in items:
        # 'blob' represents actual files (ignores directories)
        if item["type"] == "blob":
            file_path = item["path"]
            # Construct the web view link
            web_link = f"https://gitlab.com/{PROJECT_PATH}/-/blob/{DEFAULT_BRANCH}/{file_path}"
            file_links.append(web_link)
            
    # Check if a next page exists via GitLab's response headers
    if "X-Next-Page" in response.headers and response.headers["X-Next-Page"]:
        params["page"] = int(response.headers["X-Next-Page"])
    else:
        url = None  # Loop ends when there is no next page

# 3. Print or save the links
print(f"Successfully retrieved {len(file_links)} file links.\n")
# Print first 10 links as a sample
for link in file_links[:10]:
    print(link)

# 4. Save the links into a text file
output_filename = "dirac_file_links.txt"
with open(output_filename, "w", encoding="utf-8") as f:
    for link in file_links:
        f.write(link + "\n")

print(f"\nAll links have been successfully saved to '{output_filename}'")

