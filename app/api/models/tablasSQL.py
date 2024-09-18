from sqlachemy import Column, Integer, String, Floart, Date, Foreingkey
from sqlalchemy import relationship
from sqlalchemy.ext.declarative import declarative_base

#llamando a la base para crear tablas
Base = declarative_base()


#derfinicion de las tablas de mi modelo

#usuario
class Usuario(Base):
    __tablename__='usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    fechaNacimiento=colum(Date)
    ubicacion=colum(String(100))
    metaAhorro=colm(colum(float))

class Gasto(Base):
    __tablename__='gastos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(100))
    categoria = Column(String(100))
    monto = Column(Float)
    fecha = Column(Date)

class Categoria(Base)
    __tablename__='categorias'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    descripcion = Column(String(100))
    icono = Column(String(100))
    color = Column(String(100))
    gastos = relationship('gasto', backref='categoria')


class ingreso(Base):
    __tablename__='ingresos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(100))
    categoria = Column(String(100))
    monto = Column(Float)
    fecha = Column(Date)

class datoNullPrueba(Base):
    pass
