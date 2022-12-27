from fastapi import FastAPI
from . import models
from .db import engine
from .routers import post, user, auth, votes
from .config import Settings
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind = engine)

app = FastAPI()
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# while True:
    
#     try:
#         conn = psycopg2.connect(host ='localhost', database='fastapi', user='postgres', password='passlead', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("DB Connected Successfully")
#         break
#     except Exception as error:
#         print("DB Connection Failed")
#         print("Error:", error)
#         time.sleep(2)
        

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)


@app.get("/")
async def root():
    return {"message": "Hello World !"}




    
    
        
    
    