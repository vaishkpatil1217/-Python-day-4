for i in range(7,0,-1):
    for j in range(7-i):
     print(" ",end="")
    for m in range(i):
        print("* ",end="")
    print("")

for i in range(1,7):
    for j in range(7-i):
     print(" ",end="")
    for m in range(i):
        print("* ",end="")
    print("")
    
    """  
* * * * * * * 
 * * * * * * 
  * * * * *  
   * * * *   
    * * *    
     * *     
      *      
      *
     * *
    * * *
   * * * *
  * * * * *
 * * * * * *"""