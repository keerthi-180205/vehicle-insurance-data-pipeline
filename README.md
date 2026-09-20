# MLOps Project - Vehicle Insurance Data Pipeline

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#mlops-project---vehicle-insurance-data-pipeline)

Welcome to this MLOps project, designed to demonstrate a robust pipeline for managing vehicle insurance data. This project aims to impress recruiters and visitors by showcasing the various tools, techniques, services, and features that go into building and deploying a machine learning pipeline for real-world data management. Follow along to learn about project setup, data processing, model deployment, and CI/CD automation!

---

## 📁 Project Setup and Structure

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#-project-setup-and-structure)

### Step 1: Project Template

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#step-1-project-template)

- Start by executing the `template.py` file to create the initial project template, which includes the required folder structure and placeholder files.

### Step 2: Package Management

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#step-2-package-management)

- Write the setup for importing local packages in `setup.py` and `pyproject.toml` files.
- **Tip**: Learn more about these files from `crashcourse.txt`.

### Step 3: Virtual Environment and Dependencies

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#step-3-virtual-environment-and-dependencies)

- Create a virtual environment and install required dependencies from `requirements.txt`:
  ```
  conda create -n vehicle python=3.10 -y
  conda activate vehicle
  pip install -r requirements.txt
  ```
  **svg**
- Verify the local packages by running:
  ```
  pip list
  ```
  **svg**

---

## 📊 MongoDB Setup and Data Management

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#-mongodb-setup-and-data-management)

### Step 4: MongoDB Atlas Configuration

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#step-4-mongodb-atlas-configuration)

1. Sign up for [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) and create a new project.
2. Set up a free M0 cluster, configure the username and password, and allow access from any IP address (`0.0.0.0/0`).
3. Retrieve the MongoDB connection string for Python and save it (replace `<password>` with your password).

### Step 5: Pushing Data to MongoDB

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#step-5-pushing-data-to-mongodb)

1. Create a folder named `notebook`, add the dataset, and create a notebook file `mongoDB_demo.ipynb`.
2. Use the notebook to push data to the MongoDB database.
3. Verify the data in MongoDB Atlas under Database > Browse Collections.

---

## 📝 Logging, Exception Handling, and EDA

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#-logging-exception-handling-and-eda)

### Step 6: Set Up Logging and Exception Handling

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#step-6-set-up-logging-and-exception-handling)

- Create logging and exception handling modules. Test them on a demo file `demo.py`.

### Step 7: Exploratory Data Analysis (EDA) and Feature Engineering

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#step-7-exploratory-data-analysis-eda-and-feature-engineering)

- Analyze and engineer features in the `EDA` and `Feature Engg` notebook for further processing in the pipeline.

---

## 📥 Data Ingestion

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#-data-ingestion)

### Step 8: Data Ingestion Pipeline

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#step-8-data-ingestion-pipeline)

- Define MongoDB connection functions in `configuration.mongo_db_connections.py`.
- Develop data ingestion components in the `data_access` and `components.data_ingestion.py` files to fetch and transform data.
- Update `entity/config_entity.py` and `entity/artifact_entity.py` with relevant ingestion configurations.
- Run `demo.py` after setting up MongoDB connection as an environment variable.

### Setting Environment Variables

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#setting-environment-variables)

- Set MongoDB URL:
  ```
  # For Bash
  export MONGODB_URL="mongodb+srv://<username>:<password>...."
  # For Powershell
  $env:MONGODB_URL = "mongodb+srv://<username>:<password>...."
  ```
  **svg**
- **Note**: On Windows, you can also set environment variables through the system settings.

---

## 🔍 Data Validation, Transformation & Model Training

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#-data-validation-transformation--model-training)

### Step 9: Data Validation

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#step-9-data-validation)

- Define schema in `config.schema.yaml` and implement data validation functions in `utils.main_utils.py`.

### Step 10: Data Transformation

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#step-10-data-transformation)

- Implement data transformation logic in `components.data_transformation.py` and create `estimator.py` in the `entity` folder.

### Step 11: Model Training

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#step-11-model-training)

- Define and implement model training steps in `components.model_trainer.py` using code from `estimator.py`.

---

## 🌐 AWS Setup for Model Evaluation & Deployment

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#-aws-setup-for-model-evaluation--deployment)

### Step 12: AWS Setup

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#step-12-aws-setup)

1. Log in to the AWS console, create an IAM user, and grant `AdministratorAccess`.
2. Set AWS credentials as environment variables.
   ```
   # For Bash
   export AWS_ACCESS_KEY_ID="YOUR_AWS_ACCESS_KEY_ID"
   export AWS_SECRET_ACCESS_KEY="YOUR_AWS_SECRET_ACCESS_KEY"
   ```
   **svg**
3. Configure S3 Bucket and add access keys in `constants.__init__.py`.

### Step 13: Model Evaluation and Pushing to S3

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#step-13-model-evaluation-and-pushing-to-s3)

- Create an S3 bucket named `my-model-mlopsproj` in the `us-east-1` region.
- Develop code to push/pull models to/from the S3 bucket in `src.aws_storage` and `entity/s3_estimator.py`.

---

## 🚀 Model Evaluation, Model Pusher, and Prediction Pipeline

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#-model-evaluation-model-pusher-and-prediction-pipeline)

### Step 14: Model Evaluation & Model Pusher

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#step-14-model-evaluation--model-pusher)

- Implement model evaluation and deployment components.
- Create `Prediction Pipeline` and set up `app.py` for API integration.

### Step 15: Static and Template Directory

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#step-15-static-and-template-directory)

- Add `static` and `template` directories for web UI.

---

## 🔄 CI/CD Setup with Docker, GitHub Actions, and AWS

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#-cicd-setup-with-docker-github-actions-and-aws)

### Step 16: Docker and GitHub Actions

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#step-16-docker-and-github-actions)

1. Create `Dockerfile` and `.dockerignore`.
2. Set up GitHub Actions with AWS authentication by creating secrets in GitHub for:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_DEFAULT_REGION`
   - `ECR_REPO`

### Step 17: AWS EC2 and ECR

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#step-17-aws-ec2-and-ecr)

1. Set up an EC2 instance for deployment.
2. Install Docker on the EC2 machine.
3. Connect EC2 as a self-hosted runner on GitHub.

### Step 18: Final Steps

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#step-18-final-steps)

1. Open the 5080 port on the EC2 instance.
2. Access the deployed app by visiting `http://<public_ip>:5080`.

---

## 🛠️ Additional Resources

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#%EF%B8%8F-additional-resources)

- **Crash Course on setup.py and pyproject.toml**: See `crashcourse.txt` for details.
- **GitHub Secrets**: Manage secrets for secure CI/CD pipelines.

---

## 🎯 Project Workflow Summary

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#-project-workflow-summary)

1. **Data Ingestion** ➔ **Data Validation** ➔ **Data Transformation**
2. **Model Training** ➔ **Model Evaluation** ➔ **Model Deployment**
3. **CI/CD Automation** with GitHub Actions, Docker, AWS EC2, and ECR

---

## 💬 Connect

[svg](https://github.com/vikashishere/YT-MLops-Proj1/tree/main#-connect)

If you found this project helpful or have any questions, feel free to reach out!

---

This README provides a structured walkthrough of the MLOps project, showcasing the end-to-end pipeline, cloud integration, CI/CD setup, and robust data handling capabilities.
