from decimal import Decimal

import factory

from openforms.submissions.tests.factories import SubmissionFactory

from ..models import SubmissionPayment


class SubmissionPaymentFactory(factory.django.DjangoModelFactory):
    submission = factory.SubFactory(SubmissionFactory)
    plugin_id = "demo"
    plugin_options = {"foo": 123}
    order_id = factory.Sequence(lambda n: int(f"2020{n:05}"))
    amount = Decimal("10.00")
    public_order_id = factory.LazyAttribute(lambda obj: f"ref{obj.order_id}")

    class Meta:
        model = SubmissionPayment

    @classmethod
    def for_backend(cls, plugin_id, options=None, **kwargs):
        options = options or {"non-empty": True}
        payment = cls.create(
            plugin_id=plugin_id,
            plugin_options=options,
            submission__form__payment_backend=plugin_id,
            submission__form__payment_backend_options=options,
            **kwargs,
        )
        return payment

    @classmethod
    def for_submission(cls, submission, **kwargs):
        payment = cls.create(
            submission=submission,
            plugin_id=submission.form.payment_backend,
            plugin_options=submission.form.payment_backend_options,
            amount=submission.price,
            **kwargs,
        )
        return payment
