#Vowel Or Consonants
'''
Write a program to check whether the given character is vowel or consonant or Not an alphabet.

Input format: 

The input consist of a character 

Output format: 

The output consists of a below-given string “Vowel” / “Consonant” / “Not an alphabet”

Sample Input: 

a 

Sample Output: 

Vowel

 '''
char=input()
if(char>="a" and char<="z"):
    if(char=="a" or char=="e" or char=="i" or char=="o" or char=="u"):
        print("Vowel")
    else:
        print("Constant")
else:
    print("Not an alphabet")
