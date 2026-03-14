# Fighter jet hanger 

class FighterJet:
    def __init__(self, name, variant, role, payload):
        self.name = name
        self.role = role
        self.variant = variant
        self.payload = payload

    # Fighter jet informantion display function
    def display_info(self):
        print(f"Aircraft: {self.name}")
        print(f"Role: {self.role}")
        print(f"Variant: {self.variant}")
        print(f"Payload: {self.payload}")

# List of Fighter jets in the hanger / Objects

# ---------------- F-15 Variants ---------------- 
F15A = FighterJet(
    "F-15 Eagle",
    "A",
    "Air Superiority Fighter",
    ["AIM-7 Sparrow", "M61 Vulcan"]
)

F15B = FighterJet(
    "F-15 Eagle",
    "B",
    "Trainer / Air Superiority",
    ["AIM-7 Sparrow", "M61 Vulcan"]
)

F15C= FighterJet(
    "F-15 Eagle",
    "C",
    "Air Superiority Fighter",
    ["AIM-120 AMRAAM", "AIM-9 Sidewinder", "M61 Vulcan"]
)

F15D = FighterJet(
    "F-15 Eagle",
    "D",
    "Trainer / Air Superiority",
    ["AIM-120 AMRAAM", "AIM-9 Sidewinder", "M61 Vulcan"]
)   

F15E = FighterJet(
    "F-15 Eagle",
    "E Strike Eagle",
    "Strike Fighter / Multirole",
    ["AIM-120 AMRAAM", "JDAM Bomb", "AGM-65 Maverick", "M61 Vulcan"]
)

F15EX = FighterJet(
    "F-15 Eagle", 
    "EX Eagle II",
    "Modern Air Superiority / Multirole",
    ["AIM-120 AMRAAM", "AIM-9X Sidewinder", "JDAM Bomb", "AGM-65 Maverick", "M61 Vulcan"]
)

# ---------------- F-16 Variants ----------------
F16A = FighterJet(
    "F-16 Fighting Falcon", 
    "A", 
    "Multirole Fighter",
    ["AIM-9 Sidewinder", "M61 Vulcan"]
)
F16B = FighterJet(
    "F-16 Fighting Falcon", 
    "B", 
    "Trainer / Multirole",
    ["AIM-9 Sidewinder", "M61 Vulcan"]
)
F16C = FighterJet(
    "F-16 Fighting Falcon", 
    "C", 
    "Improved Multirole",
    ["AIM-120 AMRAAM", "AIM-9 Sidewinder", "M61 Vulcan", "GBU-12/31 JDAM"]
)
F16D = FighterJet(
    "F-16 Fighting Falcon", 
    "D", 
    "Trainer / Improved Multirole",
    ["AIM-120 AMRAAM", "AIM-9 Sidewinder", "M61 Vulcan", "GBU-12/31 JDAM"]
)
F16V = FighterJet(
    "F-16 Fighting Falcon", 
    "V Viper", 
    "Modern Multirole",
    ["AIM-120 AMRAAM", "AIM-9X Sidewinder", "M61 Vulcan", "JDAM Bomb"]
)

# ---------------- F/A-18 Variants ----------------
FA18A = FighterJet(
    "F/A-18 Hornet", 
    "A", 
    "Carrier Multirole / Strike Fighter",
    ["AIM-120 AMRAAM", "AIM-9 Sidewinder", "GBU-12 JDAM", "AGM-84 Harpoon"]
)
FA18B = FighterJet(
    "F/A-18 Hornet", 
    "B", 
    "Trainer / Multirole",
    ["AIM-120 AMRAAM", "AIM-9 Sidewinder", "GBU-12 JDAM", "AGM-84 Harpoon"]
)
FA18C = FighterJet(
    "F/A-18 Hornet", 
    "C", 
    "Improved Multirole",
    ["AIM-120 AMRAAM", "AIM-9 Sidewinder", "GBU-12 JDAM", "AGM-84 Harpoon"]
)
FA18D = FighterJet(
    "F/A-18 Hornet", 
    "D", 
    "Trainer / Multirole",
    ["AIM-120 AMRAAM", "AIM-9 Sidewinder", "GBU-12 JDAM", "AGM-84 Harpoon"]
)
FA18E = FighterJet(
    "F/A-18 Super Hornet", 
    "E", 
    "Advanced Multirole / Strike Fighter",
    ["AIM-120 AMRAAM", "AIM-9X Sidewinder", "GBU-31 JDAM", "AGM-84 Harpoon"]
)
FA18F = FighterJet(
    "F/A-18 Super Hornet", 
    "F", 
    "Two-seat Multirole / Strike Fighter",
    ["AIM-120 AMRAAM", "AIM-9X Sidewinder", "GBU-31 JDAM", "AGM-84 Harpoon"]
)

# ---------------- E/A-18 Variants ----------------
EA18G = FighterJet(
    "EA-18G Growler",
    "G",
    "Electronic Warfare / Jamming",
    ["ALQ-99 Jamming Pods", "AIM-120 AMRAAM", "AIM-9 Sidewinder"]
)

# ---------------- F-22 Variants ----------------
F22A = FighterJet(
    "F-22 Raptor", 
    "A", 
    "Air Superiority / Dogfight / Stealth",
    ["AIM-120 AMRAAM", "AIM-9 Sidewinder", "Internal small bombs"]
)

# ---------------- F-35 Variants ----------------
F35A = FighterJet(
    "F-35 Lightning II", 
    "A", 
    "Stealth Multirole / Strike Fighter",
    ["AIM-120 AMRAAM", "AIM-9 Sidewinder", "GBU-12/31 JDAM", "SDB Bomb"]
)
F35B = FighterJet(
    "F-35 Lightning II", 
    "B STOVL", 
    "Short Takeoff / Vertical Landing",
    ["AIM-120 AMRAAM", "AIM-9 Sidewinder", "GBU-12/31 JDAM", "SDB Bomb"]
)
F35C = FighterJet(
    "F-35 Lightning II", 
    "C Carrier", 
    "Carrier-based Strike Fighter",
    ["AIM-120 AMRAAM", "AIM-9 Sidewinder", "GBU-12/31 JDAM", "SDB Bomb"]
)

# ---------------- Hangar Dictionary ----------------
# All variant of fighter jets
hangar = {
    "F15A": F15A, "F15B": F15B, "F15C": F15C, "F15D": F15D, "F15E": F15E, "F15EX": F15EX,
    "F16A": F16A, "F16B": F16B, "F16C": F16C, "F16D": F16D, "F16V": F16V,
    "FA18A": FA18A, "FA18B": FA18B, "FA18C": FA18C, "FA18D": FA18D, "FA18E": FA18E, "FA18F": FA18F,
    "EA18G": EA18G,
    "F22A": F22A,
    "F35A": F35A, "F35B": F35B, "F35C": F35C
}

def main():

    while True:
        print("\nAvailable Fighter Jets (must include variant):")

        # Call jets in hanger / Display fleet
        for key in hangar:
            print(key)

        choice = input("\nSelect aircraft: ").strip().upper()
        
        if choice in hangar:
            print("\nAircraft Information:")
            hangar[choice].display_info()
            break

        else:
            print("Aircraft not found.")

if __name__ == "__main__":
    main()
