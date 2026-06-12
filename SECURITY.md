# Security Policy

## Supported Versions

This is a personal project currently under active development. Only the latest version on the main branch is maintained.

---

## Reporting a Vulnerability

If you discover a security issue — for example, a way to extract API keys, bypass input validation, or cause unintended system behaviour — please do not open a public GitHub issue.

Instead, report it privately by emailing the maintainer directly. You can find contact details on the author's GitHub profile.

Please include:

- A clear description of the issue
- Steps to reproduce it
- The potential impact
- Any suggested fix if you have one

I will acknowledge the report within 72 hours and work on a fix as quickly as possible.

---

## API Key Safety

This project uses API keys for OpenAI and NewsAPI. Keys must be stored in a local `.env` file and must never be committed to version control.

The `.gitignore` in this repository excludes `.env` by default. If you accidentally commit a key, revoke it immediately through the respective service's dashboard and generate a new one.
