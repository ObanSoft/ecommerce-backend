# FastAPI no necesita saber de los modelos para arrancar usa el base metadata para guardarlos y ejecutarlos en el import 


Model (User)
   ↓ import
DeclarativeBase
   ↓
Base.metadata 
   ↓
Alembic
   ↓
SQL ejecutado en PostgreSQL


🧱 Modelos → describen el dominio
📦 DeclarativeBase / MetaData → registran esas descripciones
🧭 Alembic → controla y ejecuta los cambios
🗄️ PostgreSQL → persiste la realidad
⚙️ FastAPI → solo orquesta lógica y requests


# Model User: Dominio de datos
# Model Auth: Dominio de seguridad 

Router → Service → Repository → DB

Router → Recibe la petición HTTP del cliente y devuelve la respuesta.
Service → Contiene la lógica del negocio y las reglas de validación. Decide qué hacer con los datos.
Repository → Se encarga de comunicarse con la base de datos, ejecutar queries y devolver resultados.
DB (Database) → Almacena los datos permanentemente y sirve como fuente.