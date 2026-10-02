# Contributing

Use a feature branch for each change and open a pull request into `master`. Do not commit directly to `master`.

## Branch Workflow

From the project directory in PowerShell, start with an up-to-date `master` branch:

```powershell
git switch master
git pull --ff-only
git switch -c feature/short-description
```

Make the change, then stage and commit it:

```powershell
git add .
git commit -m "Describe the change"
git push -u origin feature/short-description
```

## Pull Request Checklist

- Open a pull request from the feature branch into `master`.
- Summarize the change and note how it was checked.
- Run the application with `python main.py` and confirm the demo works.
- Address review feedback before merging.
- When repository settings allow, use a merge commit to preserve the branch merge in Git history.

After the pull request is merged, update the local `master` branch:

```powershell
git switch master
git pull --ff-only
```