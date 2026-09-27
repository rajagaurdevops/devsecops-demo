# DevSecOps Demo Project

This project demonstrates a standard DevSecOps pipeline using GitHub Actions, Terraform, and Python.

## Structure
- `/terraform`: Infrastructure as Code (AWS). Contains intentional misconfigurations for `tfsec` / `checkov` to catch.
- `/app`: A simple Python application. Contains intentional security flaws (hardcoded secrets, debug mode) for `bandit` or `trufflehog` to catch.
- `/.github/workflows`: The CI/CD pipeline that enforces security checks before deployment.
