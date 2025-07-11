# pubmed_paper_fetcher/fetcher.py

import requests
import xml.etree.ElementTree as ET
from typing import List, Dict

def fetch_papers(query: str, retmax: int = 10) -> List[Dict]:
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    search_url = f"{base_url}esearch.fcgi"
    fetch_url = f"{base_url}efetch.fcgi"

    search_params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": retmax}
    search_response = requests.get(search_url, params=search_params)
    ids = search_response.json().get("esearchresult", {}).get("idlist", [])

    fetch_params = {"db": "pubmed", "id": ",".join(ids), "retmode": "xml"}
    fetch_response = requests.get(fetch_url, params=fetch_params)
    root = ET.fromstring(fetch_response.content)

    results = []
    for article in root.findall(".//PubmedArticle"):
        title = article.findtext(".//ArticleTitle", "")
        pmid = article.findtext(".//PMID", "")
        date = article.findtext(".//PubDate/Year", "Unknown")
        authors, affiliations, email = [], [], ""

        for author in article.findall(".//Author"):
            name = f"{author.findtext('ForeName', '')} {author.findtext('LastName', '')}".strip()
            if name: authors.append(name)
            for aff in author.findall(".//AffiliationInfo/Affiliation"):
                aff_text = aff.text or ""
                affiliations.append(aff_text)
                if "@" in aff_text and not email:
                    email = aff_text

        results.append({
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": date,
            "Authors": authors,
            "Affiliations": affiliations,
            "Corresponding Email": email,
        })
    return results
