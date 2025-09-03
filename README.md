🚀 Automating EC2 Start/Stop with AWS Lambda  

** 📌 Project Overview  
This project demonstrates how to **automatically start and stop Amazon EC2 instances** using **AWS Lambda, CloudWatch Events, IAM, and SNS**.  

- ⏰ **Start EC2 at 10:00 AM IST**  
- ⏰ **Stop EC2 at 7:00 PM IST**  
- 📩 **Email notifications** sent via **SNS** whenever an instance starts or stops  

This automation helps reduce AWS costs and ensures instances run only during business hours.  

---

## 🏗️ Architecture  
<img width="1024" height="1024" alt="architecture" src="https://github.com/user-attachments/assets/f1e5cdff-91c5-4e98-a0a7-e59363cb8344" />

  

**Flow:**  
1. CloudWatch Event triggers Lambda based on cron schedule.  
2. Lambda checks for EC2 instances with a specific **tag** (e.g., `AutoStartStop=true`).  
3. Lambda starts/stops the EC2 instance accordingly.  
4. SNS sends an email notification.  

---

## ⚙️ Step-by-Step Implementation  

### **1. Create IAM Role & Policy**  
- Go to **IAM → Roles → Create Role**.  
- Attach this custom policy:  

```json
{
  "Effect": "Allow",
  "Action": [
    "ec2:StartInstances",
    "ec2:StopInstances",
    "ec2:DescribeInstances",
    "sns:Publish"
  ],
  "Resource": "*"
}
````

* Attach the role to Lambda functions.

---

### **2. Create Lambda Functions**

📂 Files in repo:

* `lambda_start.py` → Starts EC2 instances.
* `lambda_stop.py` → Stops EC2 instances.

Each function:

* Uses `boto3` to interact with EC2.
* Filters instances by tag (`AutoStartStop=true`).
* Publishes notification to SNS topic.

---

### **3. Configure CloudWatch Rules (Schedules)**

* Create two rules under **CloudWatch → Rules**:

📌 **Start EC2 at 10:00 AM IST (4:30 UTC)**

```
cron(30 4 * * ? *)
```

📌 **Stop EC2 at 7:00 PM IST (13:30 UTC)**

```
cron(30 13 * * ? *)
```

* Target → Lambda function (`lambda_start` or `lambda_stop`).

---

### **4. Create SNS Topic for Notifications**

* Go to **SNS → Topics → Create Topic**.
* Add your email as a **subscription**.
* Confirm subscription from your email inbox.
* Use the Topic ARN in Lambda code.

---

### **5. Add Tag to EC2 Instance**

* Go to **EC2 → Instances → Tags → Add Tag**.
* Key: `AutoStartStop`
* Value: `true`

---

## 📂 Repository Contents

* `lambda_start.py` → Lambda function for start.
* `lambda_stop.py` → Lambda function for stop.
* `iam-policy.json` → IAM permissions policy.
* `cron-expressions.txt` → CloudWatch cron rules.
* `architecture.png` → Architecture diagram.

---

## ⏳ Cron Expressions Used

```
# Start EC2 at 10 AM IST (4:30 UTC)
cron(30 4 * * ? *)

# Stop EC2 at 7 PM IST (13:30 UTC)
cron(30 13 * * ? *)
```

---

## 🔑 AWS Services Used

* **AWS Lambda** → Automation logic
* **Amazon CloudWatch** → Scheduling
* **Amazon SNS** → Notifications
* **Amazon EC2** → Compute instance
* **IAM** → Access control

---

## 🎯 Use Case

* Reduce EC2 running costs.
* Automatically manage EC2 runtime during office hours.
* Great hands-on project for **DevOps / AWS Engineer portfolios**.

---

👉 This project is part of my **AWS DevOps portfolio**, showcasing automation, cost optimization, and event-driven architecture.

```

---

Do you also want me to **add usage instructions** (how someone else can clone and test your repo) at the end of this README?
```

