from db.database import Base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Float, DateTime, ForeignKey

from datetime import datetime

class Company(Base):
    __tablename__ = 'companies'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
# пока без relationship в трёх таблицах
class Tag(Base):
    __tablename__ = "tags"

    vacancies = relationship(
        "Vacancy",
        secondary="vacancies_tags",
        back_populates="tags"
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

class Vacancy(Base):
    __tablename__ = "vacancies"

    id: Mapped[int] = mapped_column(primary_key=True)
    hh_id: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str] = mapped_column(String(255), nullable=True)
    salary_from: Mapped[float] = mapped_column(Float(), nullable=True)
    salary_to: Mapped[float] = mapped_column(Float(), nullable=True)
    currency: Mapped[str] = mapped_column(String(255), nullable=True)
    url: Mapped[str] = mapped_column(String(255), nullable=True)
    published: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False, default=datetime.utcnow)
    company_id: Mapped[int] = mapped_column(ForeignKey(Company.id), nullable=False)

    tags = relationship(
            "Tag",
            secondary="vacancies_tags",
            back_populates="vacancies"
        )
class Vacancy_tag(Base):
    __tablename__ = "vacancies_tags"
    vacancy_id: Mapped[int] = mapped_column(ForeignKey("vacancies.id"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"), primary_key=True)
