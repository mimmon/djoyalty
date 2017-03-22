from django.db import models


class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=32, unique=True)
    firstname = models.CharField(max_length=64, null=True, blank=True)
    lastname = models.CharField(max_length=64, null=True, blank=True)
    street = models.CharField(max_length=64, null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    zip = models.CharField(max_length=16, null=True, blank=True)
    email = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=64, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    newsletter = models.BooleanField(default=True)

    def __str__(self):
        return '[{}] {}'.format(self.code, ' '.join(filter(None, [self.firstname, self.lastname])))


class FullPriceTxnManager(models.Manager):
    def get_queryset(self):
        return super(FullPriceTxnManager, self).get_queryset().filter(is_discount=False)


class DiscountedTxnManager(models.Manager):
    def get_queryset(self):
        return super(DiscountedTxnManager, self).get_queryset().filter(is_discount=True)


class Txn(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('Customer', related_name='transactions')
    value = models.DecimalField()
    is_discount = models.BooleanField(default=False)

    objects = models.Manager()
    txn_full = FullPriceTxnManager()
    txn_discount = DiscountedTxnManager()

    def __str__(self):
        return '{}{}@{} by {}'.format(self.value, '[X]' if self.is_discount else '', self.timestamp, self.customer)


class CustomerRelatedEvtManager(models.Manager):
    def get_queryset(self):
        return super(CustomerRelatedEvtManager, self).get_queryset().filter(customer=None)


class Event(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('Customer', related_name='transactions', null=True, blank=True)
    action = models.CharField()
    description = models.DateTimeField(null=True, blank=True)

    objects = models.Manager()
    customer_related = CustomerRelatedEvtManager()
