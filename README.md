# Cybersec AI Platform Datasets

This repository contains synthetic datasets generated for the **Cybersec AI Platform** project, a unified ecosystem for detection, privacy, developer security, incident response, and cyber education.

## Overview

The datasets included here are tailored for two specific machine learning tools within the platform's architecture:

### 1. Synthetic Cybercrime Incident Corpus (`synthetic_cybercrime_corpus.csv`)
* **Purpose:** Built for **Tool F-20 (1-Click Case Filing)** and **Tool F-24 (OCR Scam Evidence)**.
* **Volume:** 15,000 synthetic scam samples.
* **Details:** This dataset covers five formal Indian cybercrime reporting categories: Financial UPI/Banking Fraud, Job Offer Scams, Cyberbullying/Harassment, Matrimonial/Impersonation Scams, and Identity Theft. 
* **Data Points:** It includes raw complaint narratives, temporal logs, monetary loss values, scam vectors (WhatsApp, SMS, Telegram, Phone), suspect bank/UPI identifiers, and synthetic OCR screenshot evidence text. It is fully anonymized and contains zero PII.

### 2. Nuclei Rule-to-Patch Mapping Corpus (`cwe_patch_corpus.csv`)
* **Purpose:** Built for **Tool F-17 (Automated Bug Remediation)**.
* **Volume:** 1,200 curated CWE (Common Weakness Enumeration) patch pairs.
* **Details:** Contains configuration files and source code fragments exhibiting vulnerable states matched directly to secure remediation snippets (e.g., missing Content-Security-Policy headers, exposed `.git` directories, misconfigured CORS flags).
* **Data Points:** Includes Nuclei Template IDs, CWE/CVE mappings, vulnerable syntax token sequences, recommended replacement patch diffs, and operational remediation explanations.

## Usage

* **Data Generation:** The Python scripts (`generate_dataset.py` and `generate_cwe_dataset.py`) used to build these CSV files are included. You can modify the scripts to tweak data distributions, introduce new vectors, or increase the volume of synthetic samples.

* **Privacy Standard:** Fully synthetic & anonymized; zero PII; designed to be compliant with the IT Act / GDPR.
