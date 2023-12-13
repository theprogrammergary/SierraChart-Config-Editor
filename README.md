# 👷🏼 (WIP) Sierra Chart Sierra4.config Editor

Configuring global graphics config colors in Sierra Chart is a pain in the ass. The end goal of this project is to include it in the TPH App. Users will be able to edit colors more efficiently by being able to mass change colors.

## Sample Byte Structure (Chart Text Color)

    // Start of bytes or definition
    C1 0A 54 00 14 00 04 00

    // 20 Global Graphic Configs
    // Each ends in 00 for a space
    - FF 80 FF 00
    - FF FF FF 00
    - FF FF FF 00
    - 00 00 00 00
    - 00 00 00 00
    - 00 00 00 00
    - 00 00 00 00
    - FF FF FF 00
    - FF FF FF 00
    - FF FF FF 00
    - FF FF FF 00
    - FF FF FF 00
    - FF FF FF 00
    - 00 00 00 00
    - 00 00 00 00
    - 00 00 00 00
    - 00 00 00 00
    - 00 00 00 00
    - 00 00 00 00
    - FF 80 FF 00

## Legend

    - 14 00 04 = Start of group
