from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session
from db import  get_session
from .models import OTUrl
from . import crud

router  = APIRouter(
  prefix = "/oturl"
)

@router.get("/check_url/{security_token}")
def check_url(security_token: str, session:Session = Depends(get_session)):
  oturl_fromdb = crud.get_valid_by_sectoken(security_token, session)
  if not oturl_fromdb or oturl_fromdb.is_completed:
      raise HTTPException(status_code=404, detail="Invalid or expired URL or the survey was completed")
  return oturl_fromdb


@router.post('/new')
def create_oturl(ot_url: OTUrl, session:Session = Depends(get_session)):    
    # set the expiry date
    url_fromdb = crud.create_oturl(ot_url, session)
    return url_fromdb


@router.get('/{security_token}', response_model=OTUrl) #output serialiser
def read_oturl(security_token:str, session:Session = Depends(get_session)):
  url_fromdb = crud.read_oturl(security_token, session)
  if not url_fromdb:
      raise HTTPException(status_code=404,detail="URL not found")
  return url_fromdb


@router.delete('/{security_token}') #output serialiser
def delete_oturl(security_token:str, session:Session = Depends(get_session)):
  respoonse = crud.delete_oturl(security_token, session)
  return respoonse


# ADMIN
# @router.get('/all', response_model=list[OTUrl]) #output serialiser
# def read_oturls(session:Session = Depends(get_session)):
#   urls_fromdb = crud.read_oturls(session)
#   return urls_fromdb

# @router.patch('/oturls/{security_token}', response_model=OTUrl) #output serialiser
# def update_oturl(security_token:str, url:OTUrl, session:Session = Depends(get_session)):
#   oturl_fromdb = crud.update_oturl(security_token, url, session)
#   if not oturl_fromdb:
#       raise HTTPException(status_code=404,detail="URL not found")
  