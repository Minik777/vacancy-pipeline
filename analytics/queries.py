from sqlalchemy import select, func

from db.models import Vacancy, Company

def average_salary(session):
    statement = select(func.avg(Vacancy.salary_from))

    result = session.scalar(statement)

    return result

def vacancy_count_by_company(session):
    statement = (
        select(
            Company.name,
            func.count(Vacancy.id)
        )
        .join(Vacancy, Vacancy.company_id == Company.id)
        .group_by(Company.id)
    )

    result = session.execute(statement).all()

    return result

def max_salary(session):
    statement = (select(Vacancy.id, func.max(Vacancy.salary_from))
                 .order_by(Vacancy.salary_from.desc())
                 .limit(1)
                 )
    result = session.execute(statement).all()
    return result

def min_salary(session):
    statement = (select(Vacancy.id, func.min(Vacancy.salary_from))
                 .order_by(Vacancy.salary_from.asc())
                 .limit(1)
                 )
    result = session.execute(statement).all()
    return result

def count_all_vacancies(session):
    statement = select(func.count(Vacancy.id))
    result = session.scalar(statement)
    return result

def vacancy_sity(session):
    statement = (select(Vacancy.city, func.count(Vacancy.id))
                 .group_by(Vacancy.city)
                 )
    result = session.execute(statement).all()
    return result

def top_salary_from(session):
    statement = (select(Vacancy.id, Vacancy.salary_from)
                 .where(Vacancy.salary_from != None)
                 .order_by(Vacancy.salary_from.desc())
                 .limit(3)
                 )
    result = session.execute(statement).all()
    return result