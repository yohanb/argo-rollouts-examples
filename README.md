# argo-rollouts-examples

## Prerequisites
- [Argo-CD Autopilot](https://argocd-autopilot.readthedocs.io/en/stable/Installation-Guide/)
- [Argo Rollouts kubectl plugin](https://argo-rollouts.readthedocs.io/en/stable/installation/#kubectl-plugin-installation)

## Bootstrap
1. `EXPORT GIT_TOKEN=<your git token>`
2. `export GIT_REPO=https://github.com/ybelval/argo-rollouts-examples`
3. `argocd-autopilot repo bootstrap` or `argocd-autopilot repo bootstrap --recover`

## Steps to reproduce
1. `kubectl port-forward -n argo-rollouts svc/argo-rollouts-dashboard 3100:3100`
2. open http://localhost:3100
3. make sure you have an `n-1` revision that you can still rollback to (inside `scaleDownDelaySeconds` window)
4. rollback to that revision
5. watch pods in that revision scale down and then back up (according to the canary steps)

### Example of bug
![Monosnap screencast 2023-08-04 16-20-57.gif](..%2F..%2FPictures%2FMonosnap%20screencast%202023-08-04%2016-20-57.gif)