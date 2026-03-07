# project-boilerplate

A reusable project template with a clean structure and pre-configured setup to kickstart new projects.

## 🚀 Getting Started

This project uses [**uv**](https://github.com/astral-sh/uv) for fast, reproducible environment setup.

### Prerequisites

`uv` is installed automatically by the setup script if not already present. You can also install it manually:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Environment Setup

Run the setup script to create the virtual environment and install all dependencies:

```bash
bash scripts/setup_env.sh
```

You can optionally specify a Python version (default is 3.12):

```bash
bash scripts/setup_env.sh 3.11
```

The script will:
1. Install `uv` if it is not found on the system.
2. Create a `.venv` virtual environment using `uv venv .venv`.
3. Install all project dependencies from `requirements.txt` via `uv pip install -r requirements.txt`.
4. Install the project itself in editable mode via `uv pip install -e .`.

### Activating the Environment

```bash
source .venv/bin/activate
```

> **Note for pip users:** If you strictly cannot use `uv`, you can still set up the environment manually with `python -m venv .venv`, `pip install -r requirements.txt`, and `pip install -e .`. However, `uv` is the recommended and primary tool for this repository.

---

Use the following prompt to generate a full README.md file for your project:

```markdown
Read the project then Generate a comprehensive professional README for this project. Structure it with the following sections: Introduction, Features,  Project Structure, Installation, Usage, Contributing, License, Acknowledgments. Add subsections if you want. Add Emojis. Add GitHub badges at the top of the Readem. Ensure the tone is friendly and approachable, with clear instructions that are easy for both developers and end-users to understand. Emphasize any important details about the project where applicable, such as installation steps and usage examples. 
```
