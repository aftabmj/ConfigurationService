
import logging
import uuid
import datetime
from sqlmodel import Session, select
from .models import OTUrl


def _delete_otu(oturl_fromdb, session:Session):
  oturl_fromdb.is_valid = False
  session.add(oturl_fromdb)
  session.commit()
  session.refresh(oturl_fromdb)
  return oturl_fromdb


def create_oturl(ot_url: OTUrl, session):
  # with Session(engine) as session:
    db_item = ot_url
    db_item.security_token = str(uuid.uuid4())  # Generating a unique URL
    now = datetime.datetime.now()
    db_item.created_date = now
    db_item.expiry_date = now + datetime.timedelta(days=3) 

    # staff = logged in staff
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


def read_oturl(url_id:str, session:Session):
  oturl_fromdb = session.get(OTUrl,url_id)
  if not oturl_fromdb:
    return None
  # if not oturl_fromdb:
  #     raise HTTPException(status_code=404,detail="One Time URL found")
  return oturl_fromdb


"""
  User clicks on their email with this url (which has the sec_code)
  The frontend app , call this function to get a full url if valid 
"""
def get_valid_by_sectoken(security_token:str, session:Session):
  statement = select(OTUrl)\
              .where(OTUrl.security_token == security_token)\
              .where(OTUrl.is_valid == True)

  results = session.exec(statement)

  oturl_fromdb = results.first()
  if oturl_fromdb and \
    (oturl_fromdb.is_completed or \
     oturl_fromdb.expiry_date <= datetime.datetime.now()) :
    
    logging.info("Token fetched an invalid URL, deactivating it.")

    _delete_otu(oturl_fromdb, session)
    return None

  return oturl_fromdb



def delete_oturl(security_token:str, session:Session):
  # oturl_fromdb = session.get(OTUrl, security_token)
  oturl_fromdb = get_valid_by_sectoken(security_token, session)
  if not oturl_fromdb:
     return None
  return _delete_otu(oturl_fromdb, session)

  # if not oturl_fromdb:
  #     raise HTTPException(status_code=404,detail="One Time URL not found")
  # session.delete(oturl_fromdb)
  # session.commit()
  # return {"deleted": True}


# ADMIN
# def read_oturls(session:Session):
#   # with Session(engine) as session:
#   oturls_fromdb = session.exec(select(OTUrl)).all()
#   return oturls_fromdb


# def update_oturl(url_id:int, url:OTUrl, session:Session):
#   oturl_fromdb = session.get(OTUrl, url_id)
#   if not oturl_fromdb:
#      return None
#       # raise HTTPException(status_code=404,detail="One Time URL found")
  
#   data = url.model_dump(exclude_unset=True) #partial update
#   for k, v in data.items():
#     setattr(oturl_fromdb, k, v)
#   session.add(oturl_fromdb)
#   session.commit()
#   session.refresh(oturl_fromdb)
#   return oturl_fromdb