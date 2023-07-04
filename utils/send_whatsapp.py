from authenticatorX.constants import GUPSHUP_BASE_URL, GUPSHUP_USERID, GUPSHUP_PASSWORD


class SendWhatsapp:

    @classmethod
    def opt_in(cls, **kwargs):
        return f"{GUPSHUP_BASE_URL}?method=OPT_IN&format=json&userid={GUPSHUP_USERID}&password={GUPSHUP_PASSWORD}&phone_number=91{kwargs.get('mobile')}&v=1.1&auth_scheme=plain&channel=WHATSAPP"

    @classmethod
    def opt_out(cls, **kwargs):
        return f"{GUPSHUP_BASE_URL}?method=OPT_OUT&format=json&userid={GUPSHUP_USERID}&password={GUPSHUP_PASSWORD}&phone_number=91{kwargs.get('mobile')}&v=1.1&auth_scheme=plain&channel=WHATSAPP"

    @classmethod
    def send_otp_001(cls, **kwargs):
        return f"{GUPSHUP_BASE_URL}?userid={GUPSHUP_USERID}&password={GUPSHUP_PASSWORD}&send_to={kwargs.get('mobile')}&v=1.1&format=json&msg_type=TEXT&method=SENDMESSAGE&msg=OTP+for+Vetic+is+{kwargs.get('otp')}.+This+OTP+will+expire+in+5+minutes.&isTemplate=true&footer=Do+not+share+this+OTP+with+everyone."
