from django.db import models


class Listing(models.Model):
    MONTHLY = '1'
    BIMONTHLY = '2'
    QUARTERLY = '3'
    HALFYEARLY = '6'
    YEARLY = '12'
    BIYEARLY = '24'
    TRIYEARLY = '48'

    BILLING = (
        (MONTHLY, 'Monthly'),
        (BIMONTHLY, 'Bi-Monthly'),
        (QUARTERLY, 'Quarterly'),
        (HALFYEARLY, 'Half-Yearly'),
        (YEARLY, 'Yearly'),
        (BIYEARLY, 'Bi-Yearly'),
        (TRIYEARLY, 'Tri-Yearly'),
    )

    KVM = 'kvm'
    OPENVZ = 'ovz'

    VIRTUAL = (
        (KVM, 'KVM'),
        (OPENVZ, 'OpenVZ'),
    )

    # Plan Details
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    billing_period = models.CharField(max_length=2, choices=BILLING, default=MONTHLY)
    coupon_code = models.CharField(default="", max_length=255)
    link = models.URLField(max_length=255)
    notes = models.TextField(default='')
    #Plan Specs
    virt_type = models.CharField(max_length=3, choices=VIRTUAL, default=OPENVZ)
    ram = models.IntegerField()  # In MB
    burst = models.IntegerField(default=0)  # Burst RAM
    hdd = models.IntegerField()  # In GB
    ipv4 = models.IntegerField(default=0)  # Number of IPv4 Addresses
    ipv6 = models.IntegerField(default=0)  # Number of IPv6 Addresses
    bandwidth = models.IntegerField()  # In GB
    cpu = models.IntegerField(default=1)  # Number of vCPU cores
    #Plan Meta
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    #Calculated Data
    monthly_cost = models.DecimalField(max_digits=20, decimal_places=3)
    yearly_cost = models.DecimalField(max_digits=20, decimal_places=3)

    def monthly_price(self):
        if self.billing_period == self.MONTHLY:
            return self.price
        if self.billing_period == self.BIMONTHLY:
            return float(self.price) / 2.0
        if self.billing_period == self.QUARTERLY:
            return float(self.price) / 3.0
        if self.billing_period == self.HALFYEARLY:
            return float(self.price) / 6.0
        if self.billing_period == self.YEARLY:
            return float(self.price) / 12.0
        if self.billing_period == self.BIYEARLY:
            return float(self.price) / 24.0
        if self.billing_period == self.TRIYEARLY:
            return float(self.price) / 48.0
        return self.price

    def yearly_price(self):
        if self.billing_period == self.MONTHLY:
            return self.price * 12
        if self.billing_period == self.BIMONTHLY:
            return float(self.price) * 6.0
        if self.billing_period == self.QUARTERLY:
            return float(self.price) * 4.0
        if self.billing_period == self.HALFYEARLY:
            return float(self.price) * 2.0
        if self.billing_period == self.YEARLY:
            return float(self.price)
        if self.billing_period == self.BIYEARLY:
            return float(self.price) / 2.0
        if self.billing_period == self.TRIYEARLY:
            return float(self.price) / 3.0

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.monthly_cost = self.monthly_price()
        self.yearly_cost = self.yearly_price()
        super(Listing, self).save(force_insert, force_update, using, update_fields)

