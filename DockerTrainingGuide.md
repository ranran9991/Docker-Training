# Docker Training Program for Data Scientists

This self-paced program teaches you to use Docker for data science workflows. You'll learn to manage images in a local repository, build Dockerfiles, and create containerized apps (like APIs or Gradio/Streamlit interfaces) accessible externally. Complete it in ~6-8 hours.

## Prerequisites
- **Software**: Docker Desktop (Windows/Mac) or Docker Engine (Linux) installed. Download from [Docker's official site](https://www.docker.com/products/docker-desktop/) (pre-download installer for offline use).
- **Skills**: Basic Python and command-line familiarity.
- **Files**: The accompanying directories, containing python scripts, requirement files and docker files.
- **Setup**: Ensure 10GB free disk space. Admin rights needed for Docker.

## Module 1: Docker Basics (30 mins)
**Goal**: Understand Docker and run your first container.

First, watch this video: [Docker in 100 Seconds](https://www.youtube.com/watch?v=Gjnup-PuquQ).
1. **What is Docker?**
   - Docker creates lightweight containers for consistent app environments.
   - Key terms: *image* (blueprint), *container* (running instance), *Dockerfile* (build instructions), *registry* (image storage).
   - Why use it? Reproducible ML environments, easy sharing.

2. **Exercise 1**: Run a simple container.
   - Open a terminal (Command Prompt/PowerShell on Windows, Terminal on Mac/Linux).
   - Run: `docker run hello-world`
   - Expected output: A message confirming Docker works.
   - Verify setup: `docker --version`

3. **Checkpoint**: If the container fails, check Docker Desktop is running or consult the `troubleshooting.txt` in the code folder.

## Module 2: Working with Images and Local Repositories (1 hour)
**Goal**: Pull, run, and manage images using a local registry.

1. **Setup Local Registry**:
   - Run a local registry: `docker run -d -p 5000:5000 --name registry registry:2`
   - This creates a local Docker registry at `localhost:5000`.

2. **Exercise 2**: Pull and push images.
   - Pull a Python image: `docker pull python:3.10-slim` (pre-download this image if offline).
   - Tag it for the local registry: `docker tag python:3.10-slim localhost:5000/my-python:3.10`
   - Push to local registry: `docker push localhost:5000/my-python:3.10`
   - Remove the local image: `docker rmi localhost:5000/my-python:3.10`
   - Pull it back: `docker pull localhost:5000/my-python:3.10`
   - Run interactively: `docker run -it localhost:5000/my-python:3.10 python`

3. **Checkpoint**: List images (`docker images`) to confirm your tagged image exists.

## Module 3: Building Dockerfiles (1.5 hours)
**Goal**: Create Dockerfiles for simple data science apps.

1. **Dockerfile Basics**:
   - Key instructions: `FROM` (base image), `COPY` (add files), `RUN` (execute commands), `CMD` (default command), `EXPOSE` (ports).
   - Example (in `simple-python` folder):
     ```
     FROM python:3.10-slim
     WORKDIR /app
     COPY script.py .
     CMD ["python", "script.py"]
     ```

2. **Exercise 3**: Build a simple data app.
   - Navigate to `simple-python` (contains `script.py` that loads a CSV with pandas and prints stats).
   - Build the image: `docker build -t my-data-app .`
   - Run it: `docker run my-data-app`
   - Expected output: CSV summary stats.
   - Tag and push to local registry: `docker tag my-data-app localhost:5000/my-data-app` and `docker push localhost:5000/my-data-app`.

3. **Checkpoint**: If the build fails, check `Dockerfile` syntax or consult `troubleshooting.txt`.

## Module 4: Containerizing Web Apps (2 hours)
**Goal**: Build and expose a Gradio app.

1. **Concepts**:
   - Expose ports with `EXPOSE` in Dockerfile and `-p` in `docker run`.
   - Use Python web frameworks (Gradio) for ML demos.

2. **Exercise 4**: Containerize a Gradio app.
   - Navigate to `gradio-app` (contains `app.py` for a simple ML demo, e.g., text sentiment analysis).
   - Dockerfile provided:
     ```
     FROM python:3.10-slim
     WORKDIR /app
     COPY requirements.txt .
     RUN pip install --no-cache-dir -r requirements.txt
     COPY . .
     EXPOSE 7860
     CMD ["python", "app.py"]
     ```
   - `requirements.txt`:
     ```
     gradio==4.44.0     
     ```
   - Build: `docker build -t my-gradio-app .`
   - Run with port mapping: `docker run -p 8501:8501 my-gradio-app`
   - Open `http://localhost:8501` in a browser to view the app.
   - Push to local registry: `docker tag my-gradio-app localhost:5000/my-gradio-app` and `docker push localhost:5000/my-gradio-app`.

3. **Checkpoint**: If the app isn’t accessible, check port conflicts or firewall settings.

## Module 5: Data Persistence (1.5 hours)
**Goal**: Persist data across container runs using volumes.

**Concepts:**
   - Docker volumes mount a host directory to a container, preserving data after the container stops.
   - Useful for saving datasets, model outputs, or logs in data science workflows.

**Exercise 5**: Build and run a persistent data app.
   - Navigate to `data-persistence` (contains `app.py` that reads/writes a CSV file).
   - Dockerfile provided:
     ```
     FROM python:3.10-slim
     WORKDIR /app
     COPY requirements.txt .
     RUN pip install --no-cache-dir -r requirements.txt
     COPY . .
     # Ensure the data directory exists
     RUN mkdir -p /app/data
     CMD ["python", "app.py"]
     ```
   - `requirements.txt`:
     ```
     pandas    
     ```
   - Create a local `data` folder: `mkdir data`
   - Build: `docker build -t my-persistent-app .`
   - Run with volume mount: `docker run -v $(pwd)/data:/app/data my-persistent-app`
   - Check the `data/user_data.csv` file on your host machine to see the persisted data.
   - Run again with a different entry: Modify `app.py` to add a new entry (e.g., `add_entry(2, "Bob", 88)`), Rebuild, and rerun. Verify teh CSV retains the previous data.
   - Push to local registry: `docker tag my-persistent-app localhost:5000/my-persistent-app` and `docker push localhost:5000/my-persistent-app`.
3. **Checkpoint**: Verify the CSV file exists in the `data` folder and contains all entries.

## Module 6: Final Project (1 hour)
**Goal**: Build and deploy a custom app.

1. **Task**:
   - Create a new folder, write a simple FastAPI app (e.g., `/predict` endpoint for a pre-trained model).
   - Example `app.py`:
     ```python
     from fastapi import FastAPI
     app = FastAPI()
     @app.get("/predict")
     def predict(text: str):
         return {"text": text, "sentiment": "positive"}
     ```
   - Write a Dockerfile, build, and run it (port 8000).
   - Push to the local registry.
   - Test: `curl http://localhost:8000/predict?text=hello`

2. **Deliverable**: Save your Dockerfile and app code for review.

## Troubleshooting
- See `troubleshooting.txt` in the code folder for common issues (e.g., port conflicts, permission errors).
- Use `docker ps` to check running containers, `docker images` for images.

## Resources
- `cheatsheet.txt`: Key Docker commands.
- Docker Docs (offline PDF in code folder, if provided).
- Optional: Extend to a personal project (e.g., containerize your ML model).