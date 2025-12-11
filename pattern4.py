for i in range(1,6):
    for j in range(6-i):
     print(" ",end="")
    for m in range(i):
        print("* ",end="")
    print("")
for i in range(6,0,-1):
    for j in range(6-i):
     print(" ",end="")
    for m in range(i):
        print("* ",end="")
    print("")
"""  * 
    * *
   * * *
  * * * *
 * * * * *
* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
     """ 
