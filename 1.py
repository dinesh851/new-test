import subprocess
from datetime import datetime

# Specify the date for the commit
commit_date = "2022-12-01T12:00:00"

# Make changes to the README file
readme_content = "Added new content"
with open("README.md", "a") as readme_file:
    readme_file.write(readme_content + "\n")

# Git commands
commands = [
    'git add .',
            
    'git add README.md',
    f'git commit --date="{commit_date}" -m "Update README with new content"',
    f'git commit  -m "Update README with new content"',
    'git push  '  # Change 'main' to your default branch name if different
]

# Execute commands
for command in commands:
    subprocess.run(command, shell=True)
