# flango

Base template for scaffolding and upgrading Domain Driven Design Django projects.

Like [Falco](https://github.com/Tobi-De/falco) for creating Django projects from templates,
but with [support for flexible composable code scaffolding](https://copier.readthedocs.io/en/stable/comparisons/)
plus [code updates](https://copier.readthedocs.io/en/stable/updating/)
and tuned for Domain Driven Design.

## Scaffold project

- [Install `copier`](https://copier.readthedocs.io/en/stable/#installation).
- `copier gh:flango-dev/flango project` with directory `project` adjusted to your needs.

## Setup project

- `cd` into the project scaffolded before.
- [Install `just`](https://github.com/casey/just?tab=readme-ov-file#packages).
- `just venv-setup`
- Open VSCode command pallet using `Ctrl+Shift+P`, select Python interpreter from path `.venv/bin/python`.

## Development

Open VSCode tasks using `Ctrl+Shift+B` and select task to run from `Flango:` prefixed tasks.

Open VSCode run and debug view (`Ctrl+Shift+D`) and run launch config `Local Project development` for local development.
