from db.database import init_db
from etl.extract import get_posts
from etl.transform import transform_vacancy
from db.database import Session
from etl.load import save_vacancy
from analytics.queries import (average_salary, vacancy_count_by_company,
                               max_salary, min_salary, count_all_vacancies,
                               vacancy_city, top_salary_from)

if __name__ == '__main__':
    init_db()
    print("БД создана!")
    vacancies = get_posts("python", 5)
    with Session() as session:
         for raw in vacancies:
             clean = transform_vacancy(raw)
             print(clean.get("title"))
             print(clean.get("tags"))
             save_vacancy(session, clean)
         session.commit()

         avg_salary = average_salary(session)
         print("Средняя salary_from:", avg_salary)

         rows = vacancy_count_by_company(session)
         for company_name, vacancy_count in rows:
             print(company_name, vacancy_count)
         # max_salary = max_salary(session)
         # vacancy_id, salary = max_salary
         # print(vacancy_id, salary)
         #
         # min_salary = min_salary(session)
         # vacancy_id, salary = min_salary
         # print(vacancy_id, salary)
         #
         # all_vac = count_all_vacancies(session)
         # print(all_vac)
         #
         # vacancy_city = vacancy_city(session)
         # for city, vacancies in vacancy_city:
         #     print(city, vacancies)
         #
         # top_salary_from = top_salary_from(session)
         # for vacancy_id, salary in top_salary_from:
         #     print(vacancy_id, salary)


