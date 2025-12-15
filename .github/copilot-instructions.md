<!-- Auto-generated guidance for AI coding agents. Keep concise and codebase-specific. -->
# Copilot / AI agent instructions — python-robotics-journey

Summary
- **Repo state:** minimal; contains [README.md](README.md) and `LICENSE` only. There is no src, tests, or dependency manifest yet.

When you start
- **Read:** open [README.md](README.md#L1) to confirm the project's intent.
- **Ask clarifying questions** before creating or modifying large scaffolding (e.g., package layout, Python version, or CI).

What to do first (short, discoverable tasks)
- If the user asks for code examples or exercises, create them under a new `src/` or `notebooks/` folder and state the chosen layout in PR description.
- When adding dependencies, add a `requirements.txt` or `pyproject.toml` and include exact pinned versions.
- If you add runnable scripts, include minimal usage in `README.md` and a short smoke test in `tests/`.

Project-specific patterns and constraints
- **No existing conventions detected.** Use common, explicit Python patterns when introduced: a top-level `src/<pkg>` layout, `tests/` with `pytest`, and a `requirements.txt` for dependencies.
- **Keep changes small & explicit.** Each PR should: 1) describe intent, 2) list added files, 3) include a minimal test or manual verification step.

> Examples
- Adding a simple exercise: create `src/example_exercise/__init__.py`, `src/example_exercise/demo.py`, and `tests/test_demo.py` with a single pytest asserting expected output.
- Adding deps: create `requirements.txt` with `numpy==1.26.0` (example) and update `README.md` usage section.

Commit / PR guidance for AI agents
- **Commit message format:** short imperative summary, e.g. "Add example exercise and tests".
- **Branch name:** `ai/<short-description>` (e.g., `ai/add-exercise`).

If you can't proceed
- Stop and ask the user when: architectural choices are required, or when introducing CI, Docker, or new major dependencies.

Questions for reviewer (include in PR body)
- Why is this change required? (reference user request)
- How should the project be structured long-term (package name, test strategy, CI)?

Maintenance note for humans
- This guidance was generated from the repo snapshot (README.md only). Update this file after adding source code or CI so future agents have concrete patterns to follow.
