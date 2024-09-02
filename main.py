from typing import Union

from fastapi import FastAPI , File, UploadFile

app = FastAPI()
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from  app.database import engine , Base

import pandas as pd

import app.models as models
import time
# models.Base.metadata,create_all(engine)
models.Base.metadata.create_all(bind=engine)
import time
from app.database import SessionLocal, engine
from app.schema import UserSchema
from app.utils import create_docx_in_memory
from fastapi.responses import StreamingResponse

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





from typing import List

# @app.get("/")
# def read_root(user:UserSchema,db:Session = Depends(get_db)):
#     models.User.all()    
#     return {"Hello": "World"}


@app.get("/", response_model=List[UserSchema])
def read_root(db: Session = Depends(get_db)):
    users = db.query(models.User).all()  # Adjust based on your ORM setup
    return users






@app.post('/download')
def download_docx():
    text = "This is the text that will be converted into a DOCX file."
    
    # Create the DOCX in memory
    docx_stream = create_docx_in_memory(text)
    response = StreamingResponse(
        docx_stream, 
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    
    response.headers["Content-Disposition"] = "attachment; filename=downloaded_file.docx"
    return response
    
   



# @app.post("/create-user")
# def create_user(user:UserSchema,db:Session = Depends(get_db)):
#     file_path = "10.xlsx"
#     df = pd.read_excel(file_path)
#     for index, row in df.iterrows():
#         email = df.iloc[index]['email']  # Assuming 'email' is the column name
#         phone = df.iloc[index]['phone']  # Assuming 'phone' is the column name
#         password = df.iloc[index]['password']
#         print(f"the mail is {email}")
#         print(f"the mail is {str(phone)}")
#         print(f"the mail is {str(password)} numer")
#         records = models.User(email = email , phone=phone,hashed_password=password)
#         db.add(records)
#     db.commit()
#     db.reset()
#     db.refresh(records)


#     return  True


#17sec 
# @app.post("/create-user")
# def create_user(user: UserSchema, db: Session = Depends(get_db)):
#     start_time = time.time()
#     file_path = "zz.xlsx"
#     df = pd.read_excel(file_path)
#     try:
#         for index, row in df.iterrows():
#             email = row['email']
#             print(email)
#             phone = row['phone']
#             password = row['password']
#             exiting_email = db.query(models.User).filter(models.User.email==email).first()
#             if exiting_email:
#                 pass
#             else:
#                 # Create the User record and add it to the session
#                 record = models.User(email=email, phone=phone, hashed_password=password)
#                 db.add(record)

#         # Commit all changes at once after all records are added
#         db.commit()
#         end_time = time.time()
#         total_time = end_time - start_time
#         print("++++++++++++++++++++++++",total_time)
#         return {"message": "Users created successfully."}

#     except Exception as e:
#         db.rollback()
#         return {"message": f"{e}."}

#         # (status_code=500, det
#         # ail=str(e))
#     finally:
#         db.close()

#around 17 sec





#using bulk create 

@app.post("/create-user")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    start_time = time.time()
    file_path = "10.xlsx"
    df = pd.read_excel(file_path)
    try:
        user_data = []
        for index, row in df.iterrows():
            email = row['email']
            print(email)
            phone = row['phone']
            password = row['password']
            record = models.User(email=email, phone=phone, hashed_password=password)
            user_data.append(record)
            
        db.bulk_save_objects(user_data)
        # Commit all changes at once after all records are added
        db.commit()
        end_time = time.time()
        total_time = end_time - start_time
        print("++++++++++++++++++++++++",total_time)
        return {"message": "Users created successfully."}

    except Exception as e:
        db.rollback()
        return {"message": f"{e}."}

        # (status_code=500, det
        # ail=str(e))
    finally:
        db.close()

