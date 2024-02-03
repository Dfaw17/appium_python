from selenium.webdriver.common.by import By

close_modal = [By.ID, "android:id/button2"]
btn_fab = [By.ID, "com.chad.financialrecord:id/fabMenu"]
date1 = [By.ID, "com.chad.financialrecord:id/tvDate"]
date2 = [By.XPATH, '(//*[@resource-id="android:id/month_view"]/child::*)[1]']
date3 = [By.ID, 'android:id/button1']
category1 = [By.ID, 'com.chad.financialrecord:id/spCategory']
category2 = [By.XPATH, '//*[@resource-id="com.chad.financialrecord:id/tvName" and @text="Rokok"]']
amount = [By.ID, 'com.chad.financialrecord:id/etAmount']
note = [By.ID, 'com.chad.financialrecord:id/etNote']
btnSave = [By.ID, 'com.chad.financialrecord:id/btSave']
assertRokokSurya = [By.XPATH, '//*[@text="Rokok Surya"]']