from cypherpunkpay.db.db import DB
from cypherpunkpay.usecases import UseCase
from cypherpunkpay.usecases.call_payment_failed_url_uc import CallPaymentFailedUrlUC


class NotifyMerchantOfAllFailedUC(UseCase):

    def __init__(self, db: DB, config=None, http_client=None):
        self._db = db
        self._config = config
        self._http_client = http_client

    def exec(self):
        charges = self._db.get_charges_for_merchant_notification(statuses=['cancelled', 'expired'])
        for charge in charges:
            CallPaymentFailedUrlUC(charge=charge, db=self._db, config=self._config, http_client=self._http_client).exec()
