package main

import (
	"fmt"
	"os"

	"github.com/EasyPost/easypost-go"
)

func main() {
	var apiKey string = ""
	if apiKey == "" {
		fmt.Fprintln(os.Stderr, "missing API key")
		os.Exit(1)
		return
	}
	client := easypost.New(apiKey)

	// create and verify addresses
	toAddr, err := client.CreateAddress(
		&easypost.Address{
			Name:    "Bugs Bunny",
			Street1: "4000 Warner Blvd",
			City:    "Burbank",
			State:   "CA",
			Zip:     "91522",
		},
		&easypost.CreateAddressOptions{Verify: []string{"delivery"}},
	)
	if err != nil {
		fmt.Fprintln(os.Stderr, "error creating to address:", err)
		os.Exit(1)
		return
	}

	fromAddr, err := client.CreateAddress(
		&easypost.Address{
			Company: "EasyPost",
			Street1: "One Montgomery St",
			Street2: "Ste 400",
			City:    "San Francisco",
			State:   "CA",
			Zip:     "94104",
			Phone:   "415-555-1212",
		},
		&easypost.CreateAddressOptions{Verify: []string{"delivery"}},
	)
	if err != nil {
		fmt.Fprintln(os.Stderr, "error creating from address:", err)
		os.Exit(1)
		return
	}

	// create parcel
	parcel, err := client.CreateParcel(
		&easypost.Parcel{
			Length: 10.2,
			Width:  7.8,
			Height: 4.3,
			Weight: 21.2,
		},
	)
	if err != nil {
		fmt.Fprintln(os.Stderr, "error creating parcel:", err)
		os.Exit(1)
		return
	}

	// create customs_info form for intl shipping
	customsItem, err := client.CreateCustomsItem(
		&easypost.CustomsItem{
			Description:    "EasyPost t-shirts",
			HSTariffNumber: "123456",
			OriginCountry:  "US",
			Quantity:       2,
			Value:          96.27,
			Weight:         21.1,
		},
	)
	if err != nil {
		fmt.Fprintln(os.Stderr, "error creating customs item:", err)
		os.Exit(1)
		return
	}

	customsInfo, err := client.CreateCustomsInfo(
		&easypost.CustomsInfo{
			CustomsCertify:    true,
			CustomsSigner:     "Wile E. Coyote",
			ContentsType:      "gift",
			EELPFC:            "NOEEI 30.37(a)",
			NonDeliveryOption: "return",
			RestrictionType:   "none",
			CustomsItems:      []*easypost.CustomsItem{customsItem},
		},
	)
	if err != nil {
		fmt.Fprintln(os.Stderr, "error creating customs info:", err)
		os.Exit(1)
		return
	}

	// create shipment
	shipment, err := client.CreateShipment(
		&easypost.Shipment{
			ToAddress:   toAddr,
			FromAddress: fromAddr,
			Parcel:      parcel,
			CustomsInfo: customsInfo,
		},
	)
	if err != nil {
		fmt.Fprintln(os.Stderr, "error creating shipment:", err)
		os.Exit(1)
		return
	}

	// buy postage label with one of the rate objects
	shipment, err = client.BuyShipment(shipment.ID, &easypost.Rate{ID: shipment.Rates[0].ID}, "")
	if err != nil {
		fmt.Fprintln(os.Stderr, "error buying shipment:", err)
		os.Exit(1)
		return
	}

	fmt.Println("tracking code:", shipment.TrackingCode)
	fmt.Println("label URL:", shipment.PostageLabel.LabelURL)

	// Insure the shipment for the value
	shipment, err = client.InsureShipment(shipment.ID, "100")
	if err != nil {
		fmt.Fprintln(os.Stderr, "error insuring shipment:", err)
		os.Exit(1)
		return
	}
}
