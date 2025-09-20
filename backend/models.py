from sqlmodel import SQLModel, Field

class Job(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str

class ResumeEval(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    resume_name: str
    job_id: int
    score: int
    verdict: str
