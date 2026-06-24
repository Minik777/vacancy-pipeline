from sqlalchemy import select, func, text

from db.models import Vacancy, Company, Tag, Vacancy_tag

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
    statement = text("""
                     SELECT id, salary_from 
                     FROM vacancies
                     WHERE salary_from IS NOT NULL
                     ORDER BY salary_from DESC
                     LIMIT 1
                     """)
    result = session.execute(statement).first()
    return result

def min_salary(session):
    statement = text("""
                     SELECT id, salary_from
                     FROM vacancies
                     WHERE salary_from IS NOT NULL
                     ORDER BY salary_from ASC 
                     LIMIT 1
                     """)
    result = session.execute(statement).first()
    return result

def count_all_vacancies(session):
    statement = text("""
        SELECT count(*)
        from vacancies
        """)
    result = session.scalar(statement)
    return result

def vacancy_city(session):
    statement = text("""
        SELECT city, count(*) 
        FROM vacancies
        GROUP BY city
        """)
    result = session.execute(statement).all()
    return result

def top_salary_from(session):
    statement = text("""
        SELECT id, salary_from 
        FROM vacancies
        ORDER BY salary_from DESC
        LIMIT 1""")
        # (select(Vacancy.id, Vacancy.salary_from)
        #          .where(Vacancy.salary_from != None)
        #          .order_by(Vacancy.salary_from.desc())
        #          .limit(3)
        #          )
    result = session.execute(statement).all()
    return result

def top_tags(session):
    statement = text("""
        SELECT tags.name, count(vacancies_tags.tag_id) as vac_count FROM tags
        JOIN vacancies_tags
            ON tags.id = vacancies_tags.tag_id
        GROUP BY tags.id, tags.name
        ORDER BY vac_count DESC
        LIMIT 1
        """)
    result = session.execute(statement).first()

    return result
