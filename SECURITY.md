# Security Policy

## Supported Versions

This project is currently under active development.
```
| Version | Supported |
|---|---|
| MVP | Yes |
```
---

# Reporting a Vulnerability

Please do NOT create public GitHub issues for security vulnerabilities.

Instead:

- Open a private security advisory
- Or contact the maintainer directly

---

# Security Guidelines

## Never Commit Secrets

Do NOT commit:

- API keys
- Tokens
- Passwords
- `.env` files
- Database dumps

---

# Environment Variables

Use:

- `.env.example`
- Docker secrets
- CI/CD secret stores

Never hardcode secrets.

---

# AI Security Considerations

This project includes AI integrations.

Potential risks include:

- Prompt injection
- Data leakage
- Unauthorized tool execution
- Excessive API usage

Future versions will include:

- Input validation
- Tool permission boundaries
- AI audit logging
- Rate limiting

---

# Dependency Security

Before production:

- pin dependencies
- run vulnerability scans
- use Dependabot
- scan Docker images

---

# Docker Security

Future improvements:

- non-root containers
- minimal base images
- image signing
- runtime scanning

---

# Disclaimer

This project is intended for educational and MVP purposes.
Production deployments require additional security hardening.
