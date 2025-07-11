
---

##  `README.md`

````markdown
#  PubMed Paper Fetcher

A Python command-line tool to search **PubMed** for research papers based on a user-specified query and identify those that include **at least one non-academic author** affiliated with **biotech or pharmaceutical companies**.

Built using [Typer](https://typer.tiangolo.com/), [Requests](https://requests.readthedocs.io/), [Pandas](https://pandas.pydata.org/), and [LXML](https://lxml.de/).

---

##  Features

-  Fetch PubMed papers using official APIs
-  Heuristically detect non-academic authors
-  Output structured CSV files
-  CLI with helpful options (`--file`, `--debug`)
-  Poetry-powered dependency management

---

##  Installation

### Prerequisites

- Python ≥ 3.10
- [Poetry](https://python-poetry.org/docs/)

### Setup Steps

```bash
git clone https://github.com/your-username/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
poetry install
````

---

##  Usage

### Command:

```bash
poetry run get-papers-list "your search query" --file output.csv --debug
```

### Example:

```bash
poetry run get-papers-list "covid vaccine" --file results.csv --debug
```

---

##  Output CSV Format

| Column                       | Description                                         |
| ---------------------------- | --------------------------------------------------- |
| `PubmedID`                   | PubMed paper ID                                     |
| `Title`                      | Title of the research paper                         |
| `Publication Date`           | Year of publication                                 |
| `Non-academic Author(s)`     | Author(s) affiliated with non-academic institutions |
| `Company Affiliation(s)`     | Detected non-academic affiliations                  |
| `Corresponding Author Email` | Contact email (if available)                        |

---

##  Non-Academic Detection Logic

Affiliations **not containing** words like:

* `university`, `institute`, `college`, `hospital`, `school`, `lab`

are considered **non-academic**.

Examples of matches:

* `XYZ Biotech Inc.`
* `ABC Pharmaceuticals Ltd.`

---

##  Project Structure

```
pubmed_paper_fetcher/
├── __init__.py
├── cli.py            # Typer CLI command
├── fetcher.py        # API and XML parsing logic
├── filters.py        # Affiliation analysis logic
├── exporter.py       # CSV writing logic
```

---

##  Technologies Used

| Tool     | Purpose                      |
| -------- | ---------------------------- |
| Python   | Programming Language         |
| Poetry   | Dependency & project manager |
| Typer    | CLI framework                |
| Pandas   | DataFrame & CSV operations   |
| Requests | PubMed API calls             |
| LXML     | XML parsing                  |
| ChatGPT  | Assisted in development      |

---


---

##  Author

**Dhanya **
 [dhanyapoojary2002@gmail.com](mailto:dhanyapoojary2002@gmail.com)
 MCA Student

---

