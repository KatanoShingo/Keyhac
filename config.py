﻿import sys
import os
import datetime
import pyauto
from keyhac import *
def configure(keymap):
 #どのウインドウにフォーカスがあっても効くキーマップ
    if 1:
        keymap_global = keymap.defineWindowKeymap()
#アプリ切り替え
        keymap_global[ "RS-Z" ] = "Win-1"
        keymap_global[ "RS-X" ] = "Win-2"
        keymap_global[ "RS-C" ] = "Win-3"
        keymap_global[ "RS-V" ] = "Win-4"
        keymap_global[ "RS-B" ] = "Win-5"
#ウィンドウの移動の配置変更
        keymap_global[ "LC-LW-Left" ] = "LW-LS-Left"
        keymap_global[ "LC-LW-Right" ] = "LW-LS-Right"
#仮想ウデスクトップ追加
        keymap_global[ "LC-LW-LA-N" ] = "LC-LW-D"
#仮想ウデスクトップ削除
        keymap_global[ "LC-LW-LA-Delete" ] = "LC-LW-F4"
#仮想ウデスクトップ移動
        keymap_global[ "LC-LW-LA-Left" ] = "LC-LW-Right"
        keymap_global[ "LC-LW-LA-Right" ] = "LC-LW-Left"
# アンダースコア入れ替え
        keymap_global[ "Underscore" ] = "S-Underscore"
        keymap_global[ "S-Underscore" ] = "Underscore"
#無変換、変換を未定義の仮想キーに置き換え
        keymap.replaceKey( 28, 58 )
        keymap.replaceKey( 29, 59 )
#IMEオン
        def ime_on():
            keymap.getWindow().setImeStatus(1)
        keymap_global[ "(58)" ] =  ime_on
#IMEオフ
        def ime_off():
            keymap.getWindow().setImeStatus(0)
        keymap_global[ "(59)" ] = ime_off

        keymap_chrome = keymap.defineWindowKeymap( exe_name="chrome.exe" )
#クローム用タブ切り替え
        keymap_chrome[ "RS-LS-Z" ] = "C-1"
        keymap_chrome[ "RS-LS-X" ] = "C-2"
        keymap_chrome[ "RS-LS-C" ] = "C-3"
        keymap_chrome[ "RS-LS-V" ] = "C-4"
        keymap_chrome[ "RS-LS-B" ] = "C-5"
#クローム用タブ削除
        keymap_chrome[ "LC-Delete" ] = "LC-W"