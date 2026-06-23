from bs4 import BeautifulSoup
from datetime import datetime
def transform_vacancy(raw: dict) -> dict:
    published = datetime.fromisoformat(raw["pubDate"])
    description = BeautifulSoup(raw.get("jobDescription", ""), "html.parser").get_text()
    return {
        "hh_id": raw["id"],
        "title": raw["jobTitle"],
        "company_name": raw["companyName"],
        "city": raw.get("jobGeo"),
        "salary_from": raw.get("salaryMin"),
        "salary_to": raw.get("salaryMax"),
        "currency": raw.get("salaryCurrency"),
        "url": raw["url"],
        "published": published,
        "created_at": raw.get("published_at"),
        "description": description,
        "tags": raw.get("jobIndustry", [])
    #     "created_at" всегда будет None, потому что в raw его нет, и salary_to тоже
    }