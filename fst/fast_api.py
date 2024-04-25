from fastapi import FastAPI
app=FastAPI()
richest_people_list={
    "Elon MUSK":"280 BILLION DOLLARS",
    "JEFF":"250 BILLION DOLLAR",
    "BILL":"190 BILLION DOLLAR",
    "MARK":"150 BILLION DOLLAR"
}

@app.get("/richest-people")
def richest_people():
    return richest_people_list
