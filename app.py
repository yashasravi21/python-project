from flask import Flask, render_template
import psutil
import docker

app = Flask(__name__)

@app.route("/")
def dashboard():

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    try:
        client = docker.from_env()
        containers = client.containers.list()
        container_count = len(containers)
    except Exception:
        container_count = "N/A"

    return render_template(
        "index.html",
        cpu=cpu,
        memory=memory,
        disk=disk,
        containers=container_count
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
