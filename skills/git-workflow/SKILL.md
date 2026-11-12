---
name: git-workflow
description: >-
  The owner's optional Git preferences: trunk-based branching, one worktree per
  feature, branch naming, Conventional Commits, squash-merged PRs and SemVer
  releases. Use when creating a branch or worktree, writing a commit message or
  PR title, preparing or updating a PR, or cutting a release. Not for routine
  read-only git status, diff or log. Grants no permission to commit, push,
  merge or tag.
---

# Git workflow

## Scope and consent

These are personal preferences, not repository policy. Existing branch
protection, contribution guides, CI rules, release tooling and accepted
decisions govern; surface conflicts instead of overriding them.

Consent rules from `working-style` apply unchanged: **do not commit, push,
create a PR, merge, tag or publish a release without explicit user approval**.
Never push directly to `main`. This skill describes how to do these steps once
approved; it never authorizes them. Do not change branch protection, repository
settings, remotes or CI configuration without separate approval.

## Branching

Prefer **trunk-based development**:

- `main` is always releasable and protected. All changes reach it through a PR.
- Before creating a feature branch or worktree, fetch the intended base from its
  configured remote and verify the starting commit matches that freshly fetched
  branch tip. A local `HEAD` or cached remote-tracking ref alone does not prove
  freshness. Normally branch from the fetched remote `main`; if branching from
  `HEAD`, verify it matches that tip first. Use a different base only when
  explicitly intended, such as a stacked PR. Do not reset local branches,
  discard changes or alter another worktree to make them match. If fetching
  fails, report that freshness could not be verified and stop branch creation.
- Use one **short-lived** feature branch per change, cut from current `main`.
  Merge it within days, not weeks. Split larger work into small, independently
  mergeable PRs; use feature flags or stacked PRs for incomplete features rather
  than long-running branches.
- Do not create `develop`, long-lived `release/*` or environment branches.
  Environments are reached by promoting the same build artifact, not by merging
  between branches.
- Delete branches after merge.

## Worktrees

Use **exactly one worktree per repository and feature**:

- Each feature gets its own worktree on its own feature branch. Do not create a
  second worktree for a feature that already has one; reuse the existing
  worktree, including for follow-up changes, fixes and review feedback.
- When a feature spans several repositories, create one worktree in each
  affected repository, using the same branch name.
- Do not work on a feature from the main checkout and a worktree at the same
  time, and do not check out one branch in several places.
- Remove the worktree after its branch is merged or abandoned
  (`git worktree remove`, then `git worktree prune`). Remove only worktrees you
  own, and never with uncommitted changes unless the owner approves discarding
  them.
- If tooling manages worktrees, follow its location and lifecycle.

## Branch naming

Use `type/short-description` in lowercase kebab-case, for example
`feat/add-login` or `fix/token-refresh-race`.

- `type` uses the Conventional Commits types listed below.
- Keep the description short and specific; describe the change, not the person
  or the date.
- If tooling or the workspace already assigns a branch name or prefix, keep it.

## Commits and PR titles

Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):
`type(scope): summary`.

- Types: `feat`, `fix`, `docs`, `refactor`, `perf`, `test`, `build`, `ci`,
  `chore`, `revert`. Scope is optional; use the module, service or skill name.
- Summary in imperative mood, lowercase start, no trailing period, about 72
  characters at most.
- Mark breaking changes with `!` after the type or scope and a
  `BREAKING CHANGE:` footer that explains the migration.
- The body explains **why**, not a line-by-line list of what changed.
- Keep each commit focused and buildable. Never commit secrets, generated
  artifacts or local configuration; extend `.gitignore` when needed.
- Keep required trailers such as `Co-authored-by` or sign-off lines.

Because PRs are **squash-merged**, the **PR title becomes the commit on `main`**
and must follow the Conventional Commits format. Commits inside the branch may
be less formal, but should still be meaningful for reviewers.

## Pull requests

- Keep PRs small and focused on one concern; review effort grows faster than
  size.
- The description states the problem, the approach, how it was verified and
  any risk or follow-up. Link the work item or issue.
- Run the repository's build, tests, lint and format checks before requesting
  review. Do not claim unrun checks passed.
- Open a draft PR for early feedback; mark it ready only when checks pass.
- Merge with **squash merge** after required reviews and checks pass. Do not
  bypass protection or required checks.

## Keeping branches current

- Update a feature branch from `main` by **rebasing** while the branch is
  unshared or only you work on it. If others share the branch, merge `main`
  in instead.
- Force-push only your own feature branch, only with `--force-with-lease`, and
  only after approval for pushes. Never force-push `main` or shared branches.
- Never rewrite history that is already on `main`. Undo merged changes with
  `git revert`, not reset.
- Resolve conflicts by understanding both sides; never discard someone else's
  change to make a conflict disappear.

## Versions and releases

When tagging, versioning or writing release notes, read the
[release preferences](references/releases.md). Release notes and Git history
own change tracking; product documentation describes only the current state.

## Sources

- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)
- [Semantic Versioning 2.0.0](https://semver.org/)
- [Trunk-based development](https://trunkbaseddevelopment.com/)
- [Git worktree documentation](https://git-scm.com/docs/git-worktree)
- [GitHub: About merge methods](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github)
