# CLO835 — Assignment 3

Starter applications for **CLO835 Assignment 3: Automate the build with GitHub Actions and deploy a versioned application to Kubernetes.**

---

## What you are building

A simple web service that returns one text message on **port 8080**, deployed to a **kind** Kubernetes cluster through an automated CI/CD pipeline. You ship **two versions**:

| Version | The app returns |
|---|---|
| **0.2** | `Hello world from the CLO835 class!` |
| **0.3** | `Hello world from the CLO835 class and 10112233!` |

`10112233` must be **your own Seneca student ID**. Everyone's running app is unique.

## Language

This submission uses **Python 3.14** (`apps/python/app.py`).

Run locally: `python3 apps/python/app.py`

Then check it: `curl http://localhost:8080` → `Hello world from the CLO835 class!`

The `MESSAGE` constant in `app.py` is the only line that changes between v0.2 and v0.3.

## What was completed

1. **`Dockerfile`** — build your chosen app into an image that serves on port 8080.
2. **`.github/workflows/docker.yml`** — on merge to `master`, log in to Docker Hub and build + push the image tagged with the version (`0.2`) and the commit SHA.
3. **`k8s/deployment.yaml`** and **`k8s/service.yaml`** — a 3-replica Deployment (`apps/v1`) and a NodePort Service for your kind cluster.

## Rules

- **Never commit Docker Hub passwords or tokens.** Store them as GitHub Actions **secrets** (e.g. `DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`).
- All commits must be dated **before** the due date.
- The **report** of challenges faced is **mandatory**.
- Your **student ID must appear** in the version 0.3 output.

## Deploy / update / rollback (quick reference)

```bash
# deploy v0.2
kubectl apply -f deployment.yaml -f service.yaml
kubectl get deploy,rs,pods,svc

# release v0.3 (after the pipeline pushed <user>/<repo>:0.3)
kubectl set image deployment/<name> <container>=<user>/<repo>:0.3
kubectl rollout status deployment/<name>
kubectl rollout history deployment/<name>

# roll back to v0.2
kubectl rollout undo deployment/<name>
kubectl rollout status deployment/clo835-app

# Self-healing demo (bonus)
kubectl delete pod <pod-name>
kubectl get pods -w
```