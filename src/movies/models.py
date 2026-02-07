from sqlalchemy import Column, Integer, String
from pydentic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase



class Base(DeclarativeBase):
    pass


class Movie(Base):
    """
    Модель для таблицы "movies" в базе данных.
    """
    __tablename__ = "movies"

    id = Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name = Mapped[str] = mapped_column(String(255), nullable=False, index=True, unique=True, comment="Название фильма")
    genre = Mapped[str] = mapped_column(String(55), nullable=False, index=True, comment="Жанр фильма")
    year_of_release = Mapped[int] = mapped_column(Integer, nullable=False, index=True, comment="Год выпуска фильма")
    director = Mapped[str] = mapped_column(String(255), nullable=False, index=True, comment="Режиссер фильма")
    class MovieCreate(BaseModel):
        

