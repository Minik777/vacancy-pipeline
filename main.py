from db.database import init_db
from etl.extract import get_posts
from etl.transform import transform_vacancy
from db.database import Session
from etl.load import save_vacancy
from analytics.queries import (average_salary, vacancy_count_by_company,
                               max_salary)
from config import DEFAULT_QUERY, DEFAULT_COUNT

if __name__ == '__main__':
    init_db()
    print("БД создана!")
    vacancies = get_posts(query=DEFAULT_QUERY, count=DEFAULT_COUNT)
    with Session() as session:
         for raw in vacancies:
             clean = transform_vacancy(raw)
             save_vacancy(session, clean)
         session.commit()

         avg_salary = average_salary(session)
         print("Средняя salary_from:", avg_salary)

         rows = vacancy_count_by_company(session)
         for company_name, vacancy_count in rows:
             print(company_name, vacancy_count)
         max_salary = max_salary(session)
         vacancy_id, salary = max_salary

