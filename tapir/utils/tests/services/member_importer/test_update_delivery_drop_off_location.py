from tapir.utils.services.member_importer import MemberImporter
from tapir.wirgarten.tests.factories import MemberFactory
from tapir.wirgarten.tests.test_utils import TapirUnitTest


class TestUpdateDeliveryDropOffLocation(TapirUnitTest):
    def test_updateDeliveryDropOffLocation_cellFilled_setsDropOffLocation(self):
        member = MemberFactory.build(
            delivery_same_as_billing_address=True, delivery_drop_off_location=""
        )

        result = MemberImporter.update_delivery_drop_off_location(
            member=member, row={"Alternativer Ablageort": " Garage "}
        )

        self.assertTrue(result)
        self.assertEqual("Garage", member.delivery_drop_off_location)
        self.assertTrue(member.delivery_same_as_billing_address)

    def test_updateDeliveryDropOffLocation_cellEmpty_keepsDropOffLocation(self):
        member = MemberFactory.build(delivery_drop_off_location="Garage")

        result = MemberImporter.update_delivery_drop_off_location(
            member=member, row={"Alternativer Ablageort": ""}
        )

        self.assertFalse(result)
        self.assertEqual("Garage", member.delivery_drop_off_location)

    def test_updateDeliveryDropOffLocation_sameValue_returnsFalse(self):
        member = MemberFactory.build(delivery_drop_off_location="Garage")

        result = MemberImporter.update_delivery_drop_off_location(
            member=member, row={"Alternativer Ablageort": "Garage"}
        )

        self.assertFalse(result)
