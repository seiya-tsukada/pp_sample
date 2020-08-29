<?php

require 'vendor/autoload.php';

use PayPay\OpenPaymentAPI\Client;
use PayPay\OpenPaymentAPI\Models\CreateQrCodePayload;
use PayPay\OpenPaymentAPI\Models\OrderItem;

$APIKEY = "";
$APISECRET = "";
$MID = "";

//Set True for Production Environment. By Default this is set False for Sandbox Environment.
$client = new Client([
  'API_KEY' => $APIKEY,
  'API_SECRET'=> $APISECRET,
  'MERCHANT_ID'=> $MID
],false);

// setup payment object
$CQCPayload = new CreateQrCodePayload();

// Set merchant pay identifier
$merchantPaymentId = "tsuk-qr-".time();
$CQCPayload->setMerchantPaymentId($merchantPaymentId);

// Log time of request
$CQCPayload->setRequestedAt();

// Indicate you want QR Code
$CQCPayload->setCodeType("ORDER_QR");

// Provide order details for invoicing
$OrderItems = [];
$OrderItems[] = (new OrderItem())
    ->setName('tsuk shop')
    ->setQuantity(1)
    ->setUnitPrice(['amount' => 100, 'currency' => 'JPY']);

$CQCPayload->setOrderItems($OrderItems);

// Save Cart totals
$amount = [
    "amount" => 100,
    "currency" => "JPY"
];

$CQCPayload->setAmount($amount);

// Configure redirects
$CQCPayload->setRedirectType('WEB_LINK');
$CQCPayload->setRedirectUrl('https//paypay.ne.jp');

// Get data for QR code
$response = $client->code->createQRCode($CQCPayload);

$data = $response['data'];

var_dump($data);

?>