#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

NEW_VERSION=$(bumpversion --dry-run --list minor | \
                 grep new_version | sed -r s,"^.*=",,)
git flow release start v$NEW_VERSION
bumpversion minor
git flow release publish
git flow release finish
git checkout master
git push origin master --tags
git checkout develop
git push origin develop --tags
