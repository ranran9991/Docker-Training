# Troubleshooting Common Docker Issues

1. **Docker not running**:
   - Error: "Cannot connect to the Docker daemon"
   - Fix: Ensure Docker Desktop is running (Windows/Mac) or Docker service is active (Linux: `sudo systemctl start docker`).

2. **Port already in use**:
   - Error: "Bind for 0.0.0.0:8501 failed: port is already allocated"
   - Fix: Check running containers (`docker ps`), stop conflicting ones (`docker stop <container_id>`), or use a different port.

3. **Image pull fails**:
   - Error: "Error response from daemon: Get ... not found"
   - Fix: Ensure `python:3.10-slim` and `registry:2` are pre-downloaded for offline use. Check with `docker images`.

4. **Permission denied**:
   - Error: "Permission denied when accessing files"
   - Fix: Add `USER 1000` in Dockerfile or run container with `--user $(id -u)`.

5. **App not accessible in browser**:
   - Check: Is the container running? (`docker ps`)
   - Fix: Verify port mapping (`-p 8501:8501` for Streamlit) and try `http://localhost:<port>`. Check firewall settings.

6. **Build errors**:
   - Error: "Failed to install package"
   - Fix: Ensure `requirements.txt` is correct and packages are compatible with `python:3.10-slim`.

Use `docker logs <container_id>` to debug container issues.