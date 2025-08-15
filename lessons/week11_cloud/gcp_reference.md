# Google Cloud Platform Quick Reference

## Essential GCP Commands

### Authentication & Setup
```bash
# Install gcloud CLI (Mac)
brew install --cask google-cloud-sdk

# Install gcloud CLI (Linux)
curl https://sdk.cloud.google.com | bash

# Initialize and authenticate
gcloud init
gcloud auth login

# Set default project
gcloud config set project PROJECT_ID

# List current configuration
gcloud config list
```

### Project Management
```bash
# List all projects
gcloud projects list

# Create new project
gcloud projects create PROJECT_ID --name="Project Name"

# Switch projects
gcloud config set project PROJECT_ID

# Get project info
gcloud projects describe PROJECT_ID
```

### Compute Engine (VMs)
```bash
# List all instances
gcloud compute instances list

# Create instance
gcloud compute instances create INSTANCE_NAME \
    --zone=us-central1-a \
    --machine-type=e2-micro \
    --image-family=ubuntu-2204-lts \
    --image-project=ubuntu-os-cloud

# Start instance
gcloud compute instances start INSTANCE_NAME --zone=us-central1-a

# Stop instance
gcloud compute instances stop INSTANCE_NAME --zone=us-central1-a

# Delete instance
gcloud compute instances delete INSTANCE_NAME --zone=us-central1-a

# SSH into instance
gcloud compute ssh INSTANCE_NAME --zone=us-central1-a

# Copy files to instance
gcloud compute scp LOCAL_FILE INSTANCE_NAME:~/REMOTE_PATH --zone=us-central1-a

# Copy files from instance
gcloud compute scp INSTANCE_NAME:~/REMOTE_FILE LOCAL_PATH --zone=us-central1-a
```

### Machine Types Reference
| Type | vCPUs | Memory | Price/hour* |
|------|-------|--------|------------|
| e2-micro | 0.25 | 1GB | $0.006 |
| e2-small | 0.5 | 2GB | $0.012 |
| e2-medium | 1 | 4GB | $0.027 |
| e2-standard-2 | 2 | 8GB | $0.067 |
| e2-standard-4 | 4 | 16GB | $0.134 |
| n2-standard-8 | 8 | 32GB | $0.388 |
| a2-highgpu-1g | 12 | 85GB + A100 GPU | $2.95 |

*Prices for us-central1 region

### Cloud Storage
```bash
# Create bucket
gsutil mb gs://BUCKET_NAME

# List buckets
gsutil ls

# Upload file
gsutil cp LOCAL_FILE gs://BUCKET_NAME/

# Download file
gsutil cp gs://BUCKET_NAME/FILE LOCAL_PATH

# Upload directory
gsutil -m cp -r LOCAL_DIR gs://BUCKET_NAME/

# List bucket contents
gsutil ls gs://BUCKET_NAME/

# Delete file
gsutil rm gs://BUCKET_NAME/FILE

# Delete bucket
gsutil rb gs://BUCKET_NAME
```

### Billing & Cost Management
```bash
# List billing accounts
gcloud billing accounts list

# Get current project billing
gcloud billing projects describe PROJECT_ID

# Set billing account for project
gcloud billing projects link PROJECT_ID --billing-account=ACCOUNT_ID

# Export billing to BigQuery (set up in Console)
```

### Useful Instance Operations
```bash
# Create instance with startup script
gcloud compute instances create INSTANCE_NAME \
    --metadata-from-file startup-script=startup.sh

# Add SSH key to project
gcloud compute project-info add-metadata \
    --metadata-from-file ssh-keys=~/.ssh/id_rsa.pub

# Create instance with specific boot disk size
gcloud compute instances create INSTANCE_NAME \
    --boot-disk-size=50GB \
    --boot-disk-type=pd-standard

# Create preemptible instance (cheaper)
gcloud compute instances create INSTANCE_NAME \
    --preemptible \
    --machine-type=e2-standard-4

# List available machine types
gcloud compute machine-types list --filter="zone:us-central1-a"

# List available images
gcloud compute images list
```

### Firewall Rules
```bash
# List firewall rules
gcloud compute firewall-rules list

# Create rule to allow HTTP
gcloud compute firewall-rules create allow-http \
    --allow tcp:80 \
    --source-ranges 0.0.0.0/0

# Create rule for specific port
gcloud compute firewall-rules create allow-8080 \
    --allow tcp:8080 \
    --source-ranges 0.0.0.0/0

# Delete firewall rule
gcloud compute firewall-rules delete RULE_NAME
```

### Monitoring & Logs
```bash
# View instance serial port output
gcloud compute instances get-serial-port-output INSTANCE_NAME

# Tail logs
gcloud logging tail

# Read specific logs
gcloud logging read "resource.type=gce_instance"

# List metrics
gcloud monitoring metrics-descriptors list
```

### Cost-Saving Commands
```bash
# Schedule instance stop (via Cloud Scheduler - setup in Console)
# Or use cron on the instance itself:
echo "0 18 * * * gcloud compute instances stop INSTANCE_NAME --zone=us-central1-a" | crontab -

# Auto-shutdown script for instance
cat > /usr/local/bin/auto-shutdown.sh << 'EOF'
#!/bin/bash
if [ $(who | wc -l) -eq 0 ]; then
    sudo shutdown -h now
fi
EOF

# Make it run every 30 minutes
echo "*/30 * * * * /usr/local/bin/auto-shutdown.sh" | crontab -
```

## Python Libraries for GCP

### Installation
```bash
pip install google-cloud-storage google-cloud-compute
```

### Storage Example
```python
from google.cloud import storage

# Initialize client
client = storage.Client()

# Create bucket
bucket = client.create_bucket("my-bucket")

# Upload file
bucket = client.bucket("my-bucket")
blob = bucket.blob("data.csv")
blob.upload_from_filename("local_data.csv")

# Download file
blob = bucket.blob("data.csv")
blob.download_to_filename("downloaded_data.csv")
```

### Compute Example
```python
from google.cloud import compute_v1

# Initialize client
instance_client = compute_v1.InstancesClient()

# List instances
project = "your-project-id"
zone = "us-central1-a"
instances = instance_client.list(project=project, zone=zone)

for instance in instances:
    print(f"Instance: {instance.name}")
```

## Common Troubleshooting

### Issue: Permission Denied
```bash
# Check current authenticated user
gcloud auth list

# Re-authenticate
gcloud auth login

# Check project permissions
gcloud projects get-iam-policy PROJECT_ID
```

### Issue: Quota Exceeded
```bash
# Check quotas
gcloud compute project-info describe --project=PROJECT_ID

# Request quota increase (done in Console)
```

### Issue: Instance Won't Start
```bash
# Check instance status
gcloud compute instances describe INSTANCE_NAME --zone=us-central1-a

# Check logs
gcloud logging read "resource.labels.instance_id=INSTANCE_ID" --limit 50
```

### Issue: Can't SSH
```bash
# Add SSH key to metadata
gcloud compute instances add-metadata INSTANCE_NAME \
    --metadata-from-file ssh-keys=~/.ssh/id_rsa.pub

# Use browser-based SSH (in Console)

# Reset instance (last resort)
gcloud compute instances reset INSTANCE_NAME --zone=us-central1-a
```

## Best Practices Checklist

- [ ] Set up billing alerts before creating resources
- [ ] Use appropriate machine types (don't over-provision)
- [ ] Stop instances when not in use
- [ ] Use preemptible instances for batch jobs
- [ ] Delete unused resources promptly
- [ ] Use labels to organize resources
- [ ] Enable auto-shutdown for development instances
- [ ] Use Cloud Storage for large datasets
- [ ] Monitor costs weekly
- [ ] Document your setup for reproducibility

## Quick Cost Estimates

| Usage Pattern | Instance Type | Monthly Cost* |
|--------------|---------------|--------------|
| Development (8hr/day, weekdays) | e2-micro | ~$1 |
| Always-on web server | e2-micro | ~$4 |
| ML training (10hr/week) | n2-standard-8 | ~$15 |
| GPU training (5hr/week) | a2-highgpu-1g | ~$60 |
| Data storage (100GB) | Cloud Storage | ~$2 |

*Approximate costs for us-central1 region

## Useful Links

- [GCP Console](https://console.cloud.google.com)
- [GCP Pricing Calculator](https://cloud.google.com/products/calculator)
- [GCP Free Tier](https://cloud.google.com/free)
- [GCP Documentation](https://cloud.google.com/docs)
- [Cloud SDK Installation](https://cloud.google.com/sdk/docs/install)
- [Qwiklabs (Free Training)](https://www.qwiklabs.com/)