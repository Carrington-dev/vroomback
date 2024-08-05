from rest_framework import serializers
from security.models import User
from tradings.models import CarModel, City, Enquiry, Country, Image, Make, State, Vehicle, VehicleKeyFeatures, VehicleOtherFeatures

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = [ "id", "vehicle", "full_name", "email", "phone", "message", ]

class VehicleOtherFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleOtherFeatures
        fields = [ "id", "induction", "cylinders", "wheels", "seats", "engine_config",\
                  "valve_gear", "fuel_injection", "engine_size", "fuel_type", 'is_repaired',\
                    "engine_location","power","torque","drive_type","global_safety_rating",\
                        "stearing_wheel","bluetooth","usb_port","remote_central_locking", \
                            'transmission', 'body_type']

class VehicleKeyFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleKeyFeatures
        fields = [ "id", "premium_pheel", "sun_roof", "premium_audio", "navigation", "bluetooth", "premium_seat_material", "front_heated_seats", "remote_engine_start", "blind_spot_System", "multi_zone_climate_control", "has_roof_rack", "electronic_doors", "has_security", "push_start_button", "turbo_charger", "driver_airbag", "side_airbag", "front_passenger_airbag", "cruise_control", "anti_lock_braking_systems", "front_park_camera", "power_steering", "roll_stabilitity_control", "rear_parking_camera", "electronic_windows", "electronic_brake_pressure_distribution", "has_immobilzer",]

class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = [ 'name', 'id' , ]

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [ 'color', 'photo' , ]


class CarMakeSerializer(serializers.PrimaryKeyRelatedField):
    class Meta:
        model = Make
        fields = [ 'name', ]

    def get_queryset(self):
        return Make.objects.all()

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = [ 'name', 'id' , ]

class CarModelSerializer(serializers.ModelSerializer):
    make = CarMakeSerializer(queryset=Make.objects.all())
    
    class Meta:
        model = CarModel
        fields = [ 'name', 'id' ,  'make']


class StateSerializer(serializers.ModelSerializer):
    cities =  CitySerializer(many=True, read_only=True)
    class Meta:
        model = State
        fields = [ 'name', 'id' , 'cities' ]


class VehicleMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = [ 'name', ]

    def get_queryset(self):
        return Make.objects.all()

class VehicleCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [ 'name', ]

class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = [ 'name',   ]
    def get_queryset(self):
        return CarModel.objects.all()


class VehicleStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = [ 'name', ]
        
    def get_queryset(self):
        return State.objects.all()



class CountrySerializer(serializers.ModelSerializer):
    states = StateSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = [ 'name', 'id' , 'states' ]



class VehicleSerializer(serializers.ModelSerializer):
    state = VehicleStateSerializer(read_only=True)
    model = VehicleModelSerializer(read_only=True)
    city = VehicleCitySerializer(read_only=True)
    make = VehicleMakeSerializer(read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    # interior_images = serializers.SerializerMethodField(method_name='interior')
    # exterior_images = serializers.SerializerMethodField(method_name='exterior')
    interior_images = ImageSerializer(many=True, read_only=True)
    exterior_images = ImageSerializer(many=True, read_only=True)
    # state = VehicleStateSerializer(queryset=State.objects.all())
    # model = VehicleModelSerializer(queryset=CarModel.objects.all())
    # city = VehicleCitySerializer(queryset=City.objects.all())
    # make = VehicleMakeSerializer(queryset=Make.objects.all())
    other_features =  VehicleOtherFeaturesSerializer(read_only=True)
    key_features =  VehicleKeyFeaturesSerializer(read_only=True)

    class Meta:
        model = Vehicle
        fields = [  'id', "title", "model", "make", "state", 'images', 'interior_images', 'exterior_images', "user", 'video_url', "type", "city", 'photo',  'year',"price", \
                  "mileage", "engine_capacity", "condition", "colour", "top_speed", \
                  'key_features', 'other_features', 'slug', \
                    "stock",  "horse_power", "airbag_quantity", "gears", ]
        

    # def interior(self, obj):
    #     return ImageSerializer(obj.images.filter(side="interior"))
    
    # def exterior(self, obj):
    #     return ImageSerializer(obj.images.filter(side="exterior"))
    
class VehicleSerializerByUser(serializers.ModelSerializer):
    vehicles = VehicleSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = [ "id", "first_name", "last_name", "vehicles" ]