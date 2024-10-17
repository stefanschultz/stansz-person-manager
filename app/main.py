from fastapi import FastAPI, Depends, Request, Form
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import models
import crud
from database import engine, get_db
from starlette.responses import HTMLResponse

models.Base.metadata.create_all(bind=engine)

application = FastAPI()

templates = Jinja2Templates(directory="templates")

@application.get("/", response_class=HTMLResponse)
def read_people(request: Request, db: Session = Depends(get_db)) -> templates.TemplateResponse:
    people = crud.get_people(db)
    return templates.TemplateResponse("index.html", {"request": request, "people": people})

@application.get("/add_person", response_class=HTMLResponse)
def add_person_form(request: Request) -> templates.TemplateResponse:
    return templates.TemplateResponse("add_person.html", {"request": request})

@application.post("/add_person")
def create_person(first_name: str = Form(...), last_name: str = Form(...), db: Session = Depends(get_db)) -> RedirectResponse:
    crud.create_person(db, first_name, last_name)
    return RedirectResponse("/", status_code=303)

@application.get("/delete_person/{person_id}")
def delete_person(person_id: int, db: Session = Depends(get_db)) -> RedirectResponse:
    crud.delete_person(db, person_id)
    return RedirectResponse("/", status_code=303)
