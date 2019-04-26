# webform-fulfill-automation

There is a working zap where it's needed to add a step to take the 4 existing values and post/submit them to a webform. The trigger comes from a webform so the details are exactly the same, and they are simply being validated against a google sheet to make sure the right person is submitting the form.

The solution comes with an automation using Selenium in Pyhton and/or a actor developed in Apify

The pyton should be launched with these parameters:

```
python fulfill_form.py --url  "https://app.acuityscheduling.com/catalog.php?owner=XXXXX&action=addCart&clear=1&id=XXXX" --firstname "John" --surname "Doe" --phone "111222343" --email "john@doe.com" --code "test1234"
```