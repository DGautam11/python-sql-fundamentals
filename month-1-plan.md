# My 6-Month AI Engineer Plan — Month 1: Python & SQL Fundamentals

> **Goal:** Go from "I can use Python and SQL" to "I genuinely own these skills and can pass technical screens."
>
> **Duration:** 30 days
> **Commitment:** 15–18 hours per week
> **Start date:** _______________
> **End date:** _______________

---

## The 6-Month Big Picture

| Month | Focus | Output |
|---|---|---|
| **1** | **Python & SQL mastery** | **GitHub with 4 projects + 40 SQL problems solved** |
| 2 | Math + Classical ML | 2 ML projects from scratch |
| 3 | Deep Learning + PyTorch | 1 DL project built line-by-line |
| 4 | NLP + Transformers + Fine-tuning (owned) | Re-fine-tune a model, fully understood |
| 5 | RAG + Agents + MCP | Edvisor v2 shipped |
| 6 | Production, Evals, Deployment | Portfolio finalized, applying heavily |

**Rule:** Apply to jobs throughout all 6 months. Don't wait.

---

## The Agreement With Myself

**I commit to:**
- 15–18 hours per week, honestly
- No AI for writing project code during Month 1 — only for explaining concepts
- Push commits to GitHub every day I work
- Write a README for every project
- Daily: 1 SQL problem minimum

**I will NOT:**
- Skip SQL practice
- Copy-paste AI-generated code into projects
- Wait until "ready" to apply for jobs
- Try to learn 5 courses at once

---

## Setup Checklist (Do Before Day 1)

### Tools
- [ ] Python 3.11+ installed and verified (`python --version`)
- [ ] VS Code installed with extensions: Python, Pylance, GitLens, Ruff
- [ ] Git installed and configured with my GitHub email
- [ ] GitHub account ready

### Accounts
- [ ] DataLemur account created (datalemur.com)
- [ ] Exercism.io account + Python track joined
- [ ] LeetCode account (for later DSA practice)

### Repository
- [ ] Created public GitHub repo named `python-fundamentals`
- [ ] Cloned locally
- [ ] Added folder structure:
  ```
  python-fundamentals/
  ├── week1-basics/
  ├── week2-oop/
  ├── week3-advanced/
  ├── week4-capstone/
  └── README.md
  ```
- [ ] First commit pushed
- [ ] Virtual environment created: `python -m venv venv`

### Tracking
- [ ] Created a "Month 1 Tracker" document (this file or separate)
- [ ] Saved bookmark list of key resources
- [ ] Decided on daily study time slot (morning before shift recommended)

---

## Daily Habits (Every Single Day)

Before bed, ask myself:
1. Did I open my editor today?
2. Did I commit something to GitHub?
3. Did I solve at least one SQL problem?

**If yes to all three, the day counts.** Even 20 minutes counts. Consistency > intensity.

---

## Week 1 — Python Basics Speedrun (Days 1–3)

Since Python basics are already comfortable, this week is a fast refresh + first project.

### Day 1 (~3 hours) — Setup + Refresh

**Setup (45 min):**
- [ ] Verify all tools installed
- [ ] Create GitHub repo `python-fundamentals`
- [ ] Set up folder structure + virtual environment
- [ ] First commit

**Python refresh — watch on 1.5x speed (90 min):**
- [ ] Corey Schafer: Python Tutorial — Strings and How to Use Them
- [ ] Corey Schafer: Python Tutorial — Lists, Tuples, and Sets
- [ ] Corey Schafer: Python Tutorial — Dictionaries
- [ ] Corey Schafer: Python Tutorial — Comprehensions
- [ ] Corey Schafer: Python Tutorial — Functions
- [ ] Corey Schafer: Python Tutorial — f-strings

**Exercise (45 min):**
- [ ] Read: Real Python "Python Type Checking (Guide)" — first half
- [ ] Add type hints to 5 practice functions
- [ ] Commit `day1-notes.md` with 5 things refreshed

### Day 2 (~3 hours) — File I/O + Start Expense Tracker

**Review (1 hour):**
- [ ] Corey Schafer: File Objects — Reading and Writing Files
- [ ] Corey Schafer: Error Handling — Try / Except

**Start Expense Tracker (2 hours):**
- [ ] Retype the skeleton from scratch (no copy-paste)
- [ ] Implement `add_expense()`
- [ ] Implement `show_total()`
- [ ] Implement `show_by_category()`

**Rules:**
- No AI assistance
- Stuck >15 min → use docs/Stack Overflow
- Type hints on everything
- Commit after each function works

### Day 3 (~3 hours) — Polish + SQL start

**Polish Expense Tracker (1.5 hours):**
- [ ] Implement `main()` CLI loop
- [ ] Add input validation (reject non-numeric amounts)
- [ ] Add `delete_expense()` by index
- [ ] Add CSV export using `csv` module
- [ ] Handle corrupted JSON gracefully

**Write README (30 min):**
- [ ] Features list
- [ ] How to run
- [ ] What I learned
- [ ] Tech stack

**First SQL (1 hour):**
- [ ] Sign up for DataLemur
- [ ] Read their free intro tutorial
- [ ] Solve 3 Easy problems

### End of Week 1 — Self Check

Can I explain these without looking anything up?
- [ ] Difference between a list and a tuple
- [ ] When to use a set over a list
- [ ] What `*args` and `**kwargs` mean
- [ ] What a context manager is, why `with open(...)` is better

### Project 1 Skeleton: Expense Tracker

```python
"""
Expense Tracker CLI
A simple command-line expense tracking application.
"""

import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("expenses.json")


def load_expenses() -> list[dict]:
    """Load expenses from the JSON file. Return empty list if file doesn't exist."""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_expenses(expenses: list[dict]) -> None:
    """Save the expenses list to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def add_expense(expenses: list[dict], amount: float, category: str, note: str = "") -> None:
    """Add a new expense entry to the list."""
    # TODO: implement
    # Hint: use datetime.now().isoformat() for timestamp
    pass


def show_total(expenses: list[dict]) -> None:
    """Print the total spent across all expenses."""
    # TODO: implement
    pass


def show_by_category(expenses: list[dict]) -> None:
    """Print totals grouped by category."""
    # TODO: implement (use a dict to accumulate totals per category)
    pass


def main() -> None:
    """Main CLI loop."""
    expenses = load_expenses()
    # TODO: build a simple menu loop with input() for add/view/quit
    pass


if __name__ == "__main__":
    main()
```

---

## Week 2 — Object-Oriented Programming (Days 4–10)

**This is where real growth happens.** OOP separates beginners from intermediates. Interviewers test it constantly.

### Days 4–5 — Corey Schafer OOP Series (2 hours each)

**Day 4:**
- [ ] OOP Tutorial 1: Classes and Instances
- [ ] OOP Tutorial 2: Class Variables
- [ ] OOP Tutorial 3: Classmethods and Staticmethods
- [ ] Exercise: Build Employee + Manager class system (see below)

**Day 5:**
- [ ] OOP Tutorial 4: Inheritance
- [ ] OOP Tutorial 5: Special (Dunder) Methods
- [ ] OOP Tutorial 6: Property Decorators
- [ ] Exercise: Extend Employee classes with `__repr__`, `__eq__`, `@property`

**Day 4 Exercise — Employee System:**
```python
# Create:
# - Employee class: name, salary, email, raise_amount (class variable)
# - Manager subclass with a list of employees to manage
# - Class variable tracking total employee count
# - Classmethod to create employee from "John-Doe-50000" string
# - Staticmethod to validate if a name is capitalized

# Test by creating 3 employees, 1 manager, calling all methods
```

**Day 5 Exercise — Extend it:**
```python
# Add to Employee:
# - __repr__ for unambiguous representation
# - __str__ for pretty printing
# - __eq__ (two employees are equal if emails match)
# - @property email (computed as f"{first}.{last}@company.com")
# - @email.setter that splits email back into first/last name
# - __len__ on Manager (returns number of employees managed)
```

### Days 6–7 — Reading + Practice (1.5 hours each)

**Day 6:**
- [ ] Real Python: "Object-Oriented Programming (OOP) in Python 3"
- [ ] 2 Exercism.io OOP exercises

**Day 7:**
- [ ] Real Python: "Python's Instance, Class, and Static Methods Demystified"
- [ ] 2 more Exercism.io exercises

### Days 8–10 — Library Management System Project

**Day 8 (2 hours) — Design on paper**
- [ ] Sketch classes: `Book`, `Member`, `Library`
- [ ] Define attributes for each class
- [ ] Define methods for each class
- [ ] Draw interactions between classes
- [ ] Commit design notes to repo as `week2-oop/design.md`

**Day 9 (3 hours) — Build core classes**
- [ ] `Book` class with `__str__`, `__repr__`, `__eq__`
- [ ] `Member` class with properties
- [ ] `Library` class with collection management methods
- [ ] Commit progress

**Day 10 (3 hours) — Persistence + CLI**
- [ ] Save/load entire library state to JSON
- [ ] Menu-based CLI for user interaction
- [ ] Error handling for edge cases (borrow already-borrowed book, etc.)
- [ ] Write README
- [ ] Push to GitHub

### Week 2 SQL (spread across the week)
- [ ] 5 DataLemur problems (include first Medium)
- [ ] Read Mode Analytics SQL Tutorial — "Joins" chapter
- [ ] Focus topic: **INNER JOIN, LEFT JOIN** (THE most-tested SQL concept)

### End of Week 2 — Self Check
- [ ] Can I explain the difference between a class and an instance?
- [ ] Can I write a class with `__init__`, `__str__`, and `@property` from scratch?
- [ ] Do I know when inheritance is appropriate vs. composition?
- [ ] Can I write INNER JOIN and LEFT JOIN on paper?

---

## Week 3 — Advanced Python (Days 11–17)

**This week turns "I know Python" into "I'm good at Python."**

### Days 11–12 — Decorators

**Day 11 (1.5 hours):**
- [ ] Corey Schafer: "Python Tutorial — Decorators" (watch twice)

**Day 12 (1.5 hours):**
- [ ] Real Python: "Primer on Python Decorators"
- [ ] Build:
  - [ ] `@timer` — prints function execution time
  - [ ] `@retry(max_attempts=3)` — retries on exception
  - [ ] `@log_calls` — logs function name and arguments

### Days 13–14 — Generators

**Day 13 (1.5 hours):**
- [ ] Corey Schafer: "Python Tutorial — Generators"
- [ ] Understand memory efficiency argument

**Day 14 (1.5 hours):**
- [ ] Real Python: "How to Use Generators and yield in Python"
- [ ] Build:
  - [ ] Generator reading large file line-by-line
  - [ ] Generator yielding Fibonacci up to N
  - [ ] Generator expression filtering even numbers

### Day 15 — Context Managers + Logging (2 hours)
- [ ] Real Python: "Context Managers and Python's `with` Statement"
- [ ] Python docs: `logging` — "Logging HOWTO"
- [ ] Build:
  - [ ] Class-based context manager (`__enter__`, `__exit__`)
  - [ ] Function-based with `@contextmanager`
  - [ ] Script using `logging.getLogger()` with levels and formatting

### Days 16–17 — Web Scraper Project

**Day 16 (3 hours) — Basic scrape**
- [ ] `pip install requests beautifulsoup4 lxml`
- [ ] `pip freeze > requirements.txt`
- [ ] Target: quotes.toscrape.com
- [ ] Scrape quotes, authors, tags from page 1
- [ ] Parse into list of dicts

**Day 17 (3 hours) — Add robustness**
- [ ] Follow pagination to scrape all pages
- [ ] Apply `@retry(max_attempts=3)` decorator
- [ ] Replace `print` with `logging` module
- [ ] Save to both JSON and CSV
- [ ] Write README
- [ ] Push to GitHub

### Week 3 SQL
- [ ] 5 DataLemur problems
- [ ] Focus: **Subqueries, CTEs (`WITH` clause), GROUP BY + HAVING**
- [ ] Watch: YouTube "SQL Window Functions" tutorial (20 min)

### End of Week 3 — Self Check
- [ ] Can I explain what a decorator does to a non-technical friend?
- [ ] Can I write a generator that yields even numbers up to N?
- [ ] Do I understand why `yield` is memory-efficient?
- [ ] Can I write a subquery filtering on an aggregate?

---

## Week 4 — Testing, Packaging, Capstone (Days 18–30)

### Day 18 (2 hours) — Intro to Testing
- [ ] Corey Schafer: "Python Tutorial — Unit Testing" (skim)
- [ ] Real Python: "Getting Started With Testing in Python"
- [ ] `pip install pytest`

### Day 19 (2 hours) — Practical Testing
- [ ] Write pytest tests for Expense Tracker functions
- [ ] Put in `tests/test_expense_tracker.py`
- [ ] Learn: `assert`, parametrize, fixtures (basic)
- [ ] Run with `pytest -v`

### Days 20–21 — Proper Packaging
- [ ] Understand why `__init__.py` files exist
- [ ] Learn `requirements.txt` basics
- [ ] Understand relative vs absolute imports
- [ ] Restructure Library project as proper package:
  ```
  library_system/
  ├── library_system/
  │   ├── __init__.py
  │   ├── book.py
  │   ├── member.py
  │   ├── library.py
  │   └── cli.py
  ├── tests/
  │   ├── __init__.py
  │   └── test_library.py
  ├── main.py
  ├── requirements.txt
  └── README.md
  ```

### Days 22–24 — Design the Capstone

**Capstone: Personal Finance Dashboard (CLI)**

Uses everything from Month 1:
- CLI with multiple commands (`add`, `view`, `summary`, `export`)
- OOP: `Transaction`, `Category`, `Account`, `Dashboard`
- File I/O with JSON persistence
- At least one generator (streaming transactions)
- At least one custom decorator (`@log_action`)
- Custom context manager for file ops
- Error handling throughout
- Type hints everywhere
- Proper package structure with `__init__.py`
- `requirements.txt`
- Comprehensive README

**Day 22 (2 hours)** — Plan on paper
- [ ] Sketch classes and relationships
- [ ] Plan module structure
- [ ] List tests to write

**Day 23 (3 hours)** — Scaffold
- [ ] Create all folders and empty files with docstrings
- [ ] Write README *first* (README-driven development)

**Day 24 (3 hours)** — Start implementing

### Days 25–30 — Build and Ship

**Days 25–28** — Heads-down build
- [ ] Implement core Transaction/Category/Account classes
- [ ] Implement Dashboard with summary methods
- [ ] Add CLI menu loop
- [ ] Add decorator for action logging
- [ ] Add context manager for file ops
- [ ] Write pytest tests for 3+ key functions

**Day 29 (5 hours)** — Major push
- [ ] Get core features working end-to-end
- [ ] Focus on MAKING IT WORK, then cleanup

**Day 30 (4 hours)** — Polish and ship
- [ ] Final polish
- [ ] Write comprehensive README
- [ ] Push to GitHub
- [ ] Review and reflect on Month 1

### Week 4 SQL
- [ ] 15 DataLemur problems (catch up to 40 total if behind)
- [ ] **Window functions** deep dive: `ROW_NUMBER`, `RANK`, `LAG`, `LEAD`, `SUM() OVER`
- [ ] Should be solving Medium problems comfortably by end

---

## SQL Progression Tracker

**Target: 40 problems solved on DataLemur by end of Month 1**

| Week | Target | Solved | Topics |
|---|---|---|---|
| Week 1 | 5 Easy | ___ | SELECT, WHERE, GROUP BY, basic aggregates |
| Week 2 | 10 (mix Easy + first Medium) | ___ | INNER JOIN, LEFT JOIN |
| Week 3 | 10 Medium | ___ | Subqueries, CTEs, HAVING |
| Week 4 | 15 Medium+ | ___ | Window functions (ROW_NUMBER, RANK, LAG, LEAD, SUM OVER) |

---

## Resources Quick Reference

### Python Learning
- **YouTube:** Corey Schafer (youtube.com/@coreyms) — free, clearest Python tutorials
- **Course:** Harvard CS50P on edx.org — free, structured
- **Book:** "Python Crash Course" by Eric Matthes (€30, optional but excellent)
- **Practice:** Exercism.io Python track — free, mentor feedback
- **Reference:** realpython.com — high-quality free articles

### SQL Learning
- **Practice:** DataLemur — free, essential daily practice
- **Practice alternative:** StrataScratch — FAANG-flavored questions
- **Tutorial:** Mode Analytics SQL Tutorial (mode.com/sql-tutorial) — free
- **Book:** "SQL for Data Analysis" by Cathy Tanimura (optional)

### Documentation
- Python docs: docs.python.org/3/
- Python type hints: docs.python.org/3/library/typing.html

---

## Weekly Reflection Template

Fill in every Sunday evening:

### Week ___ Reflection
**Date:** _______________

**What I studied this week:**
-
-
-

**What I built this week (with GitHub link):**
-

**What clicked for me (new understanding):**
-

**What I'm still confused about (next week priority):**
-

**Applications sent this week:** ___

**Hours actually spent:** ___

**How I'm feeling:** (energized / steady / tired / stuck)

**Adjustment for next week:**
-

---

## Month 1 End Deliverables

By the end of Day 30, I should have:

### On GitHub
- [ ] 4 projects committed, all with proper READMEs:
  - [ ] Expense Tracker CLI
  - [ ] Library Management System
  - [ ] Web Scraper with retry logic
  - [ ] Personal Finance Dashboard (capstone)
- [ ] Green contribution squares showing consistency
- [ ] Type hints in every function across all projects
- [ ] pytest tests in at least 2 projects
- [ ] Proper package structure in at least 1 project

### Skills Mastered
- [ ] Can write clean Python with proper OOP
- [ ] Can write decorators from scratch
- [ ] Can write generators when appropriate
- [ ] Can write and understand context managers
- [ ] Can set up proper Python packages
- [ ] Can write basic pytest tests
- [ ] 40+ SQL problems solved on DataLemur
- [ ] Comfortable with JOINs, CTEs, subqueries, window functions

### Professional
- [ ] Applied to 20+ junior AI/ML/Data Engineer roles
- [ ] LinkedIn updated with Month 1 progress
- [ ] Weekly tracking document maintained
- [ ] Ready for Month 2 (Classical ML)

---

## Troubleshooting — When Things Get Hard

**If I fall behind:**
- Don't panic. Don't quit.
- Stretch Month 1 to 5 weeks instead of 4.
- Drop Exercism problems but keep project work and SQL.
- Talk to Claude about adjustments.

**If I feel stuck:**
- Take a full day off. Rest is part of learning.
- Review what I already built — progress is often invisible when in the middle.
- Remember: 6 months is the real plan. 1 bad day isn't failure.

**If I feel like faking it with AI:**
- Pause. This is the exact moment where real learning happens.
- Use AI to *explain* the concept, not to write the code.
- If I skip this struggle, I lose the whole point of Month 1.

**If motivation drops:**
- Re-read the original conversation with Claude that started this.
- Look at my GitHub green squares.
- Remember: I have two fine-tuned transformer models. I'm not starting from zero.
- This plan is to *prove to myself* what I can already do.

---

## Notes Section

_Use this space for thoughts, wins, stuck points, and reflections throughout the month._
