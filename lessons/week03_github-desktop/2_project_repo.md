
# Setting Up Your Final Project Repository

**_Learning Objectives_:**  
1. Learn to create a collaborative project repository from a template
2. Understand project repository structure and organization
3. Practice collaborative Git workflows including branching and pull requests
4. Experience the full cycle of collaborative development using GitHub Desktop<br>
---

### Icons Used in This Notebook 
🔔 **Question**: A quick question to help you understand what's going on.<br>
🥊 **Challenge**: Interactive exercise. We'll work through these in the lesson!<br>
💡 **Tip**: How to do something a bit more efficiently or effectively.<br>
⚠️ **Warning:** Heads-up about tricky stuff or common mistakes.<br>

## Introduction

In this lesson, you'll work in groups to set up a collaborative final project repository. This will give you hands-on experience with real-world collaborative development workflows that you'll use throughout the rest of the course and in your future projects.

## Step 1: Creating Your Project Repository from Template

One person in your group should be designated as the repository owner and follow these steps:

1. **Navigate to the template repository**: Go to the [GitHub repository](https://github.com/compss211/final-project-template-repo) for the final project template.
2. **Create a new repository from template**: Click the green "Use this template" button, then select "Create a new repository"
3. **Choose repository settings**:
   - **Repository name**: Choose a meaningful name that reflects your project (e.g., `climate-data-analysis`, `social-media-sentiment`, `movie-recommendation-system`)
   - **Description**: Add a short, useful description of what your project will accomplish
   - **Visibility**: Keep it public (this allows for easier collaboration)
4. Click "Create repository from template"

💡 **Tip**: Choose a descriptive repository name that clearly indicates your project's purpose. Avoid generic names like "final-project" or "group-3-project".

### Adding Collaborators

Once your repository is created, the owner needs to add all group members as collaborators:

1. **Navigate to repository settings**: In your new repository, click on the "Settings" tab
2. **Go to Collaborators**: In the left sidebar, click "Collaborators and teams"
3. **Add collaborators**: Click "Add people" and enter each group member's GitHub username
4. **Set permissions**: Give collaborators "Write" access (this allows them to push changes directly)

🔔 **Question**: Why do you think we're giving everyone "Write" access instead of requiring pull requests for everything?

⚠️ **Warning**: Make sure all group members have accepted the collaboration invitation before proceeding to the next steps.

## Step 2: Understanding Your Repository Structure

Now let's explore the structure of your project repository. The template provides an organized folder structure that will help keep your project organized throughout the semester:

```
your-project-repo/
├── README.md
├── src/
├── scripts/
├── notebooks/
└── data/
```

### Repository Folders Explained

**`src/` folder**: This is where you'll store **common code** that you'll reuse across multiple parts of your project. Think of this as your project's library of functions, classes, and modules. For example:
- Data cleaning functions that multiple team members will use
- Statistical analysis functions
- Visualization helper functions
- Custom classes for your domain area

💡 **Tip**: We'll study the `src` folder more closely in Week 5!

**`scripts/` folder**: This contains **standalone scripts** that perform specific tasks from start to finish. These are Python files you run directly to accomplish a particular goal. Examples:
- `download_data.py` - downloads and preprocesses your dataset
- `generate_report.py` - creates a final report or summary
- `run_analysis.py` - executes your main analysis pipeline

**`notebooks/` folder**: This is where you'll store **Jupyter notebooks** for exploration, analysis, and presentation. Notebooks are great for:
- Exploratory data analysis
- Creating visualizations
- Documenting your thought process
- Presenting results with narrative text

**`data/` folder**: Store your datasets here, though remember not to commit large data files to git (we'll cover this more in future lessons).

🔔 **Question**: What's the key difference between scripts and notebooks?

- **Scripts** are meant to be run automatically and produce consistent results. They're better for production code, data processing pipelines, and tasks you'll repeat often.
- **Notebooks** are interactive and great for exploration, analysis, and explanation. They combine code, results, and narrative text in one document.


## Step 3: Cloning Your Repository

Now that your repository is set up and all collaborators have been added, everyone in the group needs to clone the repository to their local machine using GitHub Desktop.

**All group members** should follow these steps:

1. **Open GitHub Desktop**: Launch the GitHub Desktop application
2. **Clone the repository**: 
   - Click `File` > `Clone repository from the Internet`
   - Or click the `Clone a repository from the Internet` button if you see it
3. **Find your repository**:
   - Switch to the `GitHub.com` tab
   - Look for your project repository in the list (it should show up under repositories you have access to)
   - Select your repository
4. **Choose local path**: 
   - Choose where you want to store the project on your computer
   - Click `Clone`

**Note**: If you prefer to work in GitHub Codespaces instead of locally, you can set that up later. Note that, if you want to use git, you'll have to do so on the command line. We will study that next week!

⚠️ **Warning**: Make sure everyone successfully clones the repository before moving to the next step. If someone can't see the repository, check that they've accepted the collaboration invitation.

## Step 4: Taking Turns Creating Scripts

Now for some hands-on practice! Each group member will take turns creating a Python script, committing it, pushing the changes, and verifying it appears on GitHub. This exercise will reinforce the basic Git workflow you learned in `1_github_basics.md` and give you practice creating scripts.

### The Exercise Process

**Each group member should take turns doing the following:**

1. **Create a new Python script**:
   - Navigate to your local repository folder
   - Go into the `scripts/` folder
   - Create a new Python file named `hello_[your-name].py` (e.g., `hello_alice.py`)
   - Add this simple content to your script:

```python
"""
A simple hello world script by [Your Name]
"""
name = "[Your Name]"
print(f"Hello from {name}!")
print("This is my first script in our group project.")

# Add a simple calculation
favorite_number = 42  # Change this to your actual favorite number
result = favorite_number * 2
print(f"My favorite number times 2 is: {result}")
```

2. **Commit your changes** (using GitHub Desktop):
   - Open GitHub Desktop
   - You should see your new script file in the "Changes" section
   - Add a descriptive commit message like "Add [your name]'s hello world script"
   - Click "Commit to main"

3. **Push to the remote repository**:
   - Click "Push origin" to upload your changes to GitHub

4. **Verify on GitHub**:
   - Go to your repository on GitHub.com
   - Navigate to the `scripts/` folder
   - Confirm your script appears there
   - Click on your script to see the code displayed


⚠️ **Warning: Pull before you start!** If you're not the first person, make sure to pull the latest changes first (in GitHub Desktop, click "Pull origin" or "Fetch origin")

🔔 **Question**: Why do you think we're having everyone take turns instead of working simultaneously?

## Step 5: Collaborative Workflow

Now that everyone has practiced the basic workflow, let's explore the collaborative workflow using branches and pull requests.


**Each group member should do the following exercise:**

1. **Create a new branch**:
   - In GitHub Desktop, click on "Current Branch" (should show "main")
   - Click "New Branch"
   - Name your branch something descriptive like `[your-name]-feature` (e.g., `alice-feature`)
   - Click "Create Branch"

2. **Make a change**:
   - Edit the `README.md` file in your repository
   - Add a new section at the bottom with your name and a brief description of what you plan to contribute to the project
   - For example:
     ```markdown
     ## Contributors
     
     ### My name
     I will be working on data collection and cleaning for our project.
     ```

3. **Commit your changes**:
   - In GitHub Desktop, you should see your changes to README.md
   - Add a commit message like "Add [your name] to contributors section"
   - Click "Commit to [your-branch-name]"

4. **Push your branch**:
   - Click "Publish branch" (this pushes your new branch to GitHub)

5. **Create a Pull Request**:
   - Go to your repository on GitHub.com
   - You should see a banner saying "Compare & pull request" - click it
   - If you don't see that banner, click "Pull requests" tab, then "New pull request"
   - Make sure the base branch is `main` and the compare branch is your branch
   - Add a title like "Add [your name] to contributors"
   - Add a brief description of what you changed
   - Click "Create pull request"

6. **Review someone else's pull request**:
   - Look at the open pull requests in your repository
   - Choose someone else's pull request to review
   - Click on their pull request
   - Look at the "Files changed" tab to see what they modified
   - Add a comment like "Looks good to me!" in the conversation tab
   - If you're the repository owner, you can click "Merge pull request" to accept it

⚠️ **Warning**: Don't merge your own pull request - have someone else in your group review and merge it for you. This simulates real-world collaborative practices.

## What's Next?

Throughout the rest of the course, you'll use this repository for your final project. Remember:
- Use the `scripts/` folder for standalone programs that accomplish specific tasks
- Use the `notebooks/` folder for exploratory analysis and presentation
- Always use branches and pull requests for significant changes
- Communicate with your team about who's working on what to avoid conflicts
- We'll explore package management and the `src` folder in Week 5!




