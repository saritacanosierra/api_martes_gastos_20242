from sqlalchemy import create_engine,event
from sqlalchemy.orm import sessionmarker
from sqlalchemy. engine import engine

#datos para la conexion a BD

dataBaseName="gestordb"
userName="root"
userPassword=""
connectionPort=3306
server="localhost"

#creando la conexion
dataBaseConnection=f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{connectionPort}/{dataBaseName}"

#creo el motor de conexion
engine= create_engine(databaseconnecction)
sessionLocal=sessionmaker(autocommit=false,autoflush=false, bind=engine)
