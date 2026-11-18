from fastapi import FastAPI , HTTPException
from pydantic import BaseModel , Field

from fastapi.middleware.cors import CORSMiddleware


class Student(BaseModel):
    id : int
    name : str
    age : int =Field(gt=0)
    grade : float = Field (ge = 0 , le = 100)
    

class update_student(BaseModel):
    name : str
    age : int =Field(gt=0)
    grade : float = Field (ge = 0 , le = 100)
    



app = FastAPI()


app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],  # يسمح بالوصول من أي مصدر. قم بتقييد هذا في الإنتاج
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

school = [
    
]


@app.get("/")
def root():
    return "Welcome Ths our school"

@app.get("/students")
def show_students():
    if school == []:
        return "Its Empty"
    return school

@app.get("/students/{id}")
def search(id : int):
    for i , st in enumerate (school):
        if st.id == id:
            return school[i]
    raise HTTPException(status_code=404 , detail="There is not found")

@app.post("/students")  
def add_student(new_st : Student):
    for i , st in enumerate (school):
        if st.id == new_st.id:
            raise HTTPException(status_code=409 , detail="This student with this id")
    school.append(new_st)
    return new_st


@app.delete("/students/{id}")
def dl_st(id : int):
    for i , st in enumerate (school):
        if st.id == id:
            del school[i]
            return "done"    
    raise HTTPException (status_code = 404 , detail="There is no student with this id")
        
        
@app.put("/students/{id}")   
def edit_st(id : int , new_stu : update_student):
    for i , st in enumerate (school):
        if st.id == id:
            
            updated = Student(
                id = id,
                name = new_stu.name,
                age = new_stu.age,
                grade = new_stu.grade
            )
            school[i] = updated
            return new_stu
    raise HTTPException (status_code = 404 , detail="There is no student with this id")
    
        
        
        
