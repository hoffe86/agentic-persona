# Release preferences

Apply within the consent rules of the `git-workflow` skill: tagging and
publishing a release need explicit user approval.

## Versions and releases

- Version with [Semantic Versioning](https://semver.org/): breaking change →
  major, `feat` → minor, `fix` → patch.
- Tag releases on `main` as annotated tags in `vMAJOR.MINOR.PATCH` form. Do not
  move or delete published tags.
- Generate release notes from the Conventional Commits PR titles merged since
  the previous tag, grouped by type. Prefer the repository's existing release
  tooling; do not introduce new tooling without approval.
- Fix a released version with a new patch release from `main`. Create a
  short-lived maintenance branch from the tag only when an older supported
  version needs a fix, and delete it when support ends.
