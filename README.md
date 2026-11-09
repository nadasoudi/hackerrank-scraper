# HackerRank Problem Scraper

Logs in to HackerRank with Selenium and collects programming problems across five language tracks, saving each track to its own CSV.

## Output

| File | Track |
|---|---|
| `c_problems.csv` | C |
| `cpp_problems.csv` | C++ |
| `java_problems.csv` | Java |
| `python_problems_python.csv` | Python |
| `sql_problems.csv` | SQL |

## How it works

1. Logs in through HackerRank's login page, using explicit waits so it doesn't break on slow page loads
2. Switches between language tracks by clicking the filters on the page
3. Scrapes the problem listings and writes one CSV per track

## Setup

Credentials are read from environment variables and are never stored in the code:

```bash
export HACKERRANK_USERNAME=you@example.com
export HACKERRANK_PASSWORD=your_password
```

On Windows, use `setx HACKERRANK_USERNAME "..."` instead.

```bash
pip install selenium
python hackerrank_scraper.py      # or open code.ipynb
```

You need a ChromeDriver that matches your Chrome version.

## Tech stack

Python, Selenium (WebDriverWait, ActionChains), Jupyter
