from fastapi import APIRouter
from app.game.game import run_poker_round

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Poker backend is live 🎲"}

@router.post("/play")
def play():
    result = run_poker_round()
    return {"result": result}
