class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        
        for i in tokens:
            if i=="+" or i=="/" or i=="*" or i=="-":
                a=int(st.pop())
                b=int(st.pop())
                if i=="+":
                    c=b+a
                elif i=="-":
                    c=b-a
                elif i=="/":
                    c=int(b/a)
                else:
                    c=b*a
                st.append(c)
            else:
                st.append(int(i))
        return st[0]


        