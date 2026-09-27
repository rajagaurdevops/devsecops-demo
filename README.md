# 🛡️ DevSecOps Pipeline Demo

This repository demonstrates a fully functional, production-ready **DevSecOps** pipeline using GitHub Actions. It scans application code, Git history, and Infrastructure as Code (IaC) for security vulnerabilities *before* deploying to AWS.

---

## 🧐 What is DevSecOps?

**DevSecOps** stands for *Development, Security, and Operations*. 

In traditional DevOps, security checks were often performed at the very end of the software development lifecycle (usually by a separate security team). If a vulnerability was found, the code was sent all the way back to the developers, causing massive delays.

DevSecOps **"shifts security left"**. This means integrating automated security tools directly into the CI/CD pipeline. Every time a developer pushes code, the pipeline automatically scans it for passwords, bad coding practices, and cloud misconfigurations. If a critical vulnerability is found, the pipeline fails and blocks the deployment immediately.

---

## ⚙️ How This Pipeline Works

This pipeline triggers automatically whenever code is pushed to the `main` branch or a Pull Request is opened. 

It executes in two main phases:

### Phase 1: Security Scanning (The "Sec" in DevSecOps)
All scanners run in parallel or sequentially. If *any* scanner finds a critical vulnerability, it will upload a SARIF report to the GitHub Security Dashboard and fail the job.
1. **SAST Scan:** Scans the Python application code for bad coding practices.
2. **Secret Scan:** Scans the entire Git commit history to ensure no API keys or passwords are being leaked.
3. **IaC & Vulnerability Scan:** Scans the Terraform files to ensure AWS resources are configured securely (e.g., blocking public access, enabling encryption).

### Phase 2: Infrastructure Deployment (The "Ops" in DevSecOps)
This phase **only runs if Phase 1 passes perfectly**. 
1. **Terraform Init:** Initializes the backend and providers.
2. **Terraform Plan:** Generates an execution plan comparing the code to the real AWS environment.
3. *(If on the `main` branch)* **Terraform Apply:** Deploys the secure infrastructure to AWS.

---

## 🛠️ Tools We Are Using

This pipeline integrates several industry-standard open-source security tools:

| Tool | Category | What it does in this pipeline |
|------|----------|-------------------------------|
| **GitHub Actions** | CI/CD | The orchestrator that runs the pipeline and blocks deployments. |
| **Bandit** | SAST | Scans the `app.py` Python code to catch security issues like running a web server in `debug=True` or binding to `0.0.0.0`. |
| **Gitleaks** | Secret Scanning | Deep-scans the Git history looking for leaked AWS Keys, Slack Tokens, and passwords. |
| **Trivy** (Aqua Security) | IaC & CVE Scanning | Scans the `terraform/` folder for cloud misconfigurations (like public S3 buckets) and scans the filesystem for vulnerable dependencies. |
| **Terraform** | IaC | Provisions the AWS infrastructure securely once all tests pass. |

---

## 📂 Project Structure

- `/.github/workflows/devsecops.yml`: The core CI/CD pipeline definition.
- `/app/app.py`: A simple Python application used to test the Bandit SAST scanner.
- `/terraform/main.tf`: AWS Infrastructure code used to test the Trivy IaC scanner.

---

## 💡 Key DevSecOps Concepts Demonstrated
* **Blocking Deployments:** The `terraform` job `needs: security_scan`. If a developer leaks a secret, Terraform will refuse to run.
* **SARIF Integration:** Security reports are generated in `.sarif` format and uploaded directly to GitHub's native **Security -> Code Scanning** dashboard.
* **Risk Acceptance:** Sometimes security rules don't apply to a specific use case. This repo demonstrates how to use inline comments (e.g., `# trivy:ignore:AVD-AWS-0132`) to document accepted risks and bypass the scanner safely.
