# Contributing to Jarvis Voice Assistant

Thanks for taking the time to contribute. This is a student project, so contributions should be practical and focused.

---

## How to contribute

1. Fork the repository
2. Create a branch for your change

```bash
git checkout -b feature/your-feature-name
```

3. Make your changes and test them locally
4. Commit with a clear message

```bash
git commit -m "Add: brief description of what you added"
```

5. Push to your fork and open a Pull Request

---

## What to work on

Check the open issues. If you want to work on something not listed, open an issue first so we can discuss it before you spend time on it.

Good areas to contribute:

- Expanding the music library
- Adding new voice commands to `processcommand()`
- Improving error handling in the recognition loop
- Replacing hardcoded API keys with proper `.env` loading
- Writing tests

---

## Code style

- Follow PEP 8 for Python code
- Keep functions small and focused
- Add a comment if the logic is not immediately obvious
- Do not commit API keys, `.env` files, or `temp.mp3`

---

## Reporting bugs

Open a GitHub issue with:

- What you expected to happen
- What actually happened
- Your OS, Python version, and any relevant error messages

---

## Pull request checklist

- [ ] Code runs without errors
- [ ] No API keys or secrets in the diff
- [ ] `temp.mp3` is not committed
- [ ] Description explains what changed and why
