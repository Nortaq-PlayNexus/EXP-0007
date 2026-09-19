# Security Policy — EXP-0007

## Reporting Security Issues

If you discover a security vulnerability in this repository, please report it privately:

- **Email**: <exp-0007-security@example.com>
- **GitHub**: Send private vulnerability report

Do NOT open public issues for security vulnerabilities.

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x | ✓ Current |
| <1.0 | ✗ No support |

## Security Practices

This repository:

- Contains no API keys, tokens, or credentials
- Contains no passwords or private paths
- Uses relative paths and environment variables for configuration
- Stores no personal information
- Uses pinned dependencies where reproducibility requires it

## Security Review Checklist

Before releasing new versions:

- [ ] Scan for hardcoded secrets (API keys, tokens, passwords)
- [ ] Scan for personal paths (C:\Users\... / home/...)
- [ ] Scan for sensitive environment variables
- [ ] Verify no credentials in git history
- [ ] Verify dependency hashes match
- [ ] Review third-party code

## Dependency Security

Dependencies are pinned in `requirements.txt` and `pyproject.toml`. Known vulnerabilities are checked during CI.

## Security Updates

Security updates will be released as patch versions (1.0.x) with security advisory notices.
