# pubmed_paper_fetcher/cli.py

import typer
from pubmed_paper_fetcher.fetcher import fetch_papers
from pubmed_paper_fetcher.filters import filter_non_academic_authors
from pubmed_paper_fetcher.exporter import export_to_csv
import logging

app = typer.Typer()

@app.command()
def run(
    query: str = typer.Argument(..., help="PubMed search query"),
    file: str = typer.Option(None, "--file", "-f", help="Output CSV filename"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug logging"),
):
    if debug:
        logging.basicConfig(level=logging.DEBUG)

    logging.info("Fetching papers for query: %s", query)
    papers = fetch_papers(query)
    logging.info("Fetched %d papers", len(papers))

    filtered = filter_non_academic_authors(papers)
    logging.info("Filtered down to %d papers with non-academic authors", len(filtered))

    if file:
        export_to_csv(filtered, file)
        typer.echo(f" Results saved to {file}")
    else:
        for paper in filtered:
            typer.echo(paper)

if __name__ == "__main__":
    app()
