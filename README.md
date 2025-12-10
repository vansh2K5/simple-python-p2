# Jenkins Python Demo Project

This is a minimal Python project to test a Jenkins pipeline.

## Files

- `main.py` – simple script that prints a greeting.
- `Jenkinsfile` – Jenkins declarative pipeline definition.
- `requirements.txt` – place to list Python dependencies.

## Run locally

```bash
python main.py --name YourName
```

## Jenkins

Point a Jenkins job at this repo/directory. The `Jenkinsfile` will:

- Checkout the code
- Optionally show the Python version
- Install dependencies from `requirements.txt`
- Run `main.py` with a sample name
