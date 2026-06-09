# Assessment Fast Single Repo

This single repository contains:

- Flask demo application
- Dockerfile
- GitHub Actions CI workflow
- Kubernetes manifests
- ArgoCD application manifest
- Datadog Helm values
- AI troubleshooting helper script

## Replace placeholders

Replace:

```text
pareenrathore
pareenrathore
PASTE_DATADOG_API_KEY_HERE
```

## Local Docker test

```bash
docker build -t pareenrathore/assessment-app:latest .
docker run -d --name assessment-app -p 5000:5000 pareenrathore/assessment-app:latest
curl http://localhost:5000/health
```

## Push to DockerHub

```bash
docker login
docker push pareenrathore/assessment-app:latest
```

## Deploy to EKS

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods -n assessment
kubectl get svc -n assessment
```

Open the LoadBalancer EXTERNAL-IP/DNS in browser.

## ArgoCD

```bash
kubectl apply -f argocd/application.yaml
kubectl get applications -n argocd
```

## Datadog

```bash
helm repo add datadog https://helm.datadoghq.com
helm repo update
helm install datadog-agent datadog/datadog -f datadog/values.yaml
kubectl get pods -A | grep datadog
```

## AI Troubleshooting

```bash
chmod +x ai-agent/troubleshoot.sh
./ai-agent/troubleshoot.sh assessment
```