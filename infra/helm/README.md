# helm/

Helm chart packaging (mostly) of the same resources as `infra/k8s/base/`, for
teams that prefer `helm install` over `kubectl apply -k`. Pick one, don't run
both against the same cluster/namespace.

```bash
helm lint infra/helm/desktop-app-repo
helm install desktop-app-repo infra/helm/desktop-app-repo -f infra/helm/desktop-app-repo/values.yaml
```
