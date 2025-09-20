import stripe
from decouple import config

DJANGO_DEBUG = config("DJANGO_DEBUG", default=True, cast=bool)
STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY", default="")

if "sk_test" in STRIPE_SECRET_KEY and not DJANGO_DEBUG:
    raise ValueError("Invalid stripe key for production")

stripe.api_key = STRIPE_SECRET_KEY

def create_customer():
    return stripe.Customer.create(
        name="Jenny Rosen",
        email="jennyrosen@example.com",
    )
