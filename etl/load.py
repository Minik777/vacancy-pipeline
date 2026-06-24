from db.models import Vacancy, Company, Tag
from sqlalchemy import select
def get_or_create_company(session, company_name: str):
    statement = select(Company).where(Company.name == company_name)
    company = session.scalar(statement)
    if company:
        return company
    company = Company(name=company_name)
    session.add(company)
    session.flush()
    return company

def get_or_create_tag(session, tag_name):
    statement = select(Tag).where(Tag.name == tag_name)
    tag = session.scalar(statement)

    if tag:
        return tag

    tag = Tag(name=tag_name)
    session.add(tag)
    session.flush()

    return tag

def save_vacancy(session, clean: dict):
    company = get_or_create_company(
        session,
        clean["company_name"],
    )
    statement = select(Vacancy).where(Vacancy.hh_id == clean["hh_id"])
    vacancy = session.scalar(statement)
    if vacancy:
        return vacancy

    vacancy = Vacancy(
        hh_id=clean["hh_id"],
        title=clean["title"],
        city=clean["city"],
        salary_from=clean["salary_from"],
        currency=clean["currency"],
        url=clean["url"],
        published=clean["published"],
        company_id=company.id
    )
    session.add(vacancy)
    for tag_name in clean.get("tags", []):
        tag = get_or_create_tag(session, tag_name)
        vacancy.tags.append(tag)
    return vacancy








