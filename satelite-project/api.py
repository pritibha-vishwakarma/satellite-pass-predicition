from fastapi import FastAPI
from database import get_all_passes

#here i am creating a api app 
app = FastAPI()

#this is Home route
@app.get("/")
def home_page():
    return {"message": "Satellite Tracker API is running"}

@app.get("/all-passes")
def fetch_get_passes():
    records = get_all_passes()
 #get the all satellite passes
    pass_list = []  
    for item in records:
        pass_data= {
            "id": item[0],
            "satellite_name": item[1],
            "start_time": item[2],
            "end_time": item[3]
        }
        pass_list.append(pass_data)
    return pass_list