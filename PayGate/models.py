from django.db import models
from django.utils.text import gettext_lazy as _

from drfaddons.models import CreateUpdateModel
# Create your models here.
class PayTMConfiguration(CreateUpdateModel):
    """
    Contains PayTM Configurations. Only one object can have is_active
    set to True that will be used by the system by default.
    Currently to provision for multiple configuration at the runtime.

    """

    from .utils import validate_key

    mid = models.CharField(verbose_name=_("Merchant ID"), max_length=20,
                           unique=True)
    mkey = models.CharField(verbose_name=_("Merchant Key"), max_length=32,
                            validators=[validate_key])
    is_active = models.BooleanField(verbose_name=_("Is Active?"),
                                    default=False)
    gateway_url = models.URLField(verbose_name=_("Payment Gateway URL"),
                                  default="https://securegw-stage.paytm.in/the"
                                          "ia/processTransaction")
    status_url = models.URLField(verbose_name=_("Payment Status URL"),
                                 default="https://securegw-stage.paytm.in/merc"
                                         "hant-status/getTxnStatus")
    company_name = models.CharField(verbose_name=_("Company Name"),
                                    max_length=254)
    base_url = models.URLField(verbose_name=_("Base URL (without / at end)"),
                               default="http://127.0.0.1:8000")

    def __str__(self):
        return self.mid

    def clean_fields(self, exclude=None):
        """
        Used to validate the value of is_active
        Parameters
        ----------
        exclude: list of fields that is to be excluded while checking
        Returns
        -------
        None
        Raises
        ------
        ValidationError: for is_active field.
        
        """
        from django.core.exceptions import ValidationError

        if 'is_active' not in exclude:
            try:
                pc = PayTMConfiguration.objects.get(is_active=True)
            except PayTMConfiguration.DoesNotExist:
                pass
            except PayTMConfiguration.MultipleObjectsReturned:
                raise ValidationError({'is_active':
                                           _("Multiple configuration is "
                                             "active. Keep only 1 "
                                             "configuration active at a "
                                             "time.")})
            else:
                if pc.mid is not self.mid:
                    raise ValidationError({'is_active': _("Another "
                                                          "configuration is "
                                                          "active. Deactivate "
                                                          "it first.")})
        super(PayTMConfiguration, self).clean_fields(exclude=exclude)

    class Meta:
        verbose_name = _("PayTM Configuration")
        verbose_name_plural = _("PayTM Configurations")
