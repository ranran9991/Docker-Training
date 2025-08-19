Docker Training Program for Data Scientists
=========================================

This repository contains materials for a self-paced, one-day (~6-8 hours) Docker training program designed for data scientists. The program teaches how to manage Docker images in a local repository, build Dockerfiles, create containerized apps (e.g., APIs, Gradio), and handle data persistence using volumes. It is designed to work offline after initial setup.

## Prerequisites
- **Software**: Docker Desktop (Windows/Mac) or Docker Engine (Linux). Download from https://www.docker.com/products/docker-desktop/ (pre-download for offline use).
- **Skills**: Basic Python and command-line familiarity.
- **System**: 10GB free disk space, admin rights for Docker installation.
- **Optional**: Git for cloning this repository.

## Setup Instructions
1. **Clone or Download**:
   - Clone: `git clone <repository-url>`
   - Or download and unzip the repository.

2. **Offline Docker Images**:
   - Pre-download required images:
     ```
     docker pull python:3.10-slim
     docker pull registry:2
     ```
   - Save for offline use:
     ```
     docker save -o python-3.10-slim.tar python:3.10-slim
     docker save -o registry-2.tar registry:2
     ```
   - Include `python-3.10-slim.tar` and `registry-2.tar` in the repository root if working offline.
   - Load images offline:
     ```
     docker load -i python-3.10-slim.tar
     docker load -i registry-2.tar
     ```

3. **Verify Docker**:
   - Run `docker --version` to confirm installation.
   - Test with `docker run hello-world`.

## Repository Structure
- `DockerTrainingGuide.md`: Step-by-step guide for the training program (6 modules + final project).
- `simple-python/`: Basic Python app to summarize a CSV.
  - `script.py`, `requirements.txt`, `Dockerfile`
- `streamlit-app/`: Streamlit app for a sentiment analysis demo.
  - `app.py`, `requirements.txt`, `Dockerfile`
- `gradio-app/`: Gradio app for a text-reversal demo.
  - `app.py`, `requirements.txt`, `Dockerfile`
- `multistage/`: Multi-stage build example for a Gradio app.
  - `gradio_app.py`, `requirements.txt`, `Dockerfile`
- `data-persistence/`: App demonstrating data persistence with volumes.
  - `app.py`, `requirements.txt`, `Dockerfile`
- `troubleshooting.txt`: Common Docker issues and fixes.
- `cheatsheet.txt`: Key Docker commands for quick reference.

## How to Use
1. Read `DockerTrainingGuide.md` for the full program.
2. Follow each module’s exercises in order:
   - Module 1: Run a basic container.
   - Module 2: Manage images in a local registry.
   - Module 3: Build a simple Dockerfile.
   - Module 4: Containerize a web app (Streamlit/Gradio).
   - Module 5: Use volumes for data persistence.
   - Module 6: Build a custom FastAPI app.
3. Use `troubleshooting.txt` for issues and `cheatsheet.txt` for commands.
4. Save your final project files for review.

## Offline Usage
- Ensure `python:3.10-slim` image is loaded.
- All dependencies are specified in `requirements.txt` files, installed during Docker builds.
- No internet is required after setup.

## Troubleshooting
- See `troubleshooting.txt` for common issues (e.g., port conflicts, permissions).
- Use `docker logs <container_id>` to debug containers.
- Ensure Docker Desktop is running (Windows/Mac) or Docker service is active (Linux).

## Contributing
Feel free to submit issues or pull requests for improvements to the training materials.
