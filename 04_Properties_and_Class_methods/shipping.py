#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .iso3436 import create


class ShippingContainer:
    # CLASS INSTANCES
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0
    next_serial = 1337

    # Static method used for the sole purpose of logical organisation of code
    @staticmethod
    def _make_bic_code(owner_code, serial):
        return create(owner_code=owner_code,
                      serial=str(serial).zfill(6))

    # Use of class method as we try to access class instance 'next_serial'
    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    # Named Constructors or Factory Functions:
    # Functions within class which construct objects with certain configurations.
    @classmethod
    def create_empty(cls, owner_code, length_ft, *args, **kwargs):
        return cls(owner_code, length_ft, contents=None, *args, **kwargs)

    # Named Constructors or Factory Functions:
    # Functions within class which construct objects with certain configurations.
    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, *args, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), *args, **kwargs)

    def __init__(self, owner_code, length_ft, contents):
        self.contents = contents
        self.length_ft = length_ft
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._get_next_serial()
        )

    @property
    def volume_ft3(self):
        return (
            ShippingContainer.HEIGHT_FT
            * ShippingContainer.WIDTH_FT
            * self.length_ft
        )


class RefrigeratedShippingContainer(ShippingContainer):
    # CLASS INSTANCE
    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    # Static method used for the sole purpose of logical organisation of code
    @staticmethod
    def _make_bic_code(owner_code, serial):
        return create(owner_code=owner_code,
                      serial=str(serial).zfill(6),
                      category='R')

    # Static method used for the sole purpose of logical organisation of code
    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9 / 5 + 32

    # Static method used for the sole purpose of logical organisation of code
    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    def __init__(self, owner_code, length_ft, contents, celsius):
        super().__init__(owner_code, length_ft, contents)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)

    @property
    def volume_ft3(self):
        return (
            super().volume_ft3
            - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3
        )


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

    MIN_CELSIUS = -20.0

    @RefrigeratedShippingContainer.celsius.setter
    def celsius(self, value):
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature too cold!")
        # super().celsius = value # Does not work as celsius is a private property
        RefrigeratedShippingContainer.celsius.fset(self, value)