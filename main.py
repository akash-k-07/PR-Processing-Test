import json

# Load test PR data from JSON file
with open("test_pr.json", "r") as file:
    pr_data = json.load(file)

print(f"Processing PR #{pr_data['pull_request_id']} for repository {pr_data['repository_name']}.")
for file in pr_data["changed_files"]:
    print(f"File: {file['file_name']} - Changes: {file['changes']}")
