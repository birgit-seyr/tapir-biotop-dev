import React from "react";
import { Form } from "react-bootstrap";
import { DeliveryAddressRequest } from "../api-client";
import { DROP_OFF_LOCATION_LABEL } from "../utils/dropOffLocationLabel.ts";

interface DeliveryAddressFieldsProps {
  deliveryAddress: DeliveryAddressRequest;
  setDeliveryAddress: (deliveryAddress: DeliveryAddressRequest) => void;
}

type AddressField = "street" | "street2" | "postcode" | "city";

const FIELDS: { field: AddressField; label: string }[] = [
  { field: "street", label: "Straße & Hausnummer" },
  { field: "street2", label: "Adresszusatz (optional)" },
  { field: "postcode", label: "Postleitzahl" },
  { field: "city", label: "Stadt" },
];

const DeliveryAddressFields: React.FC<DeliveryAddressFieldsProps> = ({
  deliveryAddress,
  setDeliveryAddress,
}) => {
  return (
    <>
      <Form.Check
        id={"delivery_same_as_billing_address"}
        label={"Lieferadresse entspricht der Rechnungsadresse"}
        checked={deliveryAddress.sameAsBillingAddress}
        onChange={(event) =>
          setDeliveryAddress({
            ...deliveryAddress,
            sameAsBillingAddress: event.target.checked,
          })
        }
      />
      {!deliveryAddress.sameAsBillingAddress &&
        FIELDS.map(({ field, label }) => (
          <Form.Group key={field} controlId={"delivery_" + field}>
            <Form.Label>{label}</Form.Label>
            <Form.Control
              value={deliveryAddress[field] ?? ""}
              onChange={(event) =>
                setDeliveryAddress({
                  ...deliveryAddress,
                  [field]: event.target.value,
                })
              }
            />
          </Form.Group>
        ))}
      <Form.Group controlId={"delivery_drop_off_location"}>
        <Form.Label>{DROP_OFF_LOCATION_LABEL}</Form.Label>
        <Form.Control
          value={deliveryAddress.dropOffLocation ?? ""}
          onChange={(event) =>
            setDeliveryAddress({
              ...deliveryAddress,
              dropOffLocation: event.target.value,
            })
          }
        />
      </Form.Group>
    </>
  );
};

export default DeliveryAddressFields;
