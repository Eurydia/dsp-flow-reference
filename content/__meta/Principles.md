# Principles

## Style Conventions

While writing notes, the content must be written with the following in mind:
- ~~**Markdown syntax**: Notes must be written in basic Markdown syntax to ensure portability~~
- **In-game items**: Mentions of in-game items are capitalized based on what is displayed in the game

## Vault Structure

To ensure the compatibility as an Obsidian vault, the `content/` directory is the root directory, instead of the repository.

This measure is done to avoid the inclusion of `git` such as `.gitignore`, `LISCENSE` and, `README,md` files in Obsidian.

The vault structure is separated into two categories of directories.

**Private directories** are prefixed with two underscores.
- `__media/` contains non-note non-blueprint files such as images and visuals.
- `__meta/` contains notes which describes the vault itself

## Blueprint Design Conventions

All blueprints must be designed with the following conventions in mind.

- **Grounded**: Conveyor Belts must not leave the ground level
- **Manhattan geometry**: Conveyor Belts must follow the Manhattan geometry
- **End-extensible**: A module extends one another at the end, not the front
- **Belt connection**: A facility can connect to a line of Conveyor Belt at most once
