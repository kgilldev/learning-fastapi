from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Car(BaseModel):
    make: str
    model: str
    year: int
    color: str
    cats: bool
    price: float


@app.get('/')
def root():
    return {"Hello" : "World"}

cars = []

@app.post("/cars")
def list_car(car: Car):
    cars.append(car)
    return cars

@app.get("/cars/{car_id}", response_model=Car)
def get_car(car_id: int) -> Car:
    if car_id >= len(cars):
        raise HTTPException(status_code=404, detail=f"car_id {car_id} larger than length of cars")
    car = cars[car_id]
    return car

@app.get('/cars', response_model=List[Car])
def list_cars(limit: int = 10) -> List[Car]:
    if limit > len(cars):
        return cars
    return cars[:limit]

@app.delete('/cars/{car_id}')
def delete_car(car_id: int) -> Car:
    if car_id >= len(cars):
        raise HTTPException(status_code=404, detail=f"car_id {car_id} larger than length of cars")
    print(f"Deleting car {cars[car_id]}")
    poppedCar = cars.pop(car_id)
    return poppedCar
