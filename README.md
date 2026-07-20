# python-project
This is My Python Project Flowchart 

---
config:
  layout: elk
  theme: forest
  look: handDrawn
  fontFamily: '''Merriweather Variable'', serif'
  themeVariables:
    fontFamily: '''Merriweather Variable'', serif'
---
flowchart TB
    Developer["👨‍💻 Developer<br>Git Push"] -- Push Code --> GitHub["🐙 GitHub<br>Source Repository"]
    GitHub -- Webhook Trigger --> Jenkins["🔴 Jenkins<br>Pipeline Trigger"]
    Jenkins -- Execute Pipeline --> BuildDocker["🐳 Build Docker Image<br>Docker Engine"]
    BuildDocker -- Build & Tag --> DockerHub["🏗️ Docker Hub<br>Push Image"]
    DockerHub -- Pull Image --> K8s["☸️ Kubernetes Cluster<br>Minikube"]
    K8s -- Deploy --> Pod1["📦 Pod-1<br>Flask App"] & Pod2["📦 Pod-2<br>Flask App"]
    Pod1 -- Register --> Service["🔗 Kubernetes Service<br>NodePort Service"]
    Pod2 -- Register --> Service
    Service -- Route Traffic --> Browser["🌐 Browser<br>localhost:NodePort"]
