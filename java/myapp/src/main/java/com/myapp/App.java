package com.myapp;

import jp.ne.paypay.*;

    public class App  {
     public static void main( String[] args ) {

        String APIKEY = "";
        String APISECRET = "";
        String MID = "";

        ApiClient apiClient = new Configuration().getDefaultApiClient();
        apiClient.setProductionMode(false); //Set True for Production Environment. By Default this is set False for Sandbox Environment.
        apiClient.setApiKey(APIKEY);
        apiClient.setApiSecretKey(APISECRET);
        apiClient.setAssumeMerchant(MID);
             
        // Creating the payload to create a QR Code, additional parameters can be added basis the API Documentation
        QRCode qrCode = new QRCode();
              qrCode.setAmount(new MoneyAmount().amount(10).currency(MoneyAmount.CurrencyEnum.JPY));
              qrCode.setMerchantPaymentId("tsuk-mpId-12345");
              qrCode.setCodeType("ORDER_QR");
              qrCode.setOrderDescription("tsuk shop");
              qrCode.isAuthorization(false);
              qrCode.redirectUrl("https://paypay.ne.jp/");
              qrCode.redirectType(QRCode.RedirectTypeEnum.WEB_LINK);
            
        // Calling the method to create a qr code
        PaymentApi apiInstance = new PaymentApi(apiClient);
        QRCodeDetails response = apiInstance.createQRCode(qrCode);

        // Printing if the method call was SUCCESS
        System.out.println(response.getResultInfo().getCode());
        System.out.println("helloworld");

    }
}
