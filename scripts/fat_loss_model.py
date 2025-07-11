

class FatLossModel:
    def __init__(self, fasting_hours_per_day, days, calorie_deficit_per_day, fasting_factor, weight):
        self.fasting_hours_per_day = fasting_hours_per_day
        self.days = days
        self.calorie_deficit_per_day = calorie_deficit_per_day
        self.fasting_factor = fasting_factor
        
        self.weight = weight

    def calculate_body_fat(self, weight, body_fat_pct):
        fat_mass = weight * (body_fat_pct / 100)
        lean_mass = weight - fat_mass
        return fat_mass, lean_mass

    def estimate_fat_loss(self):
        # Simple model based on your rule
        fasting_factor = self.fasting_hours_per_day / 16  # normalize to 16 hrs
        calorie_factor = self.calorie_deficit_per_day / 500
        base_fat_loss_per_day = 0.06 / 14  # per day for 16hr fast & 500 cal deficit, also assuming 14 days of fasting and calorie deficit

        return round(base_fat_loss_per_day * fasting_factor * calorie_factor * self.days, 3)

    def fasting_fat_burn_multiplier(self, fasting_factor):
        if fasting_factor < 12:
            return 0.1
        elif fasting_factor < 13:
            return 0.25
        elif fasting_factor < 14:
            return 0.4
        elif fasting_factor < 15:
            return 0.65
        elif fasting_factor < 16:
            return 0.85
        elif fasting_factor < 17:
            return 1.15
        elif fasting_factor < 18:
            return 1.35
        elif fasting_factor < 19:
            return 1.55
        elif fasting_factor < 20:
            return 1.75
        elif fasting_factor < 21:
            return 1.95
        elif fasting_factor < 22:
            return 2.00
        elif fasting_factor < 23:
            return 2.00
        elif fasting_factor < 24:
            return 2.00
        else:
            return 2.00  # or increase slightly if >16
    
    def estimate_fat_loss_with_multiplier(fasting_hours_per_day, days, calorie_deficit_per_day):
        fasting_multiplier = fasting_fat_burn_multiplier(fasting_hours_per_day)
        base_fat_loss = estimate_fat_loss(fasting_hours_per_day, days, calorie_deficit_per_day)
        return round(base_fat_loss * fasting_multiplier, 3)

    def adiponectin_modifier(genotype: str) -> float:
        modifiers = {
            "GG": 1.1,  # Ideal responder
            "GT": 1.0,  # Normal
            "TT": 0.9   # Reduced fat mobilization
        }
        return modifiers.get(genotype, 1.0)

    def estimate_fat_loss_with_genotype(fasting_hours_per_day, days, calorie_deficit_per_day, genotype: str):
        adiponectin_effect = adiponectin_modifier(genotype)
        base_fat_loss = estimate_fat_loss_with_multiplier(fasting_hours_per_day, days, calorie_deficit_per_day)
        return round(base_fat_loss * adiponectin_effect, 3)
