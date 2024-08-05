from django.db import models

from tradings.utils import CONDITION, FUEL_TYPES, TRANSMISSION, TYPE_OF_VEHICLE

class KeyFeatureTemplate(models.Model): 
    premium_pheel                           = models.BooleanField(default=False)
    sun_roof                                = models.BooleanField(default=False)
    premium_audio                           = models.BooleanField(default=False)
    navigation                              = models.BooleanField(default=False)
    front_heated_seats                      = models.BooleanField(default=False)
    premium_seat_material                   = models.BooleanField(default=False)
    bluetooth                               = models.BooleanField(default=False)
    premium_seat_material                   = models.BooleanField(default=False)
    front_heated_seats                      = models.BooleanField(default=False)
    remote_engine_start                     = models.BooleanField(default=False)
    blind_spot_System                       = models.BooleanField(default=False)
    multi_zone_climate_control              = models.BooleanField(default=False)
    has_roof_rack                           = models.BooleanField(default=False)
    electronic_doors                        = models.BooleanField(default=False)
    has_security                            = models.BooleanField(default=False)
    push_start_button                       = models.BooleanField(default=False)
    turbo_charger                           = models.BooleanField(default=False)
    driver_airbag                           = models.BooleanField(default=False)
    side_airbag                             = models.BooleanField(default=False)
    front_passenger_airbag                  = models.BooleanField(default=False)
    cruise_control                          = models.BooleanField(default=True)
    anti_lock_braking_systems               = models.BooleanField(default=False)
    front_park_camera                       = models.BooleanField(default=False)
    power_steering                          = models.BooleanField(default=False)
    roll_stabilitity_control                = models.BooleanField(default=False)
    rear_parking_camera                     = models.BooleanField(default=False)
    electronic_windows                      = models.BooleanField(default=False)
    electronic_brake_pressure_distribution  = models.BooleanField(default=False)
    has_immobilzer                          = models.BooleanField(default=False)
    

    class Meta:
        abstract = True
        verbose_name = 'KeyFeature'
        verbose_name_plural = 'KeyFeatures'
    
class EnginePerformanceTemplate(models.Model):
    induction                       = models.CharField(max_length=254, default='Aspirated')
    cylinders                       = models.IntegerField(default=0)
    wheels                          = models.IntegerField(default=4)
    seats                           = models.IntegerField(default=4)
    engine_config                   = models.CharField(max_length=254, default='In-line')
    valve_gear                      = models.CharField(max_length=254, default='DOHC with VVT')
    fuel_injection                  = models.CharField(max_length=254, default='Direct Injection')
    engine_size                     = models.CharField(max_length=100, default='3.5 L')
    fuel_type                       = models.CharField(max_length=100, choices=FUEL_TYPES, default='Petrol')
    transmission                    = models.CharField(max_length=100, choices=TRANSMISSION, default='Manual')
    engine_location                 = models.CharField(max_length=254, default='Aspirated')
    power                           = models.CharField(max_length=254, default='140 kw ')
    torque                          = models.CharField(max_length=254, default='7000 rpm')
    drive_type                      = models.CharField(max_length=254, default='FWD')
    body_type                       = models.CharField(max_length=254,  choices=TYPE_OF_VEHICLE, default='Hatchback')
    global_safety_rating            = models.CharField(max_length=254, default='G NCAP Rating', help_text='Global NCAP Safety Rating')
    stearing_wheel                  = models.CharField(max_length=100, default="Standard")
    bluetooth                       = models.CharField(max_length=100, default="Standard")
    usb_port                        = models.CharField(max_length=100, default="Standard")
    remote_central_locking          = models.CharField(max_length=100, default="Standard")
    is_repaired                     = models.BooleanField(default=False)

    class Meta:
        abstract = True
        verbose_name = 'EngineFeature'
        verbose_name_plural = 'EngineFeatures'
