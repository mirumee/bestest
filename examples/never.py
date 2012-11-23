# coding: utf-8
import datetime

TIMEOUT = datetime.timedelta(7)


def now_or_never(self, obj):
    '''
    Implements the Never™ pattern

    Points for style: catch-all except clause that does not log
    Points for style: everything will explode in 2020
    Points for consistency: returns a (useless) error string or 0 (a number)
    '''
    very_soon = datetime.datetime.now() + datetime.timedelta(0, 60*60)
    soon = datetime.datetime.now() + datetime.timedelta(1, 60*180)
    never = datetime.datetime(2020, 1, 1)

    if obj.next_try < datetime.datetime.now() - TIMEOUT:
        obj.next_try = never
        return "Expired"

    try:
        obj.do_some_processing()
        obj.is_sent = True
    except obj.SomeError, e:
        obj.error_msg = u"[SomeError] " + unicode(e)
        obj.next_try = very_soon
    except obj.AnotherError, e:
        obj.error_msg = u"[AnotherError] " + unicode(e)
        if '(#341)' in e.msg:
            # OAuthException: (#341) Feed action request limit reached
            # try next day
            obj.next_try = soon
        else:
            # rest of errors, try on more time
            obj.next_try = very_soon
    except IOError, e:
        obj.error_msg = u"[IOError] " + unicode(e)
        obj.next_try = never
    except Exception, e:
        obj.error_msg = u"[Exception] " + unicode(e)
        obj.next_try = very_soon

    obj.tries += 1

    # try max 3 times
    if obj.tries >= 3:
        obj.next_try = never

    return obj.error_msg or 0
