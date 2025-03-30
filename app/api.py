from fastapi import APIRouter
from app.game.game import PokerGame
router = APIRouter()

@router.get("/")
def root():
    game = PokerGame()
    return {str(game.deal_initial_hand())}
