==================================================================
              PixGuard - IMAGE ENCRYPTION TOOL
==================================================================

[ DESCRIPTION ]
PixGuard is a command-line tool developed in Python that performs 
image encryption through pixel manipulation. It allows users to 
obfuscate images using pixel channel swapping and mathematical 
XOR operations.

The encryption is symmetric, meaning the same process is used for 
both encryption and decryption.

[ FEATURES ]
1. Swap Pixels: Swaps the Red and Blue color channels.
2. XOR Pixels: Scrambles RGB values using a bitwise XOR operation 
   with a user-defined key (0-255).
3. Swap + XOR: Combines both methods for maximum obfuscation.
4. Smart Defaults: Automatically names output files and provides 
   a default security key (128) for ease of use.

==================================================================
[ PREREQUISITES ]
==================================================================
1. Python 3.x installed on your system.
2. The 'Pillow' (PIL) library.

[ INSTALLATION ]
If you do not have the Pillow library installed, run the following 
command in your terminal or command prompt:

    pip install pillow

==================================================================
[ HOW TO USE ]
==================================================================
1. Place the image you want to encrypt in the project folder.
2. Open your terminal/command prompt in this folder.
3. Run the script:

    python pixguard.py

4. Select a mode from the menu (1-3).
5. Enter the input filename (e.g., photo.jpg).
6. Enter an output filename (or press Enter for the default name).
7. (If using Mode 2 or 3) Enter a numeric key between 0-255.

==================================================================
[ HOW TO DECRYPT ]
==================================================================
To restore an encrypted image to its original state:

1. Run the tool again.
2. Select the SAME mode used for encryption.
3. Enter the path to the ENCRYPTED image.
4. Enter the SAME key used for encryption.

Note: If you used the default key during encryption, simply press 
Enter when asked for the key during decryption.

==================================================================
[ DISCLAIMER ]
This tool is for educational purposes to demonstrate pixel 
manipulation and basic cryptography concepts.
==================================================================