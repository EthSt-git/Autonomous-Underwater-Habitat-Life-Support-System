"""
Author: Ethan St. Louis
Project: Autonomous Underwater Habitat Digital Twin

TO DO:

O2 and CO2 conditions

Power

Telemetry

Go through and fix bugs
Tests
"""

class HabitatCtrlSys:
    #values for the habitat control system
    habitat_data = { 
"owner": "Ethan", "habitat_pressure": 1.00, "temperature": 22.5, "oxygen": 21, "carbonDioxide": 0.04
        }
#Constant values for the habitat control system
    # pressure thresholds in atmospheres (atm)
    internalPressure_target = 1.00
    low_pressure_threshold = 0.95
    high_pressure_threshold = 1.05

    # temperature thresholds in degrees Celsius (°C)
    low_temp_thres = 18
    high_temp_thres = 27
    target_temp = 22.5

    #Oxygen and Carbon Dioxide thresholds in percentage (%)
    
    def __init__(self, owner, habitat_pressure, temperature, oxygen, carbonDioxide):
        self.owner = owner;
        #air pressure inside habitat
        self.habitat_pressure = habitat_pressure
        #tempurature inside habitat
        self.temperature = temperature
        #O2 conc. in habitat
        self.oxygen = oxygen
        #CO2 conc. in Habitat
        self.carbonDioxide = carbonDioxide


    #Get the owner of the habitats Name
    def get_OwnerName(self):
        return self.owner
    
    #Get the air pressure inside habitat
    def get_habitat_pressure(self):
        return self.habitat_pressure
    
    #Get temperature inside habitat
    def get_temp(self):
        return self.temperature
    #Get O2 conc. in habitat
    def get_O2(self):
        return self.oxygen
    #Get CO2 conc. in Habitat
    def get_CO2(self):
        return self.carbonDioxide
    
    #Output / Acuator functions

    def vent(self, action):
        match action:
            case "IN-RANGE":
                print("Ventilation system is off.")
            case "LOW":
                print("Ventilation system is activated to increase pressure.")
            case "HIGH":
                print("Ventilation system is activated to decrease pressure.")

    def tempCtrl(self, action):
        match action:
            case "HEAT":
                print("Habitat Temperature to LOW, Heating System is ONLINE")
                print("Cooling System is OFFLINE")
            case "COOL":
                print("Habitat Temperature to HIGH, Cooling System is ONLINE")
                print("Heating System is OFFLINE")
            case "OFF":
                print("Habitat Temperature is Stable, Heating and Cooling Systems are OFFLINE")
        

    def CO2Control(self, action):
        print("CO2 Control System Activated")
    #life support code
    def lifeSupport(self):
        curr_pres = self.get_habitat_pressure()
        curr_temp = self.get_temp()
        curr_O2 = self.get_O2()
        curr_CO2 = self.get_CO2()
        
        if curr_pres > self.low_pressure_threshold and self.habitat_pressure < self.high_pressure_threshold:
            print("Internal pressure is within acceptable range. No action needed.")
            # Ventilation remains off
            self.vent("IN-RANGE")
        elif curr_pres <= self.low_pressure_threshold:
            print("Warning: Internal pressure is too low! Activating life support systems to increase pressure.")
            # Code to activate life support systems to increase pressure
            self.vent("LOW")
        elif curr_pres >= self.high_pressure_threshold:
            print("Warning: Internal pressure is too high! Activating life support systems to decrease pressure.")
            # Code to activate life support systems to decrease pressure
            self.vent("HIGH")


        if curr_temp > low_temp_thres and temperature < high_temp_thres:
            print("Temperature is Stable no heating and cooling systems are OFFLINE")
            self.tempCtrl("OFF")
        elif curr_temp >= high_temp_thres:
            print("Temperature is High; Turning Cooling Systems ONLINE")
            self.tempCtrl("COOL")
        elif curr_temp <= low_temp_thres:
            print("Temperature is Low; Turning Heating Systems ONLINE")
            self.tempCtrl("HEAT")



    

    
        
        
    
