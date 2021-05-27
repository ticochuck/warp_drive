from django.db import models
from django.urls import reverse

class Vehicle(models.Model):
    name = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    vehicle_type = models.CharField(max_length=64)
    prop_orientation = models.CharField(max_length=64)
    max_prop_dia = models.CharField(max_length=64)
    crew = models.CharField(max_length=64)
    engine_count = models.CharField(max_length=64)
    length = models.CharField(max_length=64)
    height = models.CharField(max_length=64)
    wingspan = models.CharField(max_length=64)
    wing_area = models.CharField(max_length=64)
    design_load_factor = models.CharField(max_length=64)
    fuel_capacity = models.CharField(max_length=64)
    vne = models.CharField(max_length=64)
    cruise_speed = models.CharField(max_length=64)
    production_years = models.CharField(max_length=64)
    link_1 = models.CharField(max_length=64)
    vehicle_notes = models.CharField(max_length=64)


    def __str__(self):
        return f'{self.name}, {self.manufacturer}, {self.model}'


    def get_absolute_url(self):
        return reverse('home')
    

class Engine(models.Model):
    name = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    displacement = models.CharField(max_length=64)
    displacement_cu_in = models.CharField(max_length=64)
    horsepower = models.CharField(max_length=64)
    rpm_max = models.CharField(max_length=64)
    rpm_cruise = models.CharField(max_length=64)
    rotation = models.CharField(max_length=64)
    rotation_notes = models.CharField(max_length=64)
    selection_field_qxfWJ = models.CharField(max_length=64)
    cylinder_count = models.CharField(max_length=64)
    cooling = models.CharField(max_length=64)
    website = models.CharField(max_length=64)
    possible_reduction_ratios = models.CharField(max_length=64)
    important_note = models.CharField(max_length=64)
    bolt_patterns = models.CharField(max_length=64)
    notes = models.CharField(max_length=64)
    

    def __str__(self):
        return f'{self.name}, {self.manufacturer}, {self.model}'


    def get_absolute_url(self):
        return reverse('home')


class Propeller(models.Model):
    name = models.CharField(max_length=64)
    product_id = models.CharField(max_length=64)
    old_Serial = models.CharField(max_length=64, blank=True)
    new_Serial = models.CharField(max_length=64, blank=True)
    hub_Serial = models.CharField(max_length=64, blank=True)
    status = models.CharField(max_length=64, blank=True)
    do_not_import = models.CharField(max_length=64, blank=True)
    hub_model = models.CharField(max_length=64, blank=True)
    blade_count = models.CharField(max_length=64, blank=True)
    blade_model = models.CharField(max_length=64, blank=True)
    bld_dia = models.CharField(max_length=64, blank=True)
    taper = models.CharField(max_length=64, blank=True)
    rotation = models.CharField(max_length=64, blank=True)
    taper_specs = models.CharField(max_length=64, blank=True)
    nickel_LE = models.CharField(max_length=64, blank=True)
    tip_color = models.CharField(max_length=64, blank=True)
    weight_start = models.CharField(max_length=64, blank=True)
    weight_end = models.CharField(max_length=64, blank=True)
    weight_vert = models.CharField(max_length=64, blank=True)
    weight_taperbefore = models.CharField(max_length=64, blank=True)
    weight_taperafter = models.CharField(max_length=64, blank=True)
    tracking = models.CharField(max_length=64, blank=True)
    bld_notes = models.CharField(max_length=64, blank=True)
    pinned_collars = models.CharField(max_length=64, blank=True)
    customer_id = models.CharField(max_length=64, blank=True)
    customer_notes = models.CharField(max_length=64, blank=True)
    vehicle_id = models.CharField(max_length=64, blank=True)
    vehicle_notes = models.CharField(max_length=64, blank=True)
    engine_id = models.CharField(max_length=64, blank=True)
    engine_notes = models.CharField(max_length=64, blank=True)
    bolt_pattern = models.CharField(max_length=64, blank=True)
    bolt_pattern_notes_new_field = models.CharField(max_length=64, blank=True)
    reduction_ratio_rename_to_red_drive_name = models.CharField(max_length=64, blank=True)
    reduction_style = models.CharField(max_length=64, blank=True)
    update_1_date = models.CharField(max_length=64, blank=True)
    update_1 = models.CharField(max_length=64, blank=True)
    update_2_date = models.CharField(max_length=64, blank=True)
    update_2 = models.CharField(max_length=64, blank=True)
    update_3_date = models.CharField(max_length=64, blank=True)
    update_3 = models.CharField(max_length=64, blank=True)
    update_4_date = models.CharField(max_length=64, blank=True)
    update_4 = models.CharField(max_length=64, blank=True)
    update_5_Date = models.CharField(max_length=64, blank=True)
    update_5 = models.CharField(max_length=64, blank=True)
    x_studio_ship_date = models.CharField(max_length=64, blank=True)
    old_notes = models.CharField(max_length=64, blank=True)
    old_bldspecs = models.CharField(max_length=64, blank=True)
    old_bldnum = models.CharField(max_length=64, blank=True)
    old_bldtype = models.CharField(max_length=64, blank=True)
    old_hub = models.CharField(max_length=64, blank=True)
    

    def __str__(self):
        return f'{self.name}, {self.vehicle_id}, {self.engine_id}'


    def get_absolute_url(self):
        return reverse('home')

