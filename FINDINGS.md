# Security Findings
I created a small task tracking app, which gives users option to create, show and quit the program.

## What the scanners found

The initial version of the repository intentionally contained two security issues.

Gitleaks detected a hard-coded API key stored in `config.py`. The credential was only a fake value for this exercise, but storing credentials directly in source code is unsafe because anyone with access to the repository can see them.

The second issue was detected by pip-audit. The project was using Flask 0.12, which had multiple known security vulnerabilities(CVE-2019-1010083). The GitHub Actions workflow was configured to run both Gitleaks and pip-audit on every push, causing the initial vulnerable version to fail.

## How I fixed them

I removed the hard-coded API key from `config.py` and changed the application to read `API_KEY` from an environment variable. I then stored the credential in GitHub Secrets and configured the workflow to inject it as `API_KEY`.

I also upgraded Flask from 0.12 to 3.1.3. After these changes, both security checks passed successfully in the pull request.

## What GitHub Secrets protects against

GitHub Secrets helps prevent the credential value from being stored directly in the repository source code and avoids exposing it in normal Git history. It also allows the workflow to provide the value to the application without putting it directly in the code.

However, GitHub Secrets does not automatically make an application secure. A secret could still be exposed through application logs, incorrect workflow configuration, or by an attacker who gains access to an environment where the secret is available.

## What I got stuck on

I initially had trouble getting the GitHub Actions workflow to recognize and execute correctly, and then had to verify that Gitleaks was actually detecting the hard-coded credential.Also I got one error because I was using an old version of pip-audits, so I corrected that. I also had to add some new rules for Gitleaks to detect the credential and I used chatGPT for that. 

Overall, I used ChatGPT and Claude during this case study to help troubleshoot GitHub Actions/Gitleaks configuration and workflow structure. I reviewed and tested the suggested changes myself. 

