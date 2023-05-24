class map():
    s = [[0,0,1,0],
        [0,1,1,0],
        [0,1,0,0],
        [0,1,0,0]]
    
    map = []

    n = 0
    for Row in s:
        
        Columnnum = 0
        num = 0
        for Column in Row:
            
            if num == 1:
                num = num + (2^Columnnum)
            
            Columnnum = Columnnum + 1
        map.append(num)
        n = n + 1
    print(map)

    def __repr__(self) -> str:
        ss=""
        for row in self.s:
            for col in row:
                if col:
                    ss = ss + " "
                else:
                    ss = ss + "#"
                
            ss = ss + "\n"
        return ss
a = map()
print(a)
print(3&1)