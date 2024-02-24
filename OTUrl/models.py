from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field
# from sqlmodel.sql.sqltypes import GUID

class OTUrlBase(SQLModel):
  program:str  = Field()#index=True)
  assessment_type:str = Field()
  staff:str = Field(default="Test")
  slk:str = Field(min_length=14, max_length=14)#,default_factory="0011")
  created_date: datetime = Field(default=datetime.utcnow(), nullable=False)
  expiry_date:datetime = Field(title="Date/Time when the URL becomes invalid",
                                     )
  is_valid:bool = Field(default=True)
  is_completed:bool = Field(default=False)
  security_token:str = Field(default=None, index=True)
  # description:Optional[str]


class OTUrl(OTUrlBase, table=True):
  id:Optional[int] = Field(default=None, primary_key=True)


# {
#   "program": "string",
#   "assessment_type": "IA",
#   "staff": "Tim",
#   "slk": "ALLFT210719811"
# }


# class Program(BaseModel):
#     name: str = Field(index=True)
#     assessment_types: list[str]

# class AssessmentType(BaseModel):
#     name: str
#     questions: list[str]
#     prefill_questions: list[str]  # Optional: which questions can be pre-filled
#     survey_url: str  # URL to load the SurveyJS survey

# class Client(BaseModel):
#     slk: str
#     current_program: str

# class Configuration(BaseModel):
#     programs: list[Program]
#     clients: list[Client]
