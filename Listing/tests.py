"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from Listing.models import Listing


class TestListingModelMethods(TestCase):
    def setUp(self):
        self.listing = Listing(
            name='The Server Listing',
            price=12.00,
            link='http://example.com?id=6',
            ram=2048,
            hdd=20,
            ipv4=1,
            bandwidth=1000,
            cpu=1,
        )
        self.listing.save()

    # Listing.monthly_price() tests
    def test_monthly_price_with_monthly(self):
        """
        Listing.monthly_price() should return the same value as the price if the billing is set to monthly
        """
        self.listing.billing_period = Listing.MONTHLY
        self.listing.save()
        self.assertEqual(self.listing.monthly_price(), 12.0)

    def test_monthly_price_with_bimonthly(self):
        """
        Listing.monthly_price() should return the value of the price halved if the billing is set to bimonthly
        """
        self.listing.billing_period = Listing.BIMONTHLY
        self.listing.save()
        self.assertEqual(self.listing.monthly_price(), 6.0)

    def test_monthly_price_with_quarterly(self):
        """
        Listing.monthly_price() should return the value of the price divided by 3 if the billing is set to quarterly
        """
        self.listing.billing_period = Listing.QUARTERLY
        self.listing.save()
        self.assertEqual(self.listing.monthly_price(), 4.0)

    def test_monthly_price_with_half_yearly(self):
        """
        Listing.monthly_price() should return the value of the price divided by 6 if the billing is set to half-yearly
        """
        self.listing.billing_period = Listing.HALFYEARLY
        self.listing.save()
        self.assertEqual(self.listing.monthly_price(), 2.0)

    def test_monthly_price_with_yearly(self):
        """
        Listing.monthly_price() should return the value of the price divided by 12 if the billing is set to yearly
        """
        self.listing.billing_period = Listing.YEARLY
        self.listing.save()
        self.assertEqual(self.listing.monthly_price(), 1.0)

    def test_monthly_price_with_biyearly(self):
        """
        Listing.monthly_price() should return the value of the price divided by 24 if the billing is set to biyearly
        """
        self.listing.billing_period = Listing.BIYEARLY
        self.listing.save()
        self.assertEqual(self.listing.monthly_price(), 0.50)

    def test_monthly_price_with_biyearly(self):
        """
        Listing.monthly_price() should return the value of the price divided by 48 if the billing is set to triyearly
        """
        self.listing.billing_period = Listing.TRIYEARLY
        self.listing.save()
        self.assertEqual(self.listing.monthly_price(), 0.25)

    # Listing.yearly_price() tests

    def test_yearly_price_with_monthly(self):
        """
        Listing.yearly_price() should return the same value as the price if the billing is set to monthly
        """
        self.listing.billing_period = Listing.MONTHLY
        self.listing.save()
        self.assertEqual(self.listing.yearly_price(), 144.0)

    def test_yearly_price_with_bimonthly(self):
        """
        Listing.yearly_price() should return the value of the price halved if the billing is set to bimonthly
        """
        self.listing.billing_period = Listing.BIMONTHLY
        self.listing.save()
        self.assertEqual(self.listing.yearly_price(), 72.0)

    def test_yearly_price_with_quarterly(self):
        """
        Listing.yearly_price() should return the value of the price divided by 3 if the billing is set to quarterly
        """
        self.listing.billing_period = Listing.QUARTERLY
        self.listing.save()
        self.assertEqual(self.listing.yearly_price(), 48.0)

    def test_yearly_price_with_half_yearly(self):
        """
        Listing.yearly_price() should return the value of the price divided by 6 if the billing is set to half-yearly
        """
        self.listing.billing_period = Listing.HALFYEARLY
        self.listing.save()
        self.assertEqual(self.listing.yearly_price(), 24.0)

    def test_yearly_price_with_yearly(self):
        """
        Listing.yearly_price() should return the value of the price divided by 12 if the billing is set to yearly
        """
        self.listing.billing_period = Listing.YEARLY
        self.listing.save()
        self.assertEqual(self.listing.yearly_price(), 12.0)

    def test_yearly_price_with_biyearly(self):
        """
        Listing.yearly_price() should return the value of the price divided by 24 if the billing is set to biyearly
        """
        self.listing.billing_period = Listing.BIYEARLY
        self.listing.save()
        self.assertEqual(self.listing.yearly_price(), 6.0)

    def test_yearly_price_with_biyearly(self):
        """
        Listing.yearly_price() should return the value of the price divided by 48 if the billing is set to triyearly
        """
        self.listing.billing_period = Listing.TRIYEARLY
        self.listing.save()
        self.assertEqual(self.listing.yearly_price(), 4.0)