const Apify = require('apify');
Apify.main(async () => {
    const input = await Apify.getValue('INPUT');
    const input = await Apify.getValue('INPUT');
    console.log('Launching Puppeteer...');
    const browser = await Apify.launchPuppeteer();

    console.log('Sign in ...');
    const page = await browser.newPage();
    await page.goto('https://app.acuityscheduling.com/catalog.php?owner=XXXXXX&action=addCart&clear=1&id=XXXX');
    
    await page.type('#firstname', input.firstname);
    await page.type('#lastname', input.lastname);
    await page.type('#email', input.email);
    await page.type('#phone', input.phone);
    await page.type('[name=certificate]', input.code);
    await page.click('[name=updateqty]');
    await page.waitForSelector('#agree-to-terms-checkbox')
    await page.click('#agree-to-terms-checkbox')
    await page.click('[name=paylater]');
    await new Promise(resolve => setTimeout(resolve, 30000));

    console.log('Closing Puppeteer...');
    await browser.close();