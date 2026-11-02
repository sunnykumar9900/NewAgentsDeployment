from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .agents.job_agent import search_jobs

app = FastAPI(title="Naukri Job Research Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class JobSearchRequest(BaseModel):
    skills: str


@app.get("/")
def read_root():
    return {
        "message": "Naukri Job Research API is running.",
        "docs": "/docs",
        "job_search_endpoint": "POST /search-jobs",
    }


@app.post("/search-jobs")
def search_jobs_api(request: JobSearchRequest):
    result = search_jobs(request.skills)
    return {"result": result}