# End-to-End ML Pipeline: IT Customer Support Ticket Classification with Logistic Regression

**This repository has been modeled after Microsoft Learn's Hands On Exercises, so please follow the link in the Resources section below for detailed steps on initial set up**

This project demonstrates how to build and deploy a machine learning pipeline in **Azure Machine Learning (Azure ML)**. It walks through a complete MLOps workflow: data prep, model training, model registration, deployment, and endpoint testing.

## Real-world Usage
Once deployed, the model is accessible via a **secure HTTPS endpoint**. You can use this endpoint from any client - including a **Visual Studio Code (VS Code) web app** - by consuming the:
- **Deployment URI** (provided by Azure ML)
- **Access token or key** (for authentication)

> This makes it easy to integrate machine learning predictions into your frontend applications or internal tools.

---

## Dataset

The dataset used is the Tobi-Bueck/customer-support-tickets from Hugging Face, which includes multilingual customer support requests labeled with ticket types. The dataset was then filtered to 'en' only observations.

---

## What This Project Does

1. **Prepares customer support ticket data** (cleans, filters, and feature engineering).
2. **Trains a logistic regression model** using Scikit-learn and logs it with MLflow.
3. **Registers the model** in Azure ML workspace.
4. **Deploys the model to an online HTTPS endpoint**
5. **Tests the endpoint** using both:
   - Sample JSON (`sample-data.json`) via Azure ML SDK
   - External client apps like your **VS Code web app**

---

## Requirements

- Azure Subscription
- Visual Studio Code

---

## Resources
- Visit [Microsoft's Data Scientist Career Path](https://learn.microsoft.com/en-us/plans/wrm2co1324n1z5?source=docs) for more information.
- Visit [Microsoft Learn - Hands On Exercises](https://microsoftlearning.github.io/mslearn-azure-ml/) and choose any of the exercises for detailed instructions on initial set up, such as running the notebook on compute instance Terminal app on the **Python 3.10 - Azure ML** kernel.
