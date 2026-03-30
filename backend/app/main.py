from fastapi import FastAPI
from pydantic import BaseModel


class DemoResponse(BaseModel):
    phase: str
    message: str
    implemented: list[str]
    next_step: str


app = FastAPI(
    title="LangChain Learning Path Backend",
    version="0.1.0",
    description="Minimal phase-2 placeholder API for backend experiments.",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "backend",
        "phase": "phase-2-placeholder",
    }


@app.get("/demo", response_model=DemoResponse)
def demo() -> DemoResponse:
    return DemoResponse(
        phase="phase-2-placeholder",
        message="Backend skeleton is ready for future LangChain experiments.",
        implemented=[
            "FastAPI app bootstrap",
            "health check route",
            "demo route",
        ],
        next_step="Add chapter-oriented runtime endpoints when interactive labs begin.",
    )
