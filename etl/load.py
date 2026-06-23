from db.models import Vacancy, Company
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
    return vacancy






