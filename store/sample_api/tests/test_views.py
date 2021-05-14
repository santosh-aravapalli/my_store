from rest_framework.test import APIClient
from rest_framework.reverse import reverse
import pytest
from office.models import offices


@pytest.mark.django_db
def test_sample():
    off = {
        "officecode":1,
        "city":"hyderabad",
        "phone":999999999,
        "addressline1":"kphb",
        "addressline2":"hyderabad",
        "state":"telangana",
        "country":"india",
        "postalcode":456789,
        "territory":"hhhh"
    }
    o = offices.objects.create(**off)
    client = APIClient()
    response = client.post(reverse("createemployee"))
    assert response.data['message'] == "employee created"
    assert True