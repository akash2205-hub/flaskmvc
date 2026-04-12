from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from . import router, api_router   # 👈 IMPORTANT

# Page route (HTML)
@router.get("/todos", response_class=HTMLResponse)
def todos_page(request: Request):
    return request.app.state.templates.TemplateResponse(
        "todos.html",
        {"request": request}
    )


# API route (JSON)
@api_router.get("/todos")
def get_todos():
    return [
        {"id": 1, "title": "Finish assignment", "description": "Do FastAPI work"},
        {"id": 2, "title": "Study", "description": "Prepare for exam"}
    ]