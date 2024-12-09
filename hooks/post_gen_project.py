help = """
Your project has been created!
If you have not done so already, create a pyenv environment for your new project with:

cd {{cookiecutter.repo_name}}

uv venv

If you use fish
source ./venv/bin/activate.fish

If you use bash
```source ./venv/bin/activate```

Install your new project in your local environment with:

pip install -e .

You will need to manually add data to .gitignore to prevent it from syncing to
version control.

Don't forget to sync to GitHub. Have fun!

git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin {{cookiecutter.github_username}}/{{cookiecutter.repo_name}}
git push -u origin main

"""
print(help)
