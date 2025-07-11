# pubmed_paper_fetcher/filters.py

from typing import List, Dict

def is_non_academic(affil: str) -> bool:
    affil = affil.lower()
    academic_keywords = ["university", "college", "institute", "school", "hospital", "lab"]
    return not any(word in affil for word in academic_keywords)

def filter_non_academic_authors(papers: List[Dict]) -> List[Dict]:
    filtered = []
    for paper in papers:
        company_affils = [affil for affil in paper["Affiliations"] if is_non_academic(affil)]
        if company_affils:
            filtered.append({
                "PubmedID": paper["PubmedID"],
                "Title": paper["Title"],
                "Publication Date": paper["Publication Date"],
                "Non-academic Author(s)": ", ".join(paper["Authors"]),
                "Company Affiliation(s)": ", ".join(set(company_affils)),
                "Corresponding Author Email": paper["Corresponding Email"],
            })
    return filtered
