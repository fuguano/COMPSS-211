# Cloud Computing for Computational Social Science

📝 **Poll**: Have you ever used cloud computing services? If yes, which ones (AWS, Google Cloud, Azure, etc.)? What did you use them for?

---
**_Learning Objectives_:**  
1. Understand cloud computing concepts (IaaS, PaaS, SaaS, serverless)
2. Launch and manage virtual machines on Google Cloud Platform
3. Connect to remote instances via SSH
4. Run language models and Python jobs in the cloud
5. Manage costs and understand environmental implications
6. Apply cloud computing to computational social science workflows
---

## 1. Introduction to Cloud Computing

### What is Cloud Computing?

**Cloud computing** is the delivery of computing services—including servers, storage, databases, networking, software, and analytics—over the Internet ("the cloud"). Instead of buying and maintaining physical servers, you can access these resources on-demand from cloud providers.

Think of it like this:
- **Traditional Computing**: Buying and maintaining your own car
- **Cloud Computing**: Using Uber/Lyft when you need transportation

### Why Cloud Computing for Social Science?

🔔 **Question:** What computational challenges have you faced that your laptop couldn't handle?

Cloud computing becomes essential when:
- **Data is too large** for local storage (terabytes of social media data)
- **Processing is too intensive** (training large NLP models)
- **Collaboration is needed** (shared datasets and environments)
- **Reproducibility matters** (consistent environments across researchers)
- **Resources are temporary** (need GPUs for a week, not forever)

🎬 **Demo:** Let me show you a real example of when cloud beats local computing.

---

## 2. Cloud Computing Concepts

### Service Models

Cloud services come in different layers of abstraction:

#### Infrastructure as a Service (IaaS)
- **What you get**: Virtual machines, storage, networks
- **What you manage**: Operating system, applications, data
- **Example**: Google Compute Engine, AWS EC2
- **Like**: Renting an empty apartment - you furnish everything

#### Platform as a Service (PaaS)
- **What you get**: Development platforms, databases, tools
- **What you manage**: Your application and data
- **Example**: Google App Engine, Heroku
- **Like**: Renting a furnished apartment - just bring your belongings

#### Software as a Service (SaaS)
- **What you get**: Complete applications
- **What you manage**: Your data and settings
- **Example**: Google Docs, Dropbox, GitHub
- **Like**: Staying in a hotel - everything is provided

### Servers vs. Serverless

#### Traditional Servers (Virtual Machines)
```
You: "I need a computer with 8GB RAM and 2 CPUs"
Cloud: "Here's your VM. It costs $0.05/hour whether you use it or not"
```

#### Serverless Computing
```
You: "Run this function when someone uploads a file"
Cloud: "Done. You only pay for the milliseconds it runs"
```

**When to use each:**
- **VMs**: Long-running processes, full control needed, consistent workloads
- **Serverless**: Event-driven tasks, irregular workloads, auto-scaling needed

💡 **Tip**: For research, VMs are usually more straightforward. Serverless is great for production systems.

---

## 3. Google Cloud Platform Overview

### Why Google Cloud?

We're using Google Cloud Platform (GCP) because:
- **Free tier**: $300 credit for new users 
- **Academic friendly**: Good documentation and educational resources
- **Integration**: Works well with Colab and other Google services
- **Global infrastructure**: Data centers worldwide

### Core GCP Services We'll Use

1. **Compute Engine**: Virtual machines (our focus today)
2. **Cloud Storage**: Store large datasets
3. **Cloud Shell**: Browser-based terminal
4. **Cloud SDK**: Command-line tools

Visit [console.cloud.google.com](https://console.cloud.google.com) and explore the interface. What services do you see in the menu?

---

## 4. Setting Up Your Cloud Environment

### Creating a GCP Account

1. **Visit** [cloud.google.com](https://cloud.google.com)
2. **Click** "Get started for free"
3. **Sign in** with your Google account
4. **Provide** billing information (won't be charged during free trial)
5. **Activate** your $300 free credit

⚠️ **Important**: Set up billing alerts immediately to avoid surprises!

### Creating Your First Project

```bash
# In Cloud Console:
1. Click "Select a project" → "New Project"
2. Name it: "compss211-yourname"
3. Note your Project ID (you'll need this)
```

---

## 5. Launching Your First Virtual Machine

### Understanding VM Options

Before creating a VM, understand the choices:

```python
# VM Configuration Options
{
    "machine_type": {
        "e2-micro": "0.25-2 vCPUs, 1GB RAM, $0.006/hour",
        "e2-medium": "1-2 vCPUs, 4GB RAM, $0.03/hour", 
        "n2-standard-4": "4 vCPUs, 16GB RAM, $0.19/hour",
        "a2-highgpu-1g": "12 vCPUs, 85GB RAM, 1 A100 GPU, $2.95/hour"
    },
    "boot_disk": {
        "ubuntu-2204": "Ubuntu 22.04 LTS",
        "debian-11": "Debian 11",
        "deep-learning-vm": "Pre-configured for ML"
    },
    "region": {
        "us-central1": "Iowa (cheap)",
        "us-west1": "Oregon",
        "europe-west4": "Netherlands"
    }
}
```

### Creating a VM via Console

🎬 **Live Demo:** Creating a VM step-by-step

1. **Navigate** to Compute Engine → VM instances
2. **Click** "Create Instance"
3. **Configure**:
   - Name: `llm-instance`
   - Region: `us-central1` (cheapest)
   - Machine type: `e2-medium` (good for experiments)
   - Boot disk: Ubuntu 22.04 LTS, 30GB
   - Firewall: Allow HTTP/HTTPS
4. **Click** "Create"

### Creating a VM via Command Line

```bash
# Using Cloud Shell or local gcloud CLI
gcloud compute instances create llm-instance \
    --zone=us-central1-a \
    --machine-type=e2-medium \
    --image-family=ubuntu-2204-lts \
    --image-project=ubuntu-os-cloud \
    --boot-disk-size=30GB \
    --boot-disk-type=pd-standard
```

Create an `e2-micro` instance (free tier eligible) in your nearest region.

---

## 6. Connecting via SSH

### SSH Basics

SSH (Secure Shell) allows you to connect to remote computers securely:

```bash
# Basic SSH syntax
ssh username@ip-address

# Example
ssh jane@34.123.45.67
```

### Three Ways to Connect to Your VM

#### Method 1: Browser-based SSH (Easiest)
1. Go to VM instances page
2. Click "SSH" button next to your instance
3. Terminal opens in browser

#### Method 2: Cloud Shell
```bash
# In Cloud Shell
gcloud compute ssh llm-instance --zone=us-central1-a
```

#### Method 3: Local Terminal (Most Professional)
```bash
# First, add your SSH key to the project
gcloud compute project-info add-metadata \
    --metadata-from-file ssh-keys=~/.ssh/id_rsa.pub

# Then connect
ssh -i ~/.ssh/id_rsa username@external-ip
```

### Your First Remote Commands

Once connected, try these:

```bash
# Check system info
whoami                  # Your username
hostname                # VM name
pwd                     # Current directory
df -h                   # Disk usage
free -h                 # Memory usage
htop                    # CPU and memory monitor (install: sudo apt install htop)

# Check Python
python3 --version       # Python version
pip3 --version         # pip version
```

SSH into your VM and check how much RAM and disk space you have.

---

## 7. Running Python Jobs in the Cloud

### Setting Up Python Environment

```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3-pip python3-venv -y

# Create virtual environment
python3 -m venv ~/env
source ~/env/bin/activate

# Install essential packages
pip install numpy pandas matplotlib jupyter transformers torch
```

### Transferring Files to Your VM

#### Method 1: Using SCP (Secure Copy)
```bash
# From your local machine
scp local_file.py username@vm-ip:~/
scp -r local_folder/ username@vm-ip:~/

# From VM to local
scp username@vm-ip:~/results.csv ./
```

#### Method 2: Using Git
```bash
# On your VM
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

#### Method 3: Using Cloud Storage
```bash
# Upload to Cloud Storage (from local)
gsutil cp data.csv gs://your-bucket/

# Download on VM
gsutil cp gs://your-bucket/data.csv ./
```

### Running a Simple Python Script

Create and run a test script:

```bash
# Create a script
cat > test_cloud.py << EOF
import platform
import psutil
import datetime

print(f"Running on: {platform.node()}")
print(f"Python: {platform.python_version()}")
print(f"System: {platform.system()} {platform.release()}")
print(f"CPU cores: {psutil.cpu_count()}")
print(f"RAM: {psutil.virtual_memory().total / (1024**3):.1f} GB")
print(f"Time: {datetime.datetime.now()}")
EOF

# Run it
python3 test_cloud.py
```

Create and run a Python script that counts from 1 to 1 million and times how long it takes.

---

## 8. Running Language Models in the Cloud

### Why Run LLMs in the Cloud?

- **Memory**: LLMs need lots of RAM (8-80GB+)
- **Speed**: Cloud GPUs are much faster
- **Cost**: Pay only for what you use
- **Access**: Run models your laptop can't handle

### Setting Up for LLMs

```bash
# Install PyTorch and Transformers
pip install torch transformers accelerate

# For GPU support (if using GPU instance)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Running a Small Model (CPU)

```python
# save as run_llm.py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import time

print("Loading model...")
model_name = "microsoft/phi-2"  # 2.7B parameter model

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    torch_dtype=torch.float32,
    trust_remote_code=True
)

# Test generation
prompt = "The future of social media is"
print(f"\nPrompt: {prompt}")

inputs = tokenizer(prompt, return_tensors="pt")
start = time.time()

with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=50, temperature=0.7)

result = tokenizer.decode(outputs[0], skip_special_tokens=True)
elapsed = time.time() - start

print(f"Response: {result}")
print(f"Time: {elapsed:.2f} seconds")
```

### Running Larger Models (Llama 3)

For Llama 3.2 (3B parameters):

```python
# save as run_llama.py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# This requires ~6GB RAM
model_name = "meta-llama/Llama-3.2-3B-Instruct"

# Check if you have access (need to accept license on HuggingFace)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,  # Use half precision to save memory
    device_map="auto"
)

# Use the model
messages = [
    {"role": "user", "content": "Explain cloud computing in one sentence."}
]

input_text = tokenizer.apply_chat_template(messages, tokenize=False)
inputs = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### Using Screen for Long-Running Jobs

```bash
# Install screen
sudo apt install screen -y

# Start a new screen session
screen -S llm_training

# Run your Python script
python3 run_llama.py

# Detach from screen (Ctrl+A, then D)
# You can now disconnect from SSH

# Reattach later
screen -r llm_training

# List all screens
screen -ls
```

Run a small language model and generate text about "computational social science".

---

## 9. Cost Management

### Understanding Cloud Costs

Cloud costs can add up quickly! Here's what you pay for:

| Resource | Cost Factor | Typical Price |
|----------|------------|---------------|
| **Compute** | vCPU-hours | $0.006-0.50/hour |
| **Memory** | GB-hours | $0.001-0.05/GB/hour |
| **Storage** | GB-month | $0.02-0.10/GB/month |
| **Network** | GB transferred | $0.01-0.12/GB |
| **GPU** | GPU-hours | $0.50-8.00/hour |

### Cost Optimization Strategies

#### 1. Use Preemptible/Spot Instances
```bash
# 60-80% cheaper but can be terminated
gcloud compute instances create cheap-instance \
    --preemptible \
    --machine-type=e2-medium
```

#### 2. Stop (Don't Delete) When Not Using
```bash
# Stop instance (no compute charges, still pay for disk)
gcloud compute instances stop llm-instance

# Start when needed
gcloud compute instances start llm-instance

# Delete when completely done
gcloud compute instances delete llm-instance
```

#### 3. Use Appropriate Instance Sizes
```python
# Don't use this for simple tasks:
"n2-standard-32": "32 vCPUs, 128GB RAM, $1.50/hour"  # ❌ Overkill

# Use this instead:
"e2-micro": "0.25 vCPUs, 1GB RAM, $0.006/hour"  # ✅ Right-sized
```

#### 4. Set Up Auto-Shutdown
```bash
# Auto-shutdown after 30 minutes of inactivity
echo '*/10 * * * * /usr/bin/test $(who | wc -l) -eq 0 && /usr/bin/test $(( $(date +%s) - $(stat -c %Y /var/log/lastlog) )) -gt 1800 && sudo shutdown -h now' | crontab -
```

### Monitoring Costs

```bash
# Check current billing
gcloud billing accounts list
gcloud billing projects describe $(gcloud config get-value project)

# Set up billing export to BigQuery for analysis
# (Do this in Console: Billing → Billing export)
```

Tip: Use the [GCP Pricing Calculator](https://cloud.google.com/products/calculator).

---

## 10. Environmental and Ethical Considerations

### The Carbon Footprint of Cloud Computing

🔔 **Question:** How much energy do you think a single Google search uses?

Cloud computing has significant environmental impacts:

```python
# Rough estimates of CO2 emissions
emissions = {
    "training_gpt3": "552 tonnes CO2",  # Like 120 cars for a year
    "single_query": "0.2g CO2",         # One Google search
    "vm_per_hour": "10-50g CO2",        # Depending on region
    "gpu_training": "100-500g CO2/hour" # Intensive computing
}
```

### Regional Differences

Different data center locations have different carbon intensities:

```python
# Carbon intensity by region (gCO2/kWh)
carbon_intensity = {
    "us-central1 (Iowa)": 479,        # High (coal-heavy)
    "europe-north1 (Finland)": 181,   # Low (renewable)
    "europe-west4 (Netherlands)": 474, # High
    "us-west1 (Oregon)": 117          # Low (hydro)
}
```

💡 **Tip**: Choose low-carbon regions when possible!

### Ethical Best Practices

#### 1. Efficiency First
```python
# Bad: Wasteful approach
for i in range(1000):
    model = load_huge_model()  # Loading model 1000 times!
    result = model.predict(data[i])

# Good: Efficient approach  
model = load_huge_model()  # Load once
for i in range(1000):
    result = model.predict(data[i])
```

#### 2. Right-Size Resources
- Don't use GPUs for simple tasks
- Don't keep instances running when idle
- Use batch processing when possible

#### 3. Consider Alternatives
- Can you use a smaller model?
- Can you run locally?
- Can you use cached/pre-computed results?

#### 4. Carbon Offsetting
Some researchers purchase carbon offsets for their computational work:
- Calculate emissions using tools like [ML CO2 Impact](https://mlco2.github.io/impact/)
- Purchase verified offsets
- Document in papers

### Discussion: Sustainability in Research

🔔 **Group Discussion:** 
1. Should computational cost be a factor in research design?
2. How do we balance innovation with environmental responsibility?
3. What role should universities play in sustainable computing?

---

## 11. Practical Exercises

### Exercise 1: Cloud vs Local Comparison

Run the same task locally and in the cloud:

```python
# benchmark.py
import time
import numpy as np

def matrix_multiply(size=1000):
    """Multiply two random matrices"""
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    
    start = time.time()
    C = np.dot(A, B)
    elapsed = time.time() - start
    
    return elapsed

# Run benchmarks
sizes = [100, 500, 1000, 2000]
for size in sizes:
    time_taken = matrix_multiply(size)
    print(f"Size {size}x{size}: {time_taken:.2f} seconds")
```

Run this benchmark locally and on your cloud VM. Compare the results.

---

## 13. Summary and Best Practices

### Key Takeaways

**Cloud Computing Essentials**
- Understand IaaS vs PaaS vs SaaS
- Know when cloud beats local computing
- Master basic VM management

**Practical Skills**
- Launch and connect to VMs
- Transfer files and run jobs
- Monitor and control costs

**Professional Practices**
- Always set billing alerts
- Stop instances when not using
- Choose appropriate instance sizes
- Consider environmental impact

---

## Additional Resources

### Documentation
- [Google Cloud Documentation](https://cloud.google.com/docs)
- [GCP Free Tier](https://cloud.google.com/free)
- [SSH Tutorial](https://www.ssh.com/academy/ssh/tutorial)

### Tutorials
- [GCP Quickstart](https://cloud.google.com/compute/docs/quickstart)
- [Running Jupyter on GCP](https://cloud.google.com/ai-platform/notebooks)
- [Cloud Cost Optimization](https://cloud.google.com/architecture/cost-optimization)

### Tools
- [GCP Pricing Calculator](https://cloud.google.com/products/calculator)
- [Cloud Carbon Footprint](https://www.cloudcarbonfootprint.org/)
- [ML CO2 Calculator](https://mlco2.github.io/impact/)

### Academic Resources
- [Berkeley Research Computing](https://research-it.berkeley.edu/services/high-performance-computing)
- [Google Cloud Research Credits](https://edu.google.com/programs/credits/research/)
