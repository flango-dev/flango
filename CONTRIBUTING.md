# Contributing to flango

Welcome! We're happy to have you here. Thank you in advance for your contribution to flango.

## Basics

flango welcomes contributions in the form of pull requests.

### Prerequisites

- [Install `copier`](https://copier.readthedocs.io/en/stable/#installation).
- Fork this project in GitHub and clone it.
- Create a `flango_test` dir next to `flango`:

    flango
    flango_test

### Development

- Add/change/remove scaffolding code in `flango`,
- in `flango_test` dir next to `flango` run `copier copy ../flango .`,
- setup `flango` like described in `README.md` and test add/change/remove out,
- iterate via `cd ..; rm -r flango_test; mkdir flango_test; cd flango_test`, `copier copy ../flango .`, `just venv-setup; just database-setup-local`, `just project-run`,
- push changes to your GitHub repo fork,
- create PR.
