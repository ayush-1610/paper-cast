import arxiv
import os

def fetch_paper(query, max_results=1):
    """
    Fetch papers from arXiv based on a query.
    """
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    
    # Create data directory if it doesn't exist
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    os.makedirs(data_dir, exist_ok=True)
    
    papers = list(search.results())
    if papers:
        paper = papers[0]
        # Fix the path to use os.path for cross-platform compatibility
        filename = f"{paper.entry_id.split('/')[-1]}.pdf"
        paper.download_pdf(dirpath=data_dir)
        return os.path.join(data_dir, filename)
    return None
