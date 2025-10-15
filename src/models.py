from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(80), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favorites: Mapped[list['FavoriteCharacters']] = relationship(back_populates='user')
    favorite_planets: Mapped[list['FavoritePlanets']] = relationship(back_populates='user')
    favorite_ships: Mapped[list['FavoriteShips']] = relationship(back_populates='user')

class Characters(db.Model):
    __tablename__ = 'characters'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    height: Mapped[int] = mapped_column(Integer)
    weight: Mapped[int] = mapped_column(Integer)
    favorite_by: Mapped[list['FavoriteCharacters']] = relationship(back_populates='character')

class FavoriteCharacters(db.Model):
    __tablename__ = 'favorite_characters'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='favorites')
    character_id: Mapped[int] = mapped_column(ForeignKey('characters.id'))
    character: Mapped['Characters'] = relationship(back_populates='favorite_by')

class Planet(db.Model):
    __tablename__ = 'planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    population: Mapped[int] = mapped_column(Integer, nullable=True)
    favorite_by: Mapped[list['FavoritePlanets']] = relationship(back_populates='planet')

class FavoritePlanets(db.Model):
    __tablename__ = 'favorite_planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id')) 
    user: Mapped['User'] = relationship(back_populates='favorite_planets')
    planet_id: Mapped[int] = mapped_column(ForeignKey('planets.id'))
    planet: Mapped['Planet'] = relationship(back_populates='favorite_by')

class Ship(db.Model):
    __tablename__ = 'ships'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    capacity: Mapped[int] = mapped_column(Integer, nullable=True) #capacidad, por poner algo y no dejar solo nombre e id 
    favorite_by: Mapped[list['FavoriteShips']] = relationship(back_populates='ship')

class FavoriteShips(db.Model):
    __tablename__ = 'favorite_ships'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))  
    user: Mapped['User'] = relationship(back_populates='favorite_ships')
    ship_id: Mapped[int] = mapped_column(ForeignKey('ships.id'))
    ship: Mapped['Ship'] = relationship(back_populates='favorite_by')
