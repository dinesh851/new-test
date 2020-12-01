import subprocess

# Replace these with your repository URL and branch name
repository_url = "https://github.com/dinesh851/new-test"
branch_name = "update-readme"  # Change this to a unique branch name

# Specify the date for the commit
commit_date = "2020-12-01T12:00:00"

# Make changes to the README file
readme_content = "Added new content"
with open("README.md", "a") as readme_file:
    readme_file.write(readme_content + "\n")

# Git commands
commands = [
    f'git add .',
  
    f'git add README.md',
    f'git commit --date="{commit_date}" -m "Update README with new content"',
    f"   git push --set-upstream origin main  "
    f"   git push "
]

# Execute commands
for command in commands:
    subprocess.run(command, shell=True)
