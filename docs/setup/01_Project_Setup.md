# AEVON

# 01 — Project Setup

---

**Document:** 01_Project_Setup

**Version:** 1.0

**Status:** Active

**Owner:** Chief Architect

**Classification:** Development Environment

---

# Purpose

This document describes the standard procedure for establishing an AEVON development environment on a new machine.

Upon successful completion, the machine shall be capable of developing, testing, and maintaining AEVON and shall be ready for Google Authentication and AI Provider configuration.

---

# Scope

This document covers:

- System requirements
- Required software
- Repository setup
- Python virtual environment
- Dependency installation
- Local environment configuration
- Initial verification

This document does not cover:

- Google Authentication
- AI Provider configuration
- Deployment
- Migration

---

# Prerequisites

Before beginning, ensure that you have:

- Internet connection
- GitHub access to the AEVON repository
- Administrator privileges (if required)
- Required project credentials

---

# System Requirements

## Supported Operating Systems

- Windows 11 (Recommended)
- Windows 10 (Supported)
- Linux (Future Support)
- macOS (Future Support)

---

## Recommended Hardware

| Component | Recommendation |
|-----------|----------------|
| Processor | Intel Core i5 / AMD Ryzen 5 or better |
| Memory | 16 GB RAM or higher |
| Storage | Minimum 20 GB free SSD space |
| Internet | Stable broadband connection |

---

# Required Software

Install the following software before proceeding.

| Software | Purpose |
|----------|---------|
| Git | Version Control |
| Python 3.12+ | Development Runtime |
| Visual Studio Code (Recommended) | Code Editor |
| PowerShell / Terminal | Command Line Interface |

Verify installation using:

```bash
git --version
python --version
pip --version
```

---

# Repository Setup

Clone the AEVON repository.

```bash
git clone <repository-url>
```

Navigate to the project directory.

```bash
cd AEVON
```

---

# Python Virtual Environment

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the environment.

### Windows

```powershell
.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

# Install Project Dependencies

Install all required packages.

```bash
pip install -r requirements.txt
```

If dependency updates are required in the future, rerun the above command.

---

# Local Environment Configuration

Create the local environment configuration file if required.

```
.env
```

Populate the file using the project environment template.

Sensitive information such as API keys shall never be committed to the repository.

---

# Initial Verification

Verify that:

- Git is installed.
- Python is installed.
- Virtual environment is active.
- Dependencies installed successfully.
- No installation errors occurred.

---

# Verification Checklist

## Development Machine

- [ ] Git installed
- [ ] Python installed
- [ ] Repository cloned
- [ ] Virtual environment created
- [ ] Virtual environment activated
- [ ] Dependencies installed
- [ ] Environment configured
- [ ] Project opens successfully

---

# Troubleshooting

## Git Not Found

Ensure Git is installed and available in the system PATH.

---

## Python Not Found

Verify that Python has been installed correctly and added to the system PATH.

---

## Virtual Environment Activation Failed

Confirm that the virtual environment was created successfully before attempting activation.

---

## Dependency Installation Failed

Review the error message, verify internet connectivity, and ensure the correct Python version is installed.

---

# Completion

Upon completion of this document, the development machine is prepared for configuring external services.

Proceed to:

**02_Google_Authentication.md**

---

**End of Document**
