from fastapi import FastAPI, Response, APIRouter, status, HTTPException, Depends
from .. import schemas, db, oauth2, models
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/vote",
    tags=['Vote']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def vote(vote: schemas.Vote, db: Session = Depends(db.get_db),
               current_user:int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id {id} does not exist")
        
    vote_query = db.query(models.Votes).filter(models.Votes.post_id == vote.post_id,
                                    models.Votes.user_id == current_user.id)
    vote_found = vote_query.first()
     
    if vote.dir == 1:
        if vote_found: 
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User {current_user.id} already liked this post")
    
        new_vote = models.Votes(post_id = vote.post_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "You Liked this Post "}
    else:
        if not vote_found:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()
        
        return{"message": "You Removed Your Like"}
        
        
    
    