
class Weather:

    temp: int
    unit: str
    description: str

    def __init__(self, temp: str, unit: str, description: str) -> None:
        self.temp = int(temp)
        self.unit = unit
        self.description = description

    
    def __str__(self):
        temp_type: str
        if self.temp >= 100 or self.temp < 25:
            temp_type = "bad"
        elif self.temp > 89:
            temp_type = "scorching"
        elif self.temp > 79:
            temp_type = "hot"
        elif self.temp > 74:
            temp_type = "warm"
        elif self.temp > 65:
            temp_type = "pleasant"
        elif self.temp > 59:
            temp_type = "brisk"
        elif self.temp > 54:
            temp_type = "nippy"
        elif self.temp > 49:
            temp_type = "chilly"
        elif self.temp > 39:
            temp_type = "cold"
        elif self.temp > 31:
            temp_type = "frigid"
        else:
            temp_type = "freezing"
        
        return f"the weather is {temp_type} and {self.description}"
        
