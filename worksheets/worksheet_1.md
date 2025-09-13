# Hands-On Exercises

### Exercise A — Quick Commit Flow

1. `git clone <demo-repo>`
2. `git switch -c feature/yourname`
3. Edit `README.md`, commit:

   ```bash
   git add README.md
   git commit -m "docs: update README by <yourname>"
   git push -u origin feature/yourname
   ```
4. Open PR in GitHub.

### Exercise B — Simulate Conflict and Resolve

1. Using 2 different branches edit same file.
2. Merge one branch to master, then merge the other — resolve conflicts.
3. EXplore the terminal and editor approaches.
4. Explore the concept of ours and theirs for conflict resolution.

### Exercise C — Rebase & Squash

1. Make 3 small commits on a branch.
2. `git rebase -i HEAD~3` → squash to tidy history.
3. Push branch.
4. Observe the difference in the commit history during merge and rebase.

### Exercise D — CI Workflow

1. Add `.github/workflows/sample_workflow.yml` (simple test).
2. Push branch → verify Actions run on PR.