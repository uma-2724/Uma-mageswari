from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models import TaskRequest, APIResponse

from modules.qna import answer_question
from modules.explanation_module import explain_concept
from modules.quiz_module import generate_quiz
from modules.summary_module import summarize_text
from modules.learning_path import get_learning_recommendations


# ---------------------------------------------------------
# Project paths
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"


# ---------------------------------------------------------
# FastAPI application
# ---------------------------------------------------------

app = FastAPI(
    title="EduGenie - Google Gemini Powered Learning Assistant",
    version="1.0.0",
    description=(
        "AI-powered educational assistant for "
        "questions, explanations, quizzes, summaries, "
        "and personalized learning paths."
    ),
)


# ---------------------------------------------------------
# Static files
# ---------------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory=str(STATIC_DIR)),
    name="static"
)

templates = Jinja2Templates(
    directory=str(TEMPLATES_DIR)
)


# ---------------------------------------------------------
# Frontend
# ---------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html"
    )


# ---------------------------------------------------------
# Health check
# ---------------------------------------------------------

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "EduGenie"
    }


# ---------------------------------------------------------
# Q&A
# ---------------------------------------------------------

@app.post("/qa", response_model=APIResponse)
async def qa(payload: TaskRequest):
    try:
        result = answer_question(payload.text)

        return APIResponse(
            success=True,
            result=result
        )

    except Exception as e:
        return APIResponse(
            success=False,
            result=f"QA Error: {str(e)}"
        )


# ---------------------------------------------------------
# Explanation
# ---------------------------------------------------------

@app.post("/explain", response_model=APIResponse)
async def explain(payload: TaskRequest):

    result = explain_concept(payload.text)

    return APIResponse(
        success=True,
        result=result
    )


# ---------------------------------------------------------
# Quiz
# ---------------------------------------------------------

@app.post("/quiz", response_model=APIResponse)
async def quiz(payload: TaskRequest):

    result = generate_quiz(payload.text)

    return APIResponse(
        success=True,
        result=result
    )


# ---------------------------------------------------------
# Summary
# ---------------------------------------------------------

@app.post("/summarize", response_model=APIResponse)
async def summarize(payload: TaskRequest):

    result = summarize_text(payload.text)

    return APIResponse(
        success=True,
        result=result
    )


# ---------------------------------------------------------
# Learning Path
# ---------------------------------------------------------

@app.post(
    "/learn/recommendations",
    response_model=APIResponse
)
async def learning_recommendations(
    payload: TaskRequest
):

    result = get_learning_recommendations(
        payload.text
    )

    return APIResponse(
        success=True,
        result=result
    )