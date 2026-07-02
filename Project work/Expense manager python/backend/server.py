from fastapi import FastAPI
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel
class Expense(BaseModel):
    amount: float
    category: str
    notes: str

app = FastAPI()
@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(str(expense_date))
    return expenses

@app.post("/expenses/{expense_date}")
def create_expense(expense_date: date,expense:List[Expense]):
    db.helper.delete_expense(str(expense_date))
    for expense in expense:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
    return {"message": "Expense created successfully"}