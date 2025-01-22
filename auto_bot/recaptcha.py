from seleniumbase import SB


try:

    with SB(uc=True, test=True, ad_block=True) as sb:
        url = "https://seleniumbase.io/apps/recaptcha"
        sb.activate_cdp_mode(url)
        sb.sleep(3.2)
        sb.uc_gui_handle_captcha()  # Try with TAB + SPACEBAR
        sb.assert_element("img#captcha-success", timeout=3)
        sb.set_messenger_theme(location="top_left")
        sb.post_message("SeleniumBase wasn't detected", duration=3)

    # with SB(uc=True, test=True, incognito=True) as sb:
    #     url = "https://seleniumbase.io/apps/recaptcha"
    #     sb.activate_cdp_mode(url)
    #     sb.sleep(1)
    #     sb.uc_gui_click_captcha('iframe[src*="/recaptcha/"]')
    #     sb.assert_element("img#captcha-success", timeout=3)
    #     sb.set_messenger_theme(location="top_left")
    #     sb.post_message("SeleniumBase wasn't detected", duration=3)
except:
    print("Something went wrong!")
    exit()

# with SB(uc=True, test=True,user_data_dir="C:/Users/USER/workspace/playground/auto_bot/2captcha") as sb:
    url = "https://2captcha.com/demo/recaptcha-v2-enterprise"
    sb.activate_cdp_mode(url)
    sb.sleep(2)
    sb.uc_gui_click_captcha()
    # sb.cdp.gui_click_element(".g-recaptcha div")
    # sb.uc_gui_handle_captcha()
    sb.sleep(2)

    # sb.assert_element("img#captcha-success", timeout=3)
    # sb.set_messenger_theme(location="top_left")
    # sb.post_message("SeleniumBase wasn't detected", duration=3)
