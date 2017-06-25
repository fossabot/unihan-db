# -*- coding: utf8 - *-
from __future__ import (absolute_import, print_function, unicode_literals,
                        with_statement)

from unihan_db.tables import (UnhnLocation, UnhnLocationkXHC1983, UnhnReading,
                              kCantonese, kDefinition, kHanYu, kHanyuPinyin,
                              kIRGHanyuDaZidian, kMandarin, kTotalStrokes,
                              kXHC1983)


def import_char(c, char):
    if 'kDefinition' in char:
        for defi in char['kDefinition']:
            c.kDefinition.append(kDefinition(definition=defi))
    if 'kCantonese' in char:
        for defi in char['kCantonese']:
            c.kCantonese.append(kCantonese(definition=defi))
    if 'kMandarin' in char:
        defi = char['kMandarin']
        c.kMandarin.append(kMandarin(
            hans=defi['zh-Hans'],
            hant=defi['zh-Hant'],
        ))

    if 'kTotalStrokes' in char:
        defi = char['kTotalStrokes']
        c.kTotalStrokes.append(kTotalStrokes(
            hans=defi['zh-Hans'],
            hant=defi['zh-Hant'],
        ))

    if 'kHanyuPinyin' in char:
        for defi in char['kHanyuPinyin']:
            k = kHanyuPinyin()
            for loc in defi['locations']:
                k.locations.append(UnhnLocation(
                    volume=loc['volume'],
                    page=loc['page'],
                    character=loc['character'],
                    virtual=loc['virtual'],
                ))
            for reading in defi['readings']:
                k.readings.append(UnhnReading(reading=reading))
            c.kHanyuPinyin.append(k)

    if 'kHanYu' in char:
        for defi in char['kHanYu']:
            k = kHanYu()
            k.locations.append(UnhnLocation(
                volume=defi['volume'],
                page=defi['page'],
                character=defi['character'],
                virtual=defi['virtual'],
            ))
            c.kHanYu.append(k)

    if 'kIRGHanyuDaZidian' in char:
        for defi in char['kIRGHanyuDaZidian']:
            k = kIRGHanyuDaZidian()
            k.locations.append(UnhnLocation(
                volume=defi['volume'],
                page=defi['page'],
                character=defi['character'],
                virtual=defi['virtual'],
            ))
            c.kIRGHanyuDaZidian.append(k)

    if 'kXHC1983' in char:
        for defi in char['kXHC1983']:
            k = kXHC1983()
            for loc in defi['locations']:
                k.locations.append(UnhnLocationkXHC1983(
                    page=loc['page'],
                    character=loc['character'],
                    entry=loc['entry'],
                    substituted=loc['substituted'],
                ))
            k.readings.append(UnhnReading(reading=defi['reading']))
            c.kXHC1983.append(k)
