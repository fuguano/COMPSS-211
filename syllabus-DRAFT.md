# COMPSS 211: Advanced Computing I Syllabus \- Fall 2025

## Course Information

* **Schedule:** 3 hours weekly; 90’ lecture, 90’ lab  
* **Location:** In-person (2121 Allston Way, 2nd floor classroom)  
* **Instructor:** Tom van Nuenen, [tomvannuenen@berkeley.edu](mailto:tomvannuenen@berkeley.edu)  
* **GSI:** Arul Murugan Renganathan, [arul@berkeley.edu](mailto:arul@berkeley.edu)   
* **Office Hours:** To be communicated in class  
* **Units:** 3 units (letter graded)  
* **Prerequisites:** A passing grade (C+ or better) in COMPSS 201 or a passing grade on the waiver exam. 

## Course Description

COMPSS 211 is a hands-on, advanced computing course for master’s students in computational social science. We focus on practical tools and techniques in Python to collect, manage, and analyze textual data at scale. Key topics include:

* **Local Computing:** Command-line operations and version control with Git / Github.  
* **Data Acquisition:** Using web APIs to retrieve data and web scraping/crawling to collect data when APIs aren’t available.  
* **Deployment / Remote Computing:** Working with cloud and container technologies – for example, launching computations on Google Cloud and using Docker for reproducible environments.   
* **Natural Language Processing (NLP):** Fundamental text processing and analysis techniques for social science data.  
* **Coding in the Age of LLMs:** Integrating Large Language Models (like GPT) into the coding workflow. Students will learn how to prompt AI coding assistants and critically evaluate and debug AI-generated code.

Throughout the course, students will apply these skills to real-world computational social science problems. We will use datasets to practice methods and ultimately drive a final project that tells a social science story with data. By the end, students will be equipped to fetch data from diverse sources, manage code collaboratively, leverage AI and cloud tools, and build end-to-end computational workflows.

## Learning Outcomes

By the end of this course, students will be able to:

* **Use Unix command-line (Bash/Zsh)** to navigate files, automate tasks, and manage Python environments on local and remote systems.  
* **Employ Git and GitHub for version control**: manage repositories, track changes, branch and merge code, and collaborate on coding projects.  
* **Acquire data from the web** via authenticated APIs and by web scraping when necessary. Students will understand how to parse data from web services and how to scrape HTML content with tools like Requests and BeautifulSoup, while respecting legal and ethical guidelines.  
* **Process and analyze text data using NLP**: students will learn about NLP operations including cleaning/tokenizing text, creating bag-of-words/TF-IDF representations, learning about static word embeddings and working with large language models. Students will grasp differences between approaches, computing similarity measures, and be aware of bias in language models.  
* **Integrate Large Language Models (LLMs) into coding tasks**: throughout the course, students will use prompting techniques to have an AI assistant generate or explain code, while critically evaluating the output. Students will practice debugging AI-generated code and understand limitations spread across each week of the course.  
* **Utilize cloud and container tools**: run analyses in remote environments (Google Cloud) store data in cloud storage, and containerize applications with Docker for reproducibility.  
* **Undertake a full-cycle computational social science project**: from data acquisition and cleaning to analysis and presentation, using a text-based dataset. This includes formulating a research question, applying appropriate computational methods, and interpreting results in a social science context.

## Course Materials and Resources

All required materials are open-access. There is **no required textbook**. Instead, we will use online readings, tutorials, and repositories (favoring UC Berkeley D-Lab materials and GitHub resources):

* **Computing Platform:** We will use Jupyter Labs on Datahub, as well as VSCode for hands-on exercises and AI help.  
* **Git and GitHub:** Install Git on your machine and set up a GitHub account. We will set up a Github Education account (Settings \-\> Billing and licensing \-\> Education benefits).   
* **Cloud Accounts:** Students will sign up for a Google Cloud account for the cloud computing module.   
* **Readings & Tutorials:** Weekly readings will be provided on bCourses.

## Assignments and Evaluation Components

Your performance will be evaluated through a combination of hands-on assignments, participation, and a final project. Approximate weightings are:

* **Participation & Attendance – 10%:** Active participation in class discussions, in-class exercises, and attendance. *See attendance policy below.*  
* **AI-Generated Code Analysis Journal – 20%:** Students maintain a collection of AI-generated code examples (from ChatGPT, Claude, Copilot, etc.) with critical analysis, in a git repo based on [this git template](https://github.com/dlab-berkeley/ai-journal-starter). Students are encouraged to treat this journal as a messy, honest lab log of how they worked with AI tools during the course.   
  ***Requirements:***  
  * At least 8 code examples from different AI tools and contexts  
  * Variety of tasks: data scraping, NLP analysis, API calls, text processing, etc.  
  * For each example, students document:  
    * The original prompt they used  
    * The AI's output (with screenshot/copy)  
    * What worked well vs. what didn't  
    * Any bugs they found and how they fixed them  
    * Alternative approaches they tried  
    * Reflection on when AI help was/wasn't appropriate  
  * The 8 journal entries should include at least 1 example each of the following categories:  
    * code generation from prompt  
    * data cleaning or preprocessing  
    * exploratory data analysis or visualization  
    * API interaction  
    * web scraping or data collection  
    * text analysis or NLP  
    * LLM evaluation, critique, or debugging  
    * free choice  
* **Homework Assignments – 30%:** 7 assignments (individual unless noted) reinforcing weekly skills. These will involve coding tasks and short write-ups. Each homework assignment will be posted with instructions and is due one week later (unless otherwise specified). Detailed prompts in the Course Schedule.  
* **Final Project – 40%:** A team-based data analysis project that applies course concepts to a dataset of your choice. Students will work in small teams (2-3 students max) to pose a research question, analyze the data using methods from the course, and present their findings. Much work in industry is done in groups, so team assignments are good preparation for that kind of work. To ensure fairness and individual accountability, several components will be completed individually, even within the group project structure.  
  * ***Team Proposal (5%):*** A 1–2 page proposal due mid-semester (Week 6\) outlining your research question, planned methods, and a clear division of responsibilities among team members. Feedback will be provided to guide your project.  
  * ***Individual Progress Memo (5%):*** A short personal reflection submitted during Week 12 detailing your individual contributions so far, any challenges encountered, and your plans for the remainder of the project.  
  * ***Final Report & Code (20%):*** A collaboratively written report (5–8 pages) and a shared GitHub repository documenting your project. The report should cover your research question, data, methods, results, discussion, and social science implications. It must be clear, reproducible, and well-organized.  
  * ***Individual Appendix (5%):*** Each student will submit a brief appendix (1–2 pages) alongside the final report describing their specific contributions—this may include code snippets, analysis steps, or reflection on what they learned. This ensures everyone is evaluated on their own work as well as the team’s outcome.  
  * ***Final Presentation (5%):*** A 10-minute group presentation during the final week. All group members must participate and present a distinct portion of the project.

**Grading Rubric:**

| Grade | Description | Code quality | Analysis & methodology | Interpretation & iInsight | Communication & clarity | Contribution (group work) |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **A (90–100%)** | **Outstanding** work that surpasses expectations. | Code is correct, efficient, and well-organized; follows best practices and uses appropriate libraries. | Methods are appropriately chosen and correctly applied; clear understanding of statistical or computational logic. | Demonstrates critical thinking and originality; makes connections to broader context or implications. | Writing and/or presentation is clear, concise, well-structured, and polished; excellent use of visuals/tables. | Active and meaningful contribution; took ownership of tasks and added value beyond the minimum. |
| **B (80–89%)** | **Good** work that meets all core requirements. | Code is mostly correct with minor errors; reasonably efficient and readable. | Analysis is generally correct with small gaps in logic or depth. | Shows understanding but may lack depth or originality; interpretation is sound but not insightful. | Mostly clear communication with a few awkward or unclear sections. | Contributed adequately to team; fulfilled responsibilities but without standout engagement. |
| **C (70–79%)** | **Satisfactory** but with clear room for improvement. | Code contains errors or inefficiencies; difficult to follow in parts. | Some misapplication or misunderstanding of methods. | Basic interpretation present but lacks nuance or context. | Communication is disorganized, imprecise, or too brief to be effective. | Limited participation or unclear role in group output. |
| **D (60–69%)** | **Unsatisfactory** – incomplete or flawed work. | Code frequently fails to run or is poorly structured. | Major methodological errors or missing analysis. | Misinterprets results or fails to connect findings to the research question. | Poorly written or hard to understand; key sections missing. | Minimal involvement in team; contributed little of substance. |
| **F (\<60%)** | **Failing** – did not meet basic standards or was not submitted. | Code is missing or irrelevant. | No real attempt at analysis. | No meaningful interpretation. | Incomplete or incoherent submission. | No demonstrable contribution to group work |

Plus/minus grading will be used for final letter grades. Each assignment and project component will come with specific point allocations and criteria. Final numeric scores will be rounded to nearest percent and converted to letter grades per standard scale.

## Course Schedule 

Below is a **week-by-week schedule** of topics, readings, activities, and due dates. (Schedule subject to minor updates; any changes will be announced in advance.)

### Week 1: Introduction & Recap

**Topics:** Course overview and motivation for computational social science. Setting up your computing environment. Recap of Pandas and basic Python programming.

**In-Class Activities:**

* **Icebreaker:** Discuss in pairs how computing is used in your social science field; share examples with class.  
* **Hands-On Exercise:** Pandas  

**Assignments:**

* **HW0: Environment Setup (ungraded checkpoint)** – By end of Week 1, ensure you have Python, Git, and VSCode installed if you are working locally, and can access either local Jupyter notebooks or Codespaces. 

### Week 2: Coding with LLMs 

**Topics:** We cover how Generative AI (GitHub Copilot) can assist in writing and understanding code. We cover a short introduction to Large Language Models (LLMs) and how to critically review AI-generated code. We will cover how to do a small LLM-powered data project. 

**Readings:**

* *Reading:* “GitHub Blog: “Using GitHub Copilot in your IDE” – [Link](https://github.blog/developer-skills/github/how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices) – introduction to copilot.  
* *Reading:* “Anthropic: “Prompt Engineering Overview” – [Link](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) – guide to prompting strategies.  
* *Reading:* “Google: “Prompt Design Strategies” – [Link](https://ai.google.dev/gemini-api/docs/prompting-strategies) – more prompting strategies.

**In-Class Activities:**

* **Live Demo:** Instructor shares a Jupyter notebook with a few coding tasks. First, we solve one manually (reviewing logic). Then we ask ChatGPT (via the OpenAI API or interface) to generate the code for one of these exercises. We run the AI-generated code, possibly uncover a bug or edge-case it missed.  
* **Discussion:** Collect do’s and don’ts: e.g., do provide context and desired output format, don’t ask for too much at once, always test the code. We emphasize that using LLMs can speed up coding **if** you understand the code it produces – aligning with our course goal of *understanding underlying code*, not just copy-paste.  
* **Ethics/Policy Note:** Clarify course policy on AI use: Students *may* use LLMs as assistants on assignments *only if* they document it (e.g., in a code comment, “Used ChatGPT to help write this function”) and must personally verify and understand the solution. Remind that unacknowledged use or blindly using AI output that leads to plagiarism or incorrect work is against academic integrity.

**Assignments:**

* **AI-Generated Code Analysis Journal:** Create your first journal entry. Include:  
  * The original prompt they used  
  * The AI's output (with screenshot/copy)  
  * What worked well vs. what didn't  
  * Any bugs they found and how they fixed them  
  * Alternative approaches they tried  
  * Reflection on when AI help was/wasn't appropriate

### Week 3: (Virtual) Computing Environments

**Command-line fundamentals** – navigating directories, running Python scripts from terminal, managing files. Basic shell commands (ls, cd, pwd, grep, etc.), and writing a simple bash script.

**Readings:**

* *Reading*: The Unix Shell (Software Carpentry lesson) – [Link](http://swcarpentry.github.io/shell-novice/) – *Sections 1–3* (files/directories and basic commands). 

**In-Class Activities:**

* **Live Demo:** Instructor-led walkthrough of using the terminal to find and open a file, and run a simple Python “Hello World” script from the command line.  
* **Hands-on Exercise:** Students practice a list of shell tasks (provided as a worksheet): e.g., create a folder, navigate to it, make a file, search within a file. Helpers will circulate for troubleshooting.  
* **Discussion:** Why use the command line? Brainstorm benefits for automation and remote computing (ssh, servers) – ties into later cloud topics.

**Assignments:**

* **HW1 Assigned:** *“Bash & Git warm-up.”* (Due Week 3\) – Task: write a short bash script that automates a task (provided scenario) and initialize a Git repo for it.

### Week 4: Version Control with GitHub Desktop

**Topics:** **Git Fundamentals** – tracking changes, committing, pushing to GitHub, branching and merging. Collaboration workflows (pull requests, resolving merge conflicts). We will use command-line Git and also demonstrate GitHub’s interface.

**Readings:**

* *Reading:* Github, “What is Git?” – [Link](https://github.blog/developer-skills/programming-languages-and-frameworks/what-is-git-our-beginners-guide-to-version-control/#:~:text=What%20is%20Git%3F%20Our%20beginner%E2%80%99s,guide%20to%20version%20control) – explains Git managing a working directory, staging area and repository.  
* *Reading:* Dariah, “Git Version Control via Command Line” – [Link](https://campus.dariah.eu/resources/hosted/git-version-control-via-command-line) – highlights Git’s purpose for tracking changes in text files and facilitating collaboration

**In-Class Activities:**

* **Demo:** Initializing a Git repo, making commits, and pushing to GitHub live. Instructor will intentionally create a merge conflict and resolve it in front of class, explaining each step.  
* **Pair Exercise:** In pairs, students create a shared repo (or use our provided “Git Playground” repo). Each partner makes changes on separate branches and attempts to merge, encountering a fake conflict set up by the instructor. Pairs work through conflict resolution with guidance.  
* **Discussion:** Version control best practices (commit frequently with meaningful messages, use .gitignore, etc.). Share horror stories of “collaborating via emailing code” and how Git solves them.

**Assignments:**

* **HW1 Due:** *Bash & Git warm-up* – submit your bash script and a link to your GitHub repo (should contain at least 3 commits).

### Week 5: Version Control on the Command Line

**Topics**: Advanced Git usage via command line; staging, diffing, inspecting logs, undoing changes, and rebasing. Deeper understanding of Git internals (HEAD, staging area, working directory). How to recover from mistakes.

**Readings/Videos**:

* *Reading*: Atlassian Git Tutorial: Advanced Git Commands *–* [Link](https://www.atlassian.com/git/tutorials/advanced-overview) –   
* *Video*: “How Git Actually Works” (The Coding Train or similar \~10–15 min explainer)

**In-Class Activities**:

* **Live Demo**: Instructor will walk through a common Git workflow on the terminal:  
  1. git init, git status, git add, git commit, git log, git diff, git reset, and git checkout  
  2. Introduce HEAD, origin, and main visually with a whiteboard or diagram  
  3. What happens when you git reset vs. git revert?  
  4. When to use rebase vs. merge, and how to avoid messing up shared history.

* **Hands-on Terminal Challenge**: Students will be given a misconfigured repo and must:  
  1. Inspect what’s wrong using git status and git log  
  2. Revert a mistaken commit  
  3. Create and rebase a branch

**Assignments**:

* **HW2 Assigned**: *“Git Troubleshooting Lab”* – You’ll be given a broken repo and a list of problems to solve using Git commands. Tasks include recovering deleted files, resolving a detached HEAD state, and rewriting commit messages. Submit a write-up explaining each fix.

### Week 6: Data Acquisition through Web APIs

**Topics:** **Web APIs** – What are RESTful APIs and how to interact with them using Python. Authentication (API keys, tokens) and rate limiting. JSON data format and parsing in Python (using requests and json libraries). Case study: New York Times Article Search API – students will practice querying the NYT API for news articles on a topic (e.g., climate change or social unrest).

**Readings:**

* *Reading:* Official NYTimes API Documentation – [Link](https://developer.nytimes.com/docs/articlesearch-product/1/overview) – skim to understand endpoints, query parameters, and examples.

**In-Class Activities:**

* **Short Lecture:** Introduction to web services and REST principles (endpoints, methods GET/POST, response codes). Emphasize how many social data providers (Twitter, NYT, etc.) offer APIs for researchers.  
* **Live Coding:** Instructor walks through a simple API call using requests to the NYT API (with a pre-obtained API key) in a Jupyter notebook. We examine the JSON result structure and extract specific fields (headline, date, etc.).  
* **Hands-On Lab:** Students (individually or pairs) pick one of a few provided API options and make a query from Python. Guided tasks: change the query parameter (e.g., search a different keyword or fetch data for a different year), then parse and print a summary (e.g., top 5 results titles). TAs will help troubleshoot common issues (authentication, malformed URLs).   
* **Discussion:** Challenges in using APIs – rate limits, data cleaning after JSON, API deprecations. Mention how if an official API isn’t available or is restricted, we might resort to scraping (segue to next week).  
* **Possible APIs to use:**  
  * Reddit API / PRAW  
  * NewsAPI  
  * semantic scholar  
  * World Bank Data API

**Assignments:**

* **HW2 Due**: *“Git Troubleshooting Lab”* – Submit a write-up to bCourses explaining each fix.  
* **HW3 Assigned:** *“Remote Data via APIs.”* (Due Week 6\) – You will use a public API to fetch data and process it.

### Week 7: Web Scraping and Crawling

**Topics:** **Web Scraping** – Downloading web pages and extracting information when no convenient API is available. Tools: Python’s requests for HTTP and BeautifulSoup for parsing HTML. We’ll also touch on web crawling basics (following links automatically) and briefly mention frameworks like Scrapy for larger projects. Ethics & Legalities: Terms of Service, robots.txt, and respecting privacy. Using LLMs to help you scrape.

**Readings/Videos:**

* *Reading:* “The Web Scraping Handbook – Chapter 1” (by *Kevin Kumler*) – [Link](https://www.parsehub.com/blog/web-scraping-handbook/) – covers basics of HTML structure and scraping tips.  
* *Documentation:* Beautiful Soup 4 Documentation – [Link](https://beautiful-soup-4.readthedocs.io/en/latest/#quick-start) – focus on the quick-start and searching by tag/class.  
* *Video*: “Am I Going to jail for web scraping?” [YouTube](https://www.youtube.com/watch?v=8GhFmQPZAlo), Fireship.  
* *Video:* “Scraping Data from a Real Website” [YouTube](https://www.youtube.com/watch?v=8dTpNajxaH0), Alex the Analyst.

**In-Class Activities:**

* **Case Study Discussion:** Discuss web scraping by LLM companies.  
* **HTML Crash Course:** Briefly explain HTML DOM structure (using an example page). Identify elements by tag, id, class. The instructor uses the browser inspector on a live webpage to show the source.  
* **Live Coding:** Demonstrate scraping a real site (chosen in advance for accessibility, e.g., scraping a few entries from a public forum or a news site’s public articles list). Write a Python snippet to fetch the page and parse a specific element (like article titles or links). Show how to use developer tools to find the right selectors.  
* **Hands-On Practice:** Working in small groups, students attempt to retrieve the content using BeautifulSoup. TAs/instructor assist and share solutions.  
  * [https://quotes.toscrape.com/](https://quotes.toscrape.com/)    
  * [http://books.toscrape.com](http://books.toscrape.com)  
* **Prompt Workshop:** Break into small groups; each group is given a small coding task (e.g., “scrape tweets from a webpage and calculate sentiment” or “compute centrality measures on an email network graph”). Each group devises a prompt to ask an LLM for help. They also think of at least one *test* to verify the LLM’s output. Groups share their prompt and results: Did the LLM deliver correct code?   
* **Ethics Quiz:** Quick slideshow of scenarios – “Is it OK to scrape this? Why or why not?” (e.g., scraping a site that explicitly forbids it vs. a government public data site). Students vote thumbs up/down and justify.

**Assignments**

* **HW3 Due:** *Remote Data via APIs* – submit your code and a short summary of the data you retrieved (e.g., how many records, interesting finding).  
* **HW4 Assigned:** *“Web Scraping Mini-Project.”* – Scrape data from a website of your choice (options provided if you need inspiration, or choose your own with approval). Collect a dataset (e.g., a table or list of items), save it (CSV or JSON), and write a short analysis (even just basic stats or visualization) from that data. Ensure you abide by robots.txt and document your process.

### Week 8: NLP 1: Fundamentals

**Topics:** **Natural Language Processing Fundamentals** – We pivot to analyzing textual data, a common form of social data. This week focuses on text preprocessing (tokenization, stopword removal, stemming), constructing representations (bag-of-words and term frequencies), and basic analysis like most frequent words or n-grams, or topic models. We will also discuss an example of text analysis in social science (e.g., analyzing political speeches / social media posts). 

**Readings/Videos:**

* *Reading:* “Processing Raw Text” from *NLTK Book* by *Bird, Klein, Loper* – [Link](http://www.nltk.org/book/ch03.html) – introduces tokenization, stopwords, etc. (Skim sections on Python code examples if needed).  
* *Reading:* “How to Do Text Analysis for Social Science” (by *J. Wilkerson*, *D. Casas*, *S. Zhang*, in *CS\&S*) – [Link](https://journals.sagepub.com/doi/10.1177/0894439315609141) – *Sections 1-2* (conceptual overview).  
* *Video:* “An Introduction to Topic Modeling” [YouTube](https://www.youtube.com/watch?v=IUAHUEy1V0Q&t), Summer Institute in CSS 

**In-Class Activities:**

* **Example Case:** Examine a short text dataset (e.g., a sample of reddit data). Group brainstorm: what social science questions could we ask? What words or patterns might indicate answers?  
* **Live Coding:** Instructor demonstrates cleaning data, tokenizing words, filtering stopwords. Then build a simple frequency distribution of words.  
* **Hands-on Notebook:** Students are given a starter Jupyter notebook. They work through exercises: generate the top 10 most frequent words, bigrams, and plot a word cloud.  
* **Discussion:** Differences between bag-of-words and more advanced approaches. We introduce the concept of word embeddings (word2vec/GloVe) conceptually, and how they capture context and relationships (e.g., “king – man \+ woman ≈ queen” analogy).

**Assignments:**

* **Final Project Team Proposal (5%) Due:** A 1–2 page proposal due mid-semester (Week 9\) outlining your research question, planned methods, and a clear division of responsibilities among team members. Feedback will be provided to guide your project. We will spend a few minutes in class discussing possible project ideas. *By next week, each student/team should have a rough idea of what aspect of the data to explore.* Teams can start forming now.

### Week 9: NLP 2: Word Embeddings

**Topics:** Building on NLP basics, we delve into more advanced text analysis methods and **social language analysis**. Key concepts: word embeddings (e.g., using pre-trained models like GloVe to find similar words or bias in language), topic modeling (brief intro to LDA), and text classification basics. We also address ethical issues in NLP (bias in word embeddings, sensitive text data handling).

**Readings/Videos:**

* *Reading:* “Word Embeddings 101” (TensorFlow or Word2Vec via Google Colab) – [Link](https://developers.google.com/machine-learning/crash-course/embeddings/video-lecture) – introduces the concept and has a short video \+ code.  
* *Reading:* “Word Embeddings Quantify 100 Years of Gender and Ethnic Stereotypes” (by *Caliskan et al.*, *Science* 2017\) – [Link](https://science.sciencemag.org/content/356/6334/183) – read the *intro* and examine one result figure (we will discuss how bias in embeddings can reflect social attitudes).  
* *Video:* “Word Embeddings and Word2Vec, Clearly Explained\!\!\!”, [YouTube](https://www.youtube.com/watch?v=viZrOnJclY0), Statquest

**In-Class Activities:**

* **Warm-up:** What is a corpus? What’s tokenization? What’s an embedding? Quick write, then share to reinforce last week’s terms.  
* **Live Demo (Notebook):** Load a small pre-trained embedding. Show how to get the vector for a word and compute cosine similarity between words. Find the closest words in vector space – discuss what that means. Demonstrate a bias example.  
* **Small Group Exercise:** Each group takes a dataset. They qualitatively identify themes, then we use Word2Vec / Bertopic. Groups compare: did the topics discovered align with what they expected? What words define each topic?  
* **Case Discussion:** Present a mini-case of NLP in social science – for example, analyzing sentiment of legislators’ speeches over time, or classifying messages in an online community as support vs. harassment. How do these methods help answer social questions? What are the pitfalls (bias, misinterpretation)?

**Assignments:**

* **HW5 Assigned:** *“NLP Analysis on Social Text.”* – Using a provided text dataset (or an approved dataset of your choice), perform a basic NLP analysis: clean the text, produce some summary statistics (common words, TFIDF, word embeddings analysis), and write a short interpretation connecting it to a social question. Push your code and markdown to Github Classroom.  
* **Final Project:** By now, form teams and decide on a project focus. **Project Proposal due in Week X** – start outlining your plan.

### Week 10: NLP 3: Large Language Models

**Topics:** Introduction to Large Language Models (LLMs) and their applications in computational social science. Building on word embeddings, we explore how modern transformer-based models work and how to use them practically. Key concepts: downloading and running pre-trained models from Hugging Face (focusing on smaller models like Gemma 2B), understanding tokenization and probability distributions, text generation with controlled outputs, function calling/tool use, and prompt engineering basics. We also address the social implications of LLMs, including bias amplification, data privacy, and responsible use in research.

**Readings/Videos:**

* *Reading:* Hugging Face Transformers Documentation – "Quick Tour" and "Pipeline Tutorial" – [Link](https://huggingface.co/docs/transformers/quicktour) – practical introduction to using pre-trained models with minimal code.  
* *Reading:* "Language Models are Few-Shot Learners" (Brown et al., 2020\) – [Link](https://arxiv.org/abs/2005.14165) – read sections 1-2 only for conceptual understanding of how LLMs differ from previous NLP approaches.  
* *Reading*: "The Illustrated Transformer" (by Jay Alammar) – [Link](https://jalammar.github.io/illustrated-transformer/) – skim the first half for visual intuition about how transformers work (don't worry about mathematical details).  
* *Video*: "Large Language Models explained briefly" ([YouTube](https://www.youtube.com/watch?v=LPZh9BOjkQs) \- 3Blue1Brown) – conceptual overview of what LLMs are and how they generate text.  
* *Video*: “The Moment we Stopped Understanding AI” ([YouTube](https://www.youtube.com/watch?v=UZDiGooFs54%20) \- Alexnet) – overview of the complexity of neural networks.

**In-Class Activities:**

**Warm-up:** Quick review connecting embeddings to LLMs. If embeddings capture word meaning, what might a language model capture? Students discuss in pairs, then share insights about the progression from static embeddings to contextual understanding.

**Live Demo (Colab Notebook):**

* This week we're switching to Google Colab because we need GPU access to run language models efficiently. This is a common pattern in computational social science \- choosing the right tool for the task.  
* 5-minute Colab orientation \- show how to connect to GPU, install packages  
* Instructor demonstrates downloading Gemma 2B (or similar 2-7B model) from Hugging Face  
* Show basic text generation: give the model a prompt about a social issue and examine multiple generated completions  
* Demonstrate key concepts: tokenization (show how "social science" becomes tokens), probability distributions (show top-k tokens and their probabilities), and temperature effects on generation  
* Brief demo of controlled generation (e.g., restrict next token to be positive/negative for sentiment analysis)  
* Address common issues: GPU memory limitations, model loading errors, rate limiting  
* Discuss practical considerations: when to use local vs. cloud computing, cost considerations, model size trade-offs

**Hands-On Group Exercise:**

* Groups of 3-4 students work with different social science prompts (provided templates like "Analyze this social media post for...", "Summarize this news article focusing on...", "Generate interview questions about...")  
* Each group experiments with the same model but different parameters (temperature, max length, top-k)  
* Groups compare outputs: How does changing parameters affect the social science utility of responses? What biases do they notice?  
* **Stretch goal:** Groups try simple function calling (if time permits) – give the model access to a "search" function that returns fake social science data

**Case Discussion:**

* Present a real example of LLMs being used in social science research (e.g., content analysis of social media, automated coding of qualitative data, or survey response generation)  
* Discuss: What are the advantages over traditional NLP methods? What are the risks? How might this change social science research methods?  
* Address bias concerns: Show examples of LLM outputs that reflect social biases, discuss implications for research validity

**Assignments:**

* **HW5 Due:** Submit short interpretation of chosen dataset connecting it to a social question.  
* **HW6 Assigned:** *LLM-Assisted Social Text Analysis"* (Due Week 12\) – Using the same dataset from HW5 (or an approved alternative), apply a large language model (Gemma 2B or similar) to perform text analysis tasks such as sentiment analysis, topic classification, or content summarization. Compare the LLM results with your HW5 traditional NLP methods on a subset of your data. Write a short reflection (1-2 pages) discussing the differences between the two approaches and their implications for social science research. Include your Colab notebook with documented prompts and example outputs.  
* **Final Project Integration:** Consider how LLMs might enhance your final project analysis. This assignment serves as practice for potentially incorporating LLMs into your capstone work.

### Week 11: Working in the Cloud

**Topics:** **Remote Computing Environments** – introduction to cloud computing for data-intensive tasks. We focus on Google Cloud as a representative platform: discuss cloud concepts (servers vs. serverless, IaaS/PaaS). We demonstrate launching an instance (virtual machine) with a LLM, access through SSH commands, and running a simple Python job. Cost management and ethics of cloud (e.g., environmental impact) will be touched on.

**Readings/Videos:**

* *Reading:* Geeks for Geeks, “Introduction to Cloud Computing” – [Link](https://www.geeksforgeeks.org/cloud-computing/cloud-computing/) – brief overview of cloud computing platforms and usage.  
* *Reading:* Geeks for Geeks, “What is Google Cloud Platform (GCP)?” – [Link](https://www.geeksforgeeks.org/devops/google-cloud-platform-gcp/) – overview of Google Cloud Platform (GCP) 

**In-Class Activities:**

* **Live Demo:** Instructor walks through Google Cloud setup, configuring key pair for SSH. Once launched, demonstrate SSH into it from the terminal. Run a few basic shell commands to show it’s like a remote computer. Possibly run a simple Python script on EC2 employing a language model  
* **Student Try-out:** students follow along on their laptops (we’ll have step-by-step on slides). If not all can do it, at least a few volunteers try and share experience. (Those without accounts can pair up or just watch due to time.)  
* **Group Discussion:** Brainstorm scenarios in research where cloud is useful (e.g., too much data for a personal laptop, collaboration, needing GPUs for NLP models, etc.). Also discuss pitfalls: forgetting to shut down (cost), data security considerations, learning curve.  
* **Quick Mention:** Other cloud tools – e.g., AWS, institutional clusters. Emphasize that cloud is powerful but not always necessary; choose based on problem size.

**Assignments:**

* **Individual Progress Memo Due (5%):** A short personal reflection submitted during Week 12 detailing your individual contributions so far, any challenges encountered, and your plans for the remainder of the project.

### Week 12: Containerization with Docker

**Topics:** **Docker** – creating and using containers to ensure reproducible environments. We explain what containers are and how they differ from virtual machines. Students learn how to write a simple Dockerfile for a Python application (including choosing a base image, adding requirements, and running a script). We also show how to run a container locally and verify it works the same as the host environment. If time, mention Docker Hub and image repositories.

**Readings/Videos:**

* *Reading:* Docker Official Get Started Guide – [Link](https://docs.docker.com/get-started/) – Read Part 1: Orientation and Part 2: Containers. This gives a high-level picture and a simple example.  
* *Reading:* Dockerfile best practices (Docker Docs) – [Link](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) – skim for understanding, not memorize.  
* *Video:* “[What is Docker in 5 Minutes](https://www.youtube.com/watch?v=_dfLOzuIg2o)” (YouTube, TechSquidTV) – a conceptual crash course

**In-Class Activities:**

* **Whiteboard Analogy:** Explain containers using an analogy (e.g., shipping containers: standardized packages you can send anywhere). Illustrate how “it works on my machine” problems are solved by containerizing the exact environment.  
* **Live Build:** Instructor shows a simple Python script (e.g., hello.py that prints a message or reads a file and prints summary). Write a Dockerfile step-by-step: choose base image (perhaps python:3.10-slim), copy the script, run pip install for any dependencies. Then build the image (docker build \-t hello-app .) and run it (docker run hello-app). Project this so students see the process and output.  
* **Hands-On:** Students modify the Dockerfile to do something slightly different – for example, update the Python script to require an additional package (like numpy), then rebuild and run. This practices editing and rebuilding an image. (Those without Docker installed can pair up or just follow due to admin rights issues in labs; DataHub may also support Docker in a terminal if needed.)  
* **Discussion:** Challenges with Docker (image sizes, learning curve). Also mention container orchestration (Kubernetes) just for context but not in scope. Reiterate that for the final project, using Docker is optional but encouraged for bonus points or learning.

**Assignments:**

* **HW6 Due:** Submit short reflection (1-2 pages) discussing the differences between the two approaches and their implications for social science research. Include your Colab notebook with documented prompts and example outputs.  
* ***Individual Progress Memo Due (5%):*** A short personal reflection submitted during Week 12 detailing your individual contributions so far, any challenges encountered, and your plans for the remainder of the project.  
* **HW7 Assigned:** *“Docker & Cloud Workflow.”* (Due Week 13\) – In this final assignment you will containerize one of your previous scripts (scraper or analysis) using Docker, test it locally, and optionally deploy it on a cloud service. You will also write a short reflection on the experience – what was easier/harder in cloud vs local? Instructions will be provided, including a base Dockerfile example.

### Week 13: Final Project Presentations & Course Wrap-Up

**Topics:** **Final Project Presentations.** This week is dedicated to students showcasing their projects. Depending on class size, presentations may be spread over two sessions (Week 14 class meeting(s) or an extra session during finals period if needed). We will celebrate the work done and reflect on key takeaways from each project and the course as a whole.

**In-Class Activities:**

* **Presentations:** Each team/individual will have \~10 minutes to present, followed by \~3-5 minutes Q\&A. The audience (your peers plus any invited guests, e.g., other faculty or D-Lab staff) will ask questions and give positive feedback. Presentations should cover: the social science question, data and methods (briefly), key findings (with visuals), and conclusions/implications. Live demos are optional if appropriate (and if so, ensure offline capability in case of technical issues\!).  
* **Discussion:** After all presentations, we’ll discuss common themes and surprises. What did we learn about using computational methods in social science? How did different projects perhaps complement each other (one might focus on network structure in Enron, another on linguistic analysis; together they paint a richer picture).  
* **Course Reflection:** Instructor leads a short reflection. Students are invited to share: *What was the most valuable skill or concept you learned?* *How do you envision using these skills in your research or career?* Also, acknowledge how rapidly the field is evolving (e.g., new AI tools) and encourage continuous learning (like advanced cloud tools or deeper machine learning, which could be in Advanced Computing II).  
* **Feedback Collection:** We may do a quick anonymous poll or feedback form about the course content and structure for future improvements.  
* **Wrap-Up:** Provide information on next semester and resources for continuing to build skills (D-Lab workshops).

**Assignments:**

* **Final Project Peer Evaluation (if team):** Due by end of week – each team member submits a short form reflecting on contributions (to ensure accountability in team projects).  
* **Final Report & Code Due** (end of Week 13 or beginning of Week 14): Submit your written report and code repository. This deadline is set a few days before presentations so that the instructor can review content and you incorporate any final feedback. (Exact due date/time TBD, likely over the weekend).  
* **Prepare Presentation:** Polish your slides and narrative for next week’s presentations. Time yourselves to fit in 10 minutes. Remember to also prepare to answer questions from the audience.

## Course Policies

### Policy on Use of Generative AI Tools (e.g., ChatGPT, Claude, Gemini)

This course treats LLMs as a tool in your computational toolkit. But like any tool, it can cause harm if misused – by generating inaccurate results, obscuring your own understanding, or reinforcing bias. Your responsibility is not just to use these tools, but to interrogate them, document them, and stay accountable to your peers and the standards of computational research.

You are permitted to use generative AI tools such as ChatGPT or Claude to assist with coursework, including assignments and exams, as long as you do so transparently and ethically. You are responsible for verifying the accuracy, relevance, and originality of AI-generated content. These tools can produce incorrect or biased responses and may not cite reliable sources.

You **may**:

* use LLMs for brainstorming, outlining, summarizing, editing, or coding help.

You may **not**:

* submit unedited or unexamined AI output as your own work,  
* use LLMs to complete assignments without understanding the logic,  
* use AI to fabricate or misrepresent analysis results or data interpretation.

Violations of these guidelines will be treated as academic misconduct.

#### ***Documentation Requirements***

All uses of LLMs must be disclosed. This includes:

* a brief note in your code or report (e.g., in a comment or footnote),  
* a short explanation of how the tool was used (e.g., “Used Claude 3 to draft a regex expression, then manually debugged the output”),  
* a shared link or transcript of your LLM interaction, if available.

#### ***Assignment-Specific Rules***

* **Homework assignments**: You must disclose and explain all LLM use in a clearly labeled section at the end of your notebook or report.  
* **Final project**: Include a dedicated section in your appendix titled “LLM Usage Log” that:  
  * Describes each use case (e.g., generating code, summarizing data),  
  * Links to shared conversations or summarizes them,  
  * Discusses any problems you identified and corrected.

#### ***Reflection and Accountability***

* Some assignments will specifically ask you to compare traditional methods with LLM-assisted ones. In those, your grade will depend on your ability to evaluate, not just apply LLMs. We want you to understand what the model gets wrong, not just what it gets right.  
* You’re expected to question the model, verify its results, and reflect on its limitations. Think of LLMs as collaborators, not authorities.

***Academic Integrity Reminder***

* Misrepresenting AI-generated work as your own violates academic honesty policies.  
* Using AI tools without disclosure is considered unauthorized aid and may be treated as a form of plagiarism or cheating.  
* When in doubt about what constitutes appropriate use, consult the instructor before submitting your work.

### Attendance and Participation

Regular attendance is expected since this is a hands-on course. Missing more than 2 classes without a valid excuse may impact your participation grade. If you must miss a class due to illness, emergency, or religious observance, please inform the instructor in advance (if possible) or as soon as you can. We will work with you to keep up, and you may be asked to complete make-up exercises. In-class activities cannot be fully replicated outside class, so your proactive communication is key. Consistent tardiness or leaving early without notice will also count against participation. That said, if you are feeling unwell (fever, cough, etc.), do not attend in person – email the instructor and we will accommodate you. We follow Berkeley’s community guidelines: be respectful, engaged, and help foster an inclusive learning environment.

### Late Submission Policy

All assignments are due at the specified time (usually before class on the due date). We understand life can get complicated, so each student has a total of 4 “late days” to use throughout the semester with no penalty (no questions asked). For example, you could hand in one homework 2 days late and another 2 days late, or one homework 4 days late, without penalty. Once late days are exhausted, late work will be penalized 20% of the assignment grade per day late. Assignments more than 5 days late (or after solutions are discussed, whichever comes first) may receive a zero. ***Late days cannot be used for the final project deliverables or presentation***, due to end-of-term grading deadlines – those must be on time unless you have an extraordinary circumstance and have arranged an extension *before* the deadline. If you foresee difficulty in meeting a deadline, talk to the instructor as early as possible; we are willing to accommodate legitimate conflicts when communicated timely (e.g., conference travel, serious personal matters).

### Group vs. Individual Work 

We encourage collaboration and peer learning, but we also need to ensure individual accountability and learning. By default, homework assignments are to be done individually. You may discuss general approaches with classmates, but you must write your own code and responses. Never share your written solutions or code directly with others for individual assignments. For the final project, team collaboration is encouraged. Teams of up to 3 can work together and submit one project. All team members will typically receive the same project grade, so ensure everyone contributes significantly. In your project proposal and final report, clearly state who is on your team and who was responsible for which parts of the work (analysis, coding, writing, etc.). Each member should be able to explain the project in entirety, as we may ask questions individually during Q\&A. If there are issues with team dynamics or unequal contribution, bring it to the instructor’s attention early – do not wait until the end. A brief peer evaluation will be conducted after the project to help assign fair grades if discrepancies in contribution are reported.

### Academic Honesty (UCB Code of Conduct)

You are bound by the UC Berkeley Code of Student Conduct and the Honor Code. Plagiarism or cheating of any kind will not be tolerated. This includes: copying someone else’s code or answers (from a classmate or from the web) and presenting it as your own, using AI-generated content without attribution or instructor permission, or any other form of misrepresentation. *“Any work submitted should be your own individual thoughts… All assignments must use proper attribution… Do not collaborate or share answers unless explicitly allowed.”* . We will use automated tools and manual inspection to check for originality of code and written answers. If you use external resources or libraries not provided in the assignment, cite them (e.g., as comments or in a report). If you *do* use an AI assistant or find a solution snippet online, you must explicitly cite it and still explain it in your own words – failure to disclose use of AI is considered dishonest. Suspected violations will be reported to the Center for Student Conduct. Consequences can range from failing the assignment to failing the course, and further disciplinary action. It’s simply not worth it – when in doubt, ask for help instead of copying.

### Accommodations

***Accommodation for Disabilities (DSP)**:* We are committed to ensuring all students can fully participate in this course. If you have a documented disability or believe you have a disability that might impact your work, please contact the Disabled Students’ Program (DSP) as soon as possible to get official documentation. DSP staff will work with you and the instructor to determine appropriate accommodations. If you are authorized for accommodations, such as extra time on assignments or a note-taker, please provide your Letter of Accommodation to the instructor privately (via email or office hours) ideally in the first two weeks of class, or as soon as you receive it. We will maintain confidentiality and make all reasonable efforts to support your needs. We will collaborate with you and DSP to ensure effective implementation of accommodations. Remember, accommodations are your right – our syllabus’s late or exam policies will be adjusted in your case as required (for instance, “no late homework” rules are modified to allow for extensions granted by DSP).

***Accommodations for Illness or Religious Observance:*** If you have a religious holiday that conflicts with class or assignment due dates, let the instructor know during the first two weeks of class (or at least two weeks in advance of the date) and we will arrange an excused absence or alternative due date, in line with UC Berkeley policy. If you fall ill or have a family emergency that affects your coursework, notify us as soon as possible. We may request verification (like a note from student services or medical provider) for long or repeated absences. Extensions or make-ups for serious medical or personal issues will be granted on a case-by-case basis. Our goal is to support you in these situations – communication is key.

### Diversity and Inclusion

Our classroom is a space where everyone should feel respected and valued. We come from diverse backgrounds and technical experiences; let’s leverage that by helping each other and listening actively. Harassment or discrimination of any form is unacceptable. If you have any concerns about classroom dynamics or experience discomfort due to something in class, please reach out to the instructor or GSI. We will work to address it promptly. For issues you’d prefer not to discuss with course staff, the department and university have resources (e.g., Ombudsperson, Title IX office for relevant cases).

### UCB’s Code of Conduct and Honor Code

We expect all students to uphold Berkeley’s Honor Code: *“As a member of the UC Berkeley community, I act with honesty, integrity, and respect for others.”* This extends to how you behave in class (no trolling or heckling, treat others’ questions and viewpoints with respect) and how you carry out academic work (honesty and integrity as described above). The Code of Student Conduct outlines the university’s expectations and processes; you can find it on the Center for Student Conduct website . We will enforce these standards.

By staying enrolled in this course, you indicate that you have read and understood this syllabus and agree to abide by all policies herein. Let’s have a productive, creative, and enjoyable semester learning advanced computing skills and applying them to understand social data\!