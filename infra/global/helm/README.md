# helm/

Helm chart packaging (mostly) of the same resources as `infra/global/k8s/base/`, for
teams that prefer `helm install` over `kubectl apply -k`. Pick one, don't run
both against the same cluster/namespace.

```bash
helm lint infra/global/helm/desktop-app-repo
helm install desktop-app-repo infra/global/helm/desktop-app-repo -f infra/global/helm/desktop-app-repo/values.yaml
```
